#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bpy
import bmesh

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


def metagen(name, rev, orbitdistort=250):
    import math
    import random
    import crandom
    scene = bpy.context.scene

    # Create & distort orbit
    bpy.ops.curve.primitive_bezier_circle_add(
        location=(0, 0, 0),
        rotation=(math.radians(0), math.radians(0), math.radians(0)))
    orbit = bpy.context.active_object
    orbit.name = '{0}_orbit'.format(name)

    orbit.scale = ((
        random.randrange(1000 - orbitdistort, 1000 + orbitdistort) / 1000,
        random.randrange(1000 - orbitdistort, 1000 + orbitdistort) / 1000,
        0.5))

    weights = [(16, 1), (8, 5), (4, 14)]
    orbit.rotation_mode = 'XYZ'
    orbit.rotation_euler = (
        math.radians((random.random() - 0.5) * 2 * crandom.weighted_choice(weights)),
        math.radians((random.random() - 0.5) * 2 * crandom.weighted_choice(weights)),
        math.radians((random.random() - 0.5) * 2 * 180))

    # Create core
    core = bpy.data.objects.new('{0}_core'.format(name), None)
    core.constraints.new('FOLLOW_PATH')
    core.constraints['Follow Path'].target = orbit
    core.constraints['Follow Path'].offset = rev

    bpy.ops.object.select_all(action='DESELECT')
    scene.objects.link(core)
    scene.update()
    return core, orbit
