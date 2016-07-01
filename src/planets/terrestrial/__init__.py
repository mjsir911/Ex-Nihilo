#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from . import physiography, tectonics
from ...misc import shapes, edits

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
    planetary_core=None,
    planet_name="planet",
    seed='',
    resolution=6,
    tectonic_size=0.75,
    planet_age=None,
    continent_roundness=1 / 6,
    continent_size=5
):
    print(planet_name)
    import random
    if seed:
        random.seed(seed)
    if planet_age is None:
        planet_age = random.randrange(50000, 10000000)
    shapes.materialize('{0}_tectplates'.format(planet_name), shapes.ico_create(resolution, tectonic_size))
    bm, me = edits.edit_in('{0}_tectplates'.format(planet_name))
    # print(bm)
    continents = tectonics.generate(bm, me, expanse=continent_roundness, size=continent_size)
    tectonics.drift(planet_age)
    # group(continents)

    # Geography time
    obj = physiography.geomanipulate.mantle_create('{0}_mantle'.format(planet_name), size=tectonic_size * (4 / 3), resolution=resolution)
    kd = physiography.geomanipulate.database(obj)
    opoints = physiography.geomanipulate.detect_overlap_masse(continents)
    apoints, ipoints = physiography.geomanipulate.find_cpoints(obj, kd, opoints)
    physiography.geomanipulate.rise(obj, set(ipoints))
