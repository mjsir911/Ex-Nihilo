#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bpy
import bmesh
import math
from . import edits

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


def ico_create(sub, dia):
    import bmesh
    global scene
#    try:
#        bm.free()
    bm = bmesh.new()
    bmesh.ops.create_icosphere(bm, subdivisions=sub, diameter=dia)
    bm.verts.ensure_lookup_table()
    bm.faces.ensure_lookup_table()
    scene = bpy.context.scene
    return bm


def materialize(name, bm):
    scene = bpy.context.scene
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    me.update()
    obj = bpy.data.objects.new(name, me)
    scene.objects.link(obj)
    return obj


def autogen(name, size=6):
    materialize(name, ico_create(size, 1))
    edits.edit_in(name)


def group(object_list):
    for obj in object_list:
        obj.select = True
    bpy.context.scene.objects.active = bpy.data.objects[object_list[0].name]
    bpy.ops.object.parent_set()

"""
Thanks to Mutant Bob
http://blender.stackexchange.com/questions/53983/get-points-of-bezier-curve-in-coordinate-space-of-the-scene
"""


def interpBez3(bp0, t, bp3):
    # bp1, HR, HL, bp2

    return interpBez3_(bp0.co, bp0.handle_right, bp3.handle_left, bp3.co, t)
#    return interpBez3_(bp0.co, bp0.handle_left, bp3.handle_right, bp3.co, t)


def interpBez3_(p0, p1, p2, p3, t):
    r = 1-t
    return (r*r*r*p0 +
            3*r*r*t*p1 +
            3*r*t*t*p2 +
            t*t*t*p3)


def mission1(obj, t):

    i1 = math.floor(t)

    curve = obj.data


    bp1 = curve.splines[0].bezier_points[i1]
    bp2 = curve.splines[0].bezier_points[i1+1]

    coords = obj.matrix_world * interpBez3(bp1, t-i1, bp2)

    return coords
