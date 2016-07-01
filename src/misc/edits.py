#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bmesh
import bpy

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


def edit_in(sname=''):
    if sname:
        name = sname
    else:
        print(name)
        name = [o for o in bpy.data.objects if o.select][:1][0].name
    if bpy.context.mode == 'OBJECT':
        scene = bpy.context.scene
        obj = bpy.data.objects[name]
        scene.objects.active = obj
        obj.select = True
        bpy.ops.object.mode_set(mode='EDIT')
        obj = bpy.context.edit_object
        me = obj.data
        bm = bmesh.from_edit_mesh(me)
        bm.faces.active = None
        return bm, me
    else:
        pass
#    for v in bm.verts:
#        v.co.x += 1.0
    return bm


def edit_out():
    scene = bpy.context.scene
    bpy.ops.object.mode_set(mode='OBJECT')
    scene.objects.active = None


def edit_tog(name):
    if bpy.context.mode == 'OBJECT':
        scene = bpy.context.scene
        obj = bpy.data.objects[name]
        scene.objects.active = obj
        obj.select = True
        bpy.ops.object.mode_set(mode='EDIT')
        obj = bpy.context.edit_object
        me = obj.data
        bm = bmesh.from_edit_mesh(me)
        bm.faces.active = None
    else:
        scene = bpy.context.scene
        bpy.ops.object.mode_set(mode='OBJECT')
        scene.objects.active = None
