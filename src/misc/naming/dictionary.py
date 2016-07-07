#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string
import random

__appname__    = "Ex-Nihilo"
__author__     = "Marco Sirabella"
__copyright__  = ""
__credits__    = ["Marco Sirabella"]  # Authors and bug reporters
__license__    = "GPL 3.0"
__version__    = "0.3.0"
__maintainer__ = "Marco Sirabella"
__email__      = "msirabel@gmail.com"
__status__     = "Prototype"
__module__     = ""

onset = list(
        set(string.ascii_lowercase)
        - set('aeiou')
        - set('qxc')
        | set(['bl', 'br', 'cl', 'cr', 'dr', 'fl',
            'fr', 'gl', 'gr', 'pl', 'pr', 'sk',
            'sl', 'sm', 'sn', 'sp', 'st', 'str',
            'sw', 'tr', 'ch', 'sh'])
)

nucleus = list(
        'aeiou'
)

coda = list(
        set(string.ascii_lowercase)
        - set('aeiou')
        | set(['ct', 'ft', 'mp', 'nd', 'ng', 'nk', 'nt',
            'pt', 'sk', 'sp', 'ss', 'st', 'ch', 'sh'])
)

syllables_temp = []

#for o in onset:
#    for n in nucleus:
#        for c in coda:
#            if random.random() > 0.5:
#                syllables_temp.append(o + n + c)
#            else:
#                syllables_temp.append(o + n)

syllables = list([o+s+c for o in onset for s in nucleus for c in coda])
