#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dictionary
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

def generatea(length=None):
    if length:
        pass
    else:
        length = random.randrange(2,10)
    name = ""
    y = None
    for x in range(0, length):
        if y == "vowel" or y == None:
            if random.random() > 0.25:
                name += dictionary.constonants[random.randrange(0, len(dictionary.constonants))]
                y = "constonant"
            else:
                name += dictionary.vowels[random.randrange(0, len(dictionary.vowels))]
                y = "vowel"
        else:
            name += dictionary.vowels[random.randrange(0, len(dictionary.vowels))]
            y = "vowel"
    return(name)


def generate_advanced(length=None):
    if length:
        pass
    else:
        length = random.randrange(1,4)
    name = ""
    for x in range(0, length):
        name += dictionary.syllables[random.randrange(0, len(dictionary.syllables))]
    return name
