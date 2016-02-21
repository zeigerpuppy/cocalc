#!/usr/bin/env python3

import os
from os.path import join, abspath, normpath, exists, dirname
from codecs import open

TARG = join(abspath(dirname(__file__)), "..", "static", "about")

if not exists(TARG):
    os.mkdir(TARG)

with open(join(TARG, "index.html"), "w", "utf8") as index:
    index.write("SMC HELP")