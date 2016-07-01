#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__appname__    = "Ex-Nihilo"
__author__     = "Marco Sirabella"
__copyright__  = ""
__credits__    = ["Marco Sirabella"]  # Authors and bug reporters
__license__    = "GPL 3.0"
__version__    = "0.2.0"
__maintainer__ = "Marco Sirabella"
__email__      = "msirael@gmail.com"
__status__     = "Prototype"
__module__     = ""


def generate(
    start_revolution=None,
    orbital_distortion=250,
    planet_name='planet'
):
    if start_revolution is None:
        start_revolution = random.randint(0, 99)
    core, orbit = metagen(planet_name, start_revolution, orbital_distortion)
