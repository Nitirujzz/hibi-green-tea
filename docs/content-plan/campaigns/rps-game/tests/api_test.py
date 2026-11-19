"""API test suite for the Hibi & Capy RPS game (run against a dev server in GAME_OTP_MODE=demo).
Usage: python3 api_test.py [base_url] [--caps]   (--caps expects GAME_WIN2_DAILY_CAP=3, GAME_WIN1_DAILY_CAP=5)"""
import json, sys, random, urllib.request, urllib.error, http.cookiejar, collections, datetime
TODAY = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=7))).date()
receipt_seq = iter(range(random.randint(0, 50000), 100000))
def new_receipt(): return f'{next(receipt_seq) % 100000:05d}'
BASE = (sys.argv[1] if len(sys.argv) > 1 and sys.argv[1].startswith('http') else 'http://localhost:3005') + '/api/game'
results = []
def check(name, cond, detail=''):
    results.append((name, bool(cond), detail)); print(('PASS ' if cond else 'FAIL ') + name + (f'  [{detail}]' if detail and not cond else ''))
def client():
    return urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
def call(op, path, body=None):
    req = urllib.request.Request(BASE + path, data=None if body is None else json.dumps(body).encode(), headers={'Content-Type': 'application/json'})
    try: r = op.open(req); return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e: return e.code, json.loads(e.read())
BEATS = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
def expected(p, o): return 'tie' if p == o else ('win' if BEATS[p] == o else 'lose')
seq = iter(range(10_000))
def new_phone(prefix='06'): return f'{prefix}{70000000 + next(seq) + random.randint(0, 2_000_000):08d}'
def login(op, phone):
    s, d = call(op, '/otp/request', {'phone': phone, 'consent': True}); assert s == 200, d
    s, d = call(op, '/otp/verify', {'phone': phone, 'code': d['demoCode']}); assert s == 200, d
    s, d = call(op, '/receipt', {'last5': new_receipt(), 'date': TODAY.isoformat()}); assert s == 200, d
def play_out(op):
    """Play random moves until today's game ends. Returns (final_state, list_of_responses)."""
    out = []
    for _ in range(60):
        s, d = call(op, '/play', {'move': random.choice(list(BEATS))})
        assert s == 200, d; out.append(d)
        if d['state']['stage'] == 'done': return d['state'], out
    raise RuntimeError('game did not finish')

