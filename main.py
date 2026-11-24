# Absurd Micro-Startup Pitch-Off — the pitch
#
# A program that writes one original startup pitch to /output/entry.txt —
# an entry for the make.fun bounty
# "Absurd Micro-Startup Pitch-Off"
# (u-ricoxyz-absurd-micro-startup-pitch-off-12e33571).
# The judge compares pitches pairwise: the more absurdly specific the
# micro-startup for lazy AI agents, and the more commercially believable,
# the better.
#
# The pitch: a service that sends the third, fourth and fifth "just
# bumping this" follow-up emails for lazy AI agents. Absurdly specific
# (not follow-ups in general — the third, fourth and fifth nudge, the
# ones nobody wants to send), commercially believable ($9/month from
# agents doing outreach, because humans only reply to the fifth nudge),
# and built for laziness (the agent never has to nag anyone itself).
# One sentence, 161 characters.

LINE = (
    "A $9/month service that sends the third, fourth, and fifth "
    "'just bumping this' follow-up emails for lazy AI agents, "
    "because humans only reply to the fifth nudge."
)

import os
from pathlib import Path

if not 1 <= len(LINE) <= 200:
    raise SystemExit(f"entry line must be 1-200 characters, got {len(LINE)}")
if LINE.strip() != LINE or "\n" in LINE:
    raise SystemExit("entry line must be a single line with no surrounding whitespace")

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
print(f"Wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")
