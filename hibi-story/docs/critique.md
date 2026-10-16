# Hibi Brand Story: critique log (9x16)

## Round 1
| hook | read | motion | variety | brand | sync | min |
|  7   |  7   |   7    |    7    |   8   |  7   |  7  |

Worst three:
1. [all scenes] Mascots too small (Hibi ~200 px tall in S2/S3, Capy small in S4/S6/S8). They are the brand's charm and read as specks on the phone sheet. -> Scale Hibi 0.62→0.8–0.9, Capy 0.85–0.95→1.05–1.2. Bigger notebook; removed the progress dots that collided with Capy.
2. [b14-15] The tile row stayed on screen while the price tag and the doubt line arrived, so tiles, tag and header overlapped. -> Lift the row faster (snappy, from b13.55, −1100 px).
3. [b22, b40] Downbeat frames almost empty (cards land at b23.5+; S8 characters arrive after b40). -> Card track moved to land at b22.8/25.9/28.9; S8 tiles and characters enter from b39.55.
Also: price tag drawn behind the S5 type; AI label 30→34 px.
Checks failed: no-blank-downbeat (b22, b40).
Verdict: ANOTHER ROUND

## Round 2
| hook | read | motion | variety | brand | sync | min |
|  8   |  8   |   8    |    8    |   8   |  8   |  8  |

Sync: 51/63 hits within 20 ms of an onset, median 4.6 ms. The misses are peak-anchored whooshes/swells with soft onsets, not drift. Mix at −14.0 LUFS, −1.2 dBTP.
Worst three:
1. [b14] Doubt beat still opened on a near-empty frame (tag mid-drop, no text). -> Tag drops from b13.55 (lands on the b14 thud); lines rise at b13.95 / b14.45; Hibi and Capy enter from b13.7 / b13.95.
2. [b16] The falling tag sat on top of "ของดี" at the drop. -> Tag falls faster (b15.5–16.4) and drifts left, out of the type's way.
3. [b44] At the clink the glasses were ~170 px apart and the sparkle floated above them. -> Characters 55 px closer each; sparkle moved to the glass rims (525, 1215).
Verdict: ANOTHER ROUND (round 3 minimum)

## Round 3
| hook | read | motion | variety | brand | sync | min |
|  8   |  9   |   8    |    8    |   8   |  8   |  8  |

Fixed:
1. [b15.8-16] The whisk wipe left ~0.2 s of plain matcha before "ของดี" rose, so the drop frame was blank. -> The wipe now clips and reveals S5 already in motion; "ของดี" starts at b15.6.
2. [b39.5-40] During the push, Hibi poked out over the dark S7 frame. -> S8 clipped to its own panel during the push.
Checks: no banned defaults (the AI label is a brief requirement, not decoration); longest gap is the b52-56 end-card hold (2.7 s, intended); one accent (matcha); end card holds 2.7 s; flashes only at b16 (drop) and b48 (logo).
Verdict: READY

Remaining (next pass, not blocking):
- Swap the placeholder 日々 logo for the real logo file.
- S7: the pour could get a small splash ring at the glass surface.
- S1: Hibi's landing on 々 could kick up a tiny ink ripple from the stamp.
