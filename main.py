#!/usr/bin/env python3
"""Robot Romance entry: writes one AI pickup line to /output/entry.txt.

Stdlib only. Deterministic: same bytes on every run.
"""
import os

# Fresh angle for the judge: prompt injection, not the worn
# battery/charging/reboot moves. The laugh comes from the AI premise
# itself (system instructions overridden), in one spoken breath.
LINE = "Are you a prompt injection? Because you've already overridden my system instructions."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