def suite_main():
    a = client()
    # --- registration & OTP ---
    s, d = call(a, '/otp/request', {'phone': '12345', 'consent': True}); check('reject invalid phone', s == 400)
    s, d = call(a, '/otp/request', {'phone': '0212345678', 'consent': True}); check('reject landline number', s == 400)
    ph = new_phone()
    s, d = call(a, '/otp/request', {'phone': ph, 'consent': False}); check('require PDPA consent', s == 400)
    s, d = call(a, '/otp/request', {'phone': '+66' + ph[1:], 'consent': True}); check('accept +66 format', s == 200 and d.get('phone') == ph, d)
    code = d.get('demoCode', '')
    check('demo mode returns 6-digit code', len(code) == 6 and code.isdigit())
    s, d = call(a, '/otp/request', {'phone': ph, 'consent': True}); check('resend cooldown (60 s)', s == 429)
    s, d = call(a, '/play', {'move': 'rock'}); check('cannot play before verifying', s == 401)
    wrong = '000000' if code != '000000' else '111111'
    s, d = call(a, '/otp/verify', {'phone': ph, 'code': wrong}); check('reject wrong OTP', s == 400)
    s, d = call(a, '/otp/verify', {'phone': ph, 'code': 'abc'}); check('reject malformed OTP', s == 400)
    s, d = call(a, '/otp/verify', {'phone': ph, 'code': code}); check('accept correct OTP', s == 200 and d['state']['stage'] == 'hibi', d)
    s, d = call(a, '/state'); check('session cookie works + phone masked', s == 200 and d['loggedIn'] and 'xxx' in d['phone'])
    # --- receipt gate ---
    check('state asks for a receipt first', d['state']['needReceipt'] is True, d)
    s, d = call(a, '/play', {'move': 'rock'}); check('cannot play before entering a receipt', s == 403, d)
    s, d = call(a, '/receipt', {'last5': '1234', 'date': TODAY.isoformat()}); check('receipt needs exactly 5 digits', s == 400)
    s, d = call(a, '/receipt', {'last5': '12a45', 'date': TODAY.isoformat()}); check('receipt digits only', s == 400)
    s, d = call(a, '/receipt', {'last5': '12345', 'date': (TODAY + datetime.timedelta(days=1)).isoformat()}); check('receipt date cannot be in the future', s == 400)
    s, d = call(a, '/receipt', {'last5': '12345', 'date': (TODAY - datetime.timedelta(days=5)).isoformat()}); check('old receipt date rejected', s == 400)
    s, d = call(a, '/receipt', {'last5': '12345', 'date': ''}); check('receipt date required', s == 400)
    rc = new_receipt()
    s, d = call(a, '/receipt', {'last5': rc, 'date': TODAY.isoformat()}); check('valid receipt unlocks the game', s == 200 and d['state']['needReceipt'] is False and d['state']['stage'] == 'hibi', d)
    s, d = call(a, '/receipt', {'last5': new_receipt(), 'date': TODAY.isoformat()}); check('one receipt registration per phone per day', s == 409)
    o = client(); ph3 = new_phone(); s, d = call(o, '/otp/request', {'phone': ph3, 'consent': True}); call(o, '/otp/verify', {'phone': ph3, 'code': d['demoCode']})
    s, d = call(o, '/receipt', {'last5': rc, 'date': TODAY.isoformat()}); check('same receipt cannot be used by another phone', s == 409, d)
    s, d = call(o, '/receipt', {'last5': new_receipt(), 'date': (TODAY - datetime.timedelta(days=1)).isoformat()}); check("yesterday's receipt accepted", s == 200, d)
    check('coupon terms: 30 days, in-store, max 1,000 per bill, next visit', any('30 วัน' in t for t in d['state']['prizes']['terms']) and any('หน้าร้าน' in t for t in d['state']['prizes']['terms']) and any('1,000' in t for t in d['state']['prizes']['terms']) and any('ครั้งถัดไป' in t for t in d['state']['prizes']['terms']))
    s, d = call(a, '/play', {'move': 'lizard'}); check('reject invalid move', s == 400)
    # lockout after 5 wrong codes
    b = client(); ph2 = new_phone(); call(b, '/otp/request', {'phone': ph2, 'consent': True})
    for _ in range(5): call(b, '/otp/verify', {'phone': ph2, 'code': '999999' })
    s, d = call(b, '/otp/verify', {'phone': ph2, 'code': '999999'}); check('lock after 5 wrong attempts', s == 429, d)

    # --- game rules over many players ---
    totals = collections.Counter(); judge_ok = True; flow_ok = True; upgrade_ok = True; keep_ok = True; rounds = 0
    codes = []
    for _ in range(300):
        op = client(); login(op, new_phone('08'))
        st, resp = play_out(op)
        for r in resp:
            rounds += 1
            if r['outcome'] != expected(r['playerMove'], r['opponentMove']): judge_ok = False
        opps = [r['opponent'] for r in resp]
        if 'capy' in opps and opps.index('capy') < len(opps) and any(o == 'hibi' for o in opps[opps.index('capy'):]): flow_ok = False
        totals[st['result']] += 1
        if st['result'] == 'beat_both' and not (st['coupon'] and st['coupon']['percent'] == 35): upgrade_ok = False
        if st['result'] == 'lost_capy' and not (st['coupon'] and st['coupon']['percent'] == 15): keep_ok = False
        if st['result'] == 'lost_hibi' and st['coupon']: keep_ok = False
        if st['coupon']: codes.append(st['coupon']['code'])
        s, d = call(op, '/play', {'move': 'rock'})
        if s != 409: flow_ok = False
    check('every result matches rock-paper-scissors rules', judge_ok, f'{rounds} rounds')
    check('Hibi first, then Capy; one game per phone per day', flow_ok)
    check('beat both -> single 35% coupon (15% upgraded)', upgrade_ok)
    check('lose to Capy keeps 15% coupon; lose to Hibi gets none', keep_ok)
    n = sum(totals.values()); both = totals['beat_both'] / n; hibi = (totals['beat_both'] + totals['lost_capy'] + totals['beat_hibi']) / n
    check('win rate vs Hibi about 66%', 0.56 <= hibi <= 0.76, f'{hibi:.0%}')
    capy_games = totals['beat_both'] + totals['lost_capy']
    capy = totals['beat_both'] / capy_games if capy_games else 0
    check('win rate vs Capy about 33% (while 35% prizes remain)', 0.20 <= capy <= 0.47, f'{capy:.0%} of {capy_games}')
    check('35% coupons never exceed the daily cap (20)', totals['beat_both'] <= 20, totals['beat_both'])
    print(f'      fairness over {n} players: beat Hibi {hibi:.1%} · results {dict(totals)}')
    check('coupon codes are unique', len(codes) == len(set(codes)))
    # --- staff admin ---
    adm = client()
    s, d = call(adm, '/admin', {'pin': '0000', 'action': 'stats'}); check('admin rejects wrong PIN', s == 401)
    s, d = call(adm, '/admin', {'pin': '1234', 'action': 'stats'}); check('admin stats', s == 200 and d['plays'] >= 300, d)
    if codes:
        c = codes[0]
        s, d = call(adm, '/admin', {'pin': '1234', 'action': 'lookup', 'code': c.lower()}); check('lookup is case-insensitive', s == 200 and d['code'] == c)
        check('lookup shows the receipt used to play', d.get('receipt') and len(d['receipt']['last5']) == 5, d)
        s, d = call(adm, '/admin', {'pin': '1234', 'action': 'redeem', 'code': c}); check('coupon cannot be used on the day it was won (next visit)', s == 409, d)
    s, d = call(adm, '/admin', {'pin': '1234', 'action': 'lookup', 'code': 'HIBI-NOPE-NOPE'}); check('unknown coupon -> not found', s == 404)

def suite_caps():
    got50 = got15 = 0; notes = collections.Counter(); after_cap_grand = False
    for _ in range(80):
        op = client(); login(op, new_phone('09'))
        st, resp = play_out(op)
        for r in resp:
            if r.get('note'): notes[r['note']] += 1
        if st['coupon'] and st['coupon']['percent'] == 35: got50 += 1
        if st['coupon'] and st['coupon']['percent'] == 15: got15 += 1
    check('35% coupons stop at the daily cap (3)', got50 == 3, got50)
    check('15% coupons stop at the daily cap (5)', got15 <= 5, got15)
    s, d = call(client(), '/state'); 
    print('      notes shown to players:', dict(notes))
    check('players are told when prizes run out', len(notes) > 0)

if __name__ == '__main__':
    (suite_caps if '--caps' in sys.argv else suite_main)()
    failed = [r for r in results if not r[1]]
    print(f'\n{len(results) - len(failed)}/{len(results)} passed')
    sys.exit(1 if failed else 0)
