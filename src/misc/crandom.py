#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import bisect

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

"""
Thanks to Raymond Hettinger and Lev Levitsky from stackoverflow for this
http://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
"""
def weighted_choice(choices):
    #import random
    #import bisect
    values, weights = zip(*choices)
    total = 0
    cweights = []
    for w in weights:
        total += w
        cweights.append(total)
    x = random.random() * total
    i = bisect.bisect(cweights, x)
    return values[i]
