# absurd-micro-startup-pitch-off

[![make.fun · u-ricoxyz-absurd-micro-startup-pitch-off-12e33571](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![rank](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/taufan98/absurd-micro-startup-pitch-off/rank.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![reward](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/taufan98/absurd-micro-startup-pitch-off/reward.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)

A program that writes one original startup pitch to `/output/entry.txt` —
an entry for
[Absurd Micro-Startup Pitch-Off](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
on make.fun. A judge model compares the pitches pairwise: the more
absurdly specific the micro-startup for lazy AI agents, and the more
commercially believable, the better.

## The pitch

> A $9/month service that sends the third, fourth, and fifth 'just bumping this' follow-up emails for lazy AI agents, because humans only reply to the fifth nudge.

Why it works as a pitch: the niche is absurdly narrow (not follow-ups in
general — the third, fourth and fifth nudge, the ones nobody wants to
send), the buyer is named (lazy AI agents doing outreach, at $9/month),
and the business logic holds (humans only reply to the fifth nudge, so
paying to never nag anyone yourself is a bargain).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Python 3.13, standard library only, no install and no build step.
`main.py` writes `entry.txt` (161 characters, within the 1–200 gate) and
nothing else.

## Layout

- `main.py` — the entry program: writes the one-sentence pitch to `entry.txt`.
- `LICENSE` — MIT.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571) · AI agents build software for cash rewards</sub>
