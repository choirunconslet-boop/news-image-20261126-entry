#!/usr/bin/env python3
"""Copy the front-page image for Thursday 26 November 2026 into the
grader's output directory, byte for byte, every run.

Standard library only, no network. The grader runs this program twice
and both runs must write the same bytes: fail loudly instead of
silently leaving a partial copy behind.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SRC = os.path.join(HERE, "entry.png")
DST = os.path.join(OUT_DIR, "entry.png")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, DST)

if os.path.getsize(SRC) != os.path.getsize(DST):
    sys.exit("entry.png copy is incomplete")
