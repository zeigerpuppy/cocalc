#!/usr/bin/env python3

import os
from os.path import join, abspath, normpath, exists, dirname
from datetime import datetime
from codecs import open

TARG = join(abspath(dirname(__file__)), "..", "static", "pages")
YEAR = datetime.utcnow().year

def render():
    if not exists(TARG):
        os.mkdir(TARG)

    with open(join(TARG, "about", "index.html"), "w", "utf8") as index:
        index.write("SMC HELP + %s" % YEAR)

def main():
    render()

if __name__ == "__main__":
    main()