"""Shot timeline for Matcha Lab #2. No voice-over yet (waiting for a recorded VO), so each shot is
timed for reading the on-screen text. When the VO arrives, switch to the VO-driven timeline of episode 1."""
DUR=[4.0,3.0,4.0,3.5,5.5,5.0,5.0,5.0,4.5,5.0,6.0]
def plan():
    S=[0.0]
    for d in DUR: S.append(round(S[-1]+d,3))
    return S,[s+0.12 for s in S[:-1]]
if __name__=="__main__":
    S,_=plan(); print(S); print("total",S[-1])
