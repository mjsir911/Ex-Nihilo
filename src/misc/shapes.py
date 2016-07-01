#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bpy
import bmesh
from . import edits

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
