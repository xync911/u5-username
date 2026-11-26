"""Copy entry.txt to the output directory for the make.fun entry.

The entry is our own make.fun username and nothing else, one
word, at most 30 characters.
xync911: the handle itself is the entry. No explanation, no
links, no pitch — the judge reads the username and decides
whether it feels funnier or more interesting than the next one.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
# The entry text is copied verbatim; the judge reads it exactly as written.
# Verify the copy is byte-identical to the source.
assert open(SRC, "rb").read() == open(OUT, "rb").read(), "output differs from entry.txt"
