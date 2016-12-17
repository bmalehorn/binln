#!/usr/bin/env python2

USAGE = """
USAGE:
    $ binln foo.py bar.sh
    /home/brian/bin/foo -> /path/to/foo.py
    /home/brian/bin/bar -> /path/to/bar.sh
"""

# installation:
# $ ./binln.py binln.py

import subprocess
import sys
import os

# ~/bin
BIN_PATH = os.path.join(os.environ["HOME"], "bin")

def main():
    args = sys.argv[1:]
    force = False
    if args[0] == "--force" or args[0] == "-f":
        force = True
        args = args[1:]
    for f in args:
        link_f(f, force)

def link_f(f, force):
    if not os.path.exists(f):
        print "file %r not found" % f
        print USAGE
        return
    if f.startswith("/"):
        f_abs_path = f
    else:
        cwd = os.environ["PWD"]
        f_abs_path = os.path.join(cwd, f)
    lnk = f.split("/")[-1].split(".")[0]
    lnk_abs_path = os.path.join(BIN_PATH, lnk)
    subprocess.call(["chmod", "u+x", f_abs_path])
    if os.path.isfile(lnk_abs_path) and force:
        subprocess.call(["rm", "-v", lnk_abs_path])
    subprocess.call(["ln", "-sv", f_abs_path, lnk_abs_path])

main()
