#!/usr/bin/env python3
"""Copy the entry image into the make.fun output directory.

The entry image (entry.png) sits in this repo next to this script.
Running this script copies it, byte for byte, to the output directory
given by the MAKEFUN_OUTPUT_DIR environment variable (default /output)
as entry.png, creating the directory first if it does not exist yet.
The source is resolved from the script's own location, so the copy
works no matter which directory the script is run from.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, out_dir / "entry.png")


if __name__ == "__main__":
    main()
