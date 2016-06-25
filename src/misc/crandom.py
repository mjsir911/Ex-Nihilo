#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

__appname__    = "Custom functions built off of random"
__author__     = "Marco Sirabella"
__copyright__  = ""
__credits__    = ["Marco Sirabella"]  # Authors and bug reporters
__license__    = "GPL"
__version__    = "1.0"
__maintainer__ = "Marco Sirabella"
__email__      = "msirabel@gmail.com"
__status__     = "Prototype"  # "Prototype", "Development" or "Production"
__module__     = ""

"""
Thanks to Ned Batchelder and moooeeeep from stackoverflow for this
http://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
"""
def weighted_choice(choices):
   total = sum(w for c, w in choices)
   r = random.uniform(0, total)
   upto = 0
   for c, w in choices:
      upto += w
      if upto + w >= r:
         return c
   assert False, "Shouldn't get here"
