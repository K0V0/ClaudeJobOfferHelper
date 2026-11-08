#!/usr/bin/env python3
"""Builds the one file save-offer executable for this system into dist/.

Usage: python scripts/build_executable.py <output name>   (needs pyinstaller, requests, beautifulsoup4)
"""
import sys
from pathlib import Path

import PyInstaller.__main__

SCRIPTS = Path(__file__).resolve().parent

arguments = ["--onefile", "--noconfirm", "--clean", "--name", sys.argv[1], "--paths", str(SCRIPTS), "--specpath", "build"]
for path in sorted(SCRIPTS.glob("*/extract.py")):  # loaded from files at run time, PyInstaller can not see them
    arguments += ["--add-data", f"{path}:{path.parent.name}"]
PyInstaller.__main__.run([*arguments, str(SCRIPTS / "save_offer.py")])
