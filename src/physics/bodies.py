#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bpy
import bmesh
import math
import mathutils
import random
from ..misc import crandom
from ..misc import shapes
from ..planets.terrestrial.physiography import geomanipulate

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


def find_dist(obj, kd, opoint):
    co, index, dist = kd.find(opoint)
    points.append(obj.data.vertices[index])
    indexpoints.append(index)
    return points, indexpoints


def orbit(name, rev, porbits, orbitdistort=250, detail=25, dist=2):
    scene = bpy.context.scene

    # Create & distort orbit
    bpy.ops.curve.primitive_bezier_circle_add(
        location=(0, 0, 0),
        rotation=(math.radians(0), math.radians(0), math.radians(0)))
    orbit = bpy.context.active_object
    orbit.name = '{0}_orbit'.format(name)
    scale = random.uniform(1, 15)
    orbit.scale = ((
        (random.randrange(1000 - orbitdistort, 1000 + orbitdistort) / 1000) * scale,
        (random.randrange(1000 - orbitdistort, 1000 + orbitdistort) / 1000) * scale,
        0.5))

    weights = [(16, 1), (8, 5), (4, 14)]
    orbit.rotation_mode = 'XYZ'
    orbit.rotation_euler = (
        math.radians((random.random() - 0.5) * 2 * crandom.weighted_choice(weights)),
        math.radians((random.random() - 0.5) * 2 * crandom.weighted_choice(weights)),
        math.radians((random.random() - 0.5) * 2 * 180))

    # Check to see if close to any other orbits
    # kd = geomanipulate.database(orbit)
    kd = mathutils.kdtree.KDTree(detail)
    for x in range(0, detail):
        kd.insert(shapes.mission1(orbit, random.uniform(-1, 3)), x)
    kd.balance()

    print('kdtree created')
    for circle in porbits:
        #print("checking range")
        for x in range(0, detail):
            if kd.find_range(
                shapes.mission1(circle, random.uniform(-1, 3)), dist
            ):
                print("too close")
                orbit.select = True
                bpy.ops.object.delete()
                return None, None
                print("youshouldntbehere.gif")

    # Create core
    core = bpy.data.objects.new('{0}_core'.format(name), None)
    core.constraints.new('FOLLOW_PATH')
    core.constraints['Follow Path'].target = orbit
    core.constraints['Follow Path'].offset = rev

    bpy.ops.object.select_all(action='DESELECT')
    scene.objects.link(core)
    scene.update()
    return core, orbit
