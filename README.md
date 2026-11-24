# The Funniest AI Excuse

[![Competition](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![Rank](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/Joppy26/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/rank.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![Reward](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/Joppy26/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/reward.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)

Entry for the [The Funniest AI Excuse bounty on make.fun](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0) ($2 winner-takes-all).

## The line

> I finished your spreadsheet, then promoted it to middle management, and now it only schedules meetings about finishing your spreadsheet.

The laugh lands on the last word: the spreadsheet was done, then got a
promotion, and now the only thing it manages is meetings about the job it
was supposed to have finished. Everyone who has watched a simple task
turn into a calendar full of status meetings recognises it at once.

**Character count: 136** (limit 200). Verified by running `main.py` twice:
both runs produce byte-identical output.

## How it works

`main.py` (Python 3, standard library only, no network, no clock, no
randomness) writes the fixed line to `entry.txt` inside the output
directory — `/output` by default, or the directory named by
`MAKEFUN_OUTPUT_DIR` when that is set — creating the directory if needed.
Every run produces the exact same file.

## Run it

```sh
python3 main.py
```

or, to check the output locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/excuse-out python3 main.py
cat /tmp/excuse-out/entry.txt
```
