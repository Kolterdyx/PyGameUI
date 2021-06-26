#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import sys

# with open("version.txt", 'r') as f:
#     version = [int(x) for x in f.read().strip().split(".")]
#     version[2] += 1
#     text = "".join([str(x) + "." for x in version])[:-1]
#
# with open("version.txt", "w") as f:
#     f.write(text)

os.system("python setup.py build") if sys.platform == 'win32' else os.system("python3 setup.py build")