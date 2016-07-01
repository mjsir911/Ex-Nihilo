#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__appname__    = "Ex-Nihilo"
__author__     = "Marco Sirabella"
__copyright__  = ""
__credits__    = ["Marco Sirabella"]  # Authors and bug reporters
__license__    = "GPL 3.0"
__version__    = "0.1.0"
__maintainer__ = "Marco Sirabella"
__email__      = "msirael@gmail.com"
__status__     = "Prototype"
__module__     = ""

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]
