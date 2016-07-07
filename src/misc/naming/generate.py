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

def generate_sound(length=None):
    if length:
        pass
    else:
        length = random.randrange(2,10)
    name = ""
    y = None
    for x in range(0, length):
        if y == "nucleus" or y == None:
            if random.random() > 0.25:
                name += dictionary.consonants[random.randrange(0, len(dictionary.consonants))]
                y = "consonant"
            else:
                name += dictionary.nucleus[random.randrange(0, len(dictionary.nucleus))]
                y = "nucleus"
        else:
            name += dictionary.nucleus[random.randrange(0, len(dictionary.nucleus))]
            y = "nucleus"
    return(name)


def generate_syllabic(length=None):
    if length:
        pass
    else:
        length = random.randrange(1,4)
    name = ""
    for x in range(0, length):
        name += dictionary.syllables[random.randrange(0, len(dictionary.syllables))]
    return name
