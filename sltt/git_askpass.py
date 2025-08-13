#!/usr/bin/env python3
import os
import sys

if sys.argv[1].startswith("Username"):
    print("git")
    sys.exit(0)
if sys.argv[1].startswith("Password"):
    print(os.environ["GITHUB_TOKEN"])
    sys.exit(0)

sys.exit(1)
