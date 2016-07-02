#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from . import bodies

__appname__    = "Ex-Nihilo"
__author__     = "Marco Sirabella"
__copyright__  = ""
__credits__    = ["Marco Sirabella"]  # Authors and bug reporters
__license__    = "GPL 3.0"
__version__    = "0.3.0"
__maintainer__ = "Marco Sirabella"
__email__      = "msirael@gmail.com"
__status__     = "Prototype"
__module__     = ""


def generate(
    porbits=[],
    start_revolution=None,
    orbital_distortion=250,
    planet_name='planet',
    orbital_detailWIP=10,
    distance_range=1
):
    # porbits=[]
    detail = orbital_detailWIP
    if start_revolution is None:
        start_revolution = random.randint(0, 99)
    core, orbit = bodies.orbit(planet_name, start_revolution, porbits, orbital_distortion, detail, distance_range)
    return core, orbit


def generate_masse(
    orbital_amount=10,
    detail=10,
    dist=1
):
    porbits = []
    x = 0
    while len(porbits) < orbital_amount:
        x += 1
        core, orbit = generate(porbits=porbits, orbital_detailWIP=detail, distance_range=dist)
        if orbit:
            porbits.append(orbit)
        if x > 100:
            break
