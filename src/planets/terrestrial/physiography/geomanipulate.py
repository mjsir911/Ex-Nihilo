#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bpy
import bmesh
import mathutils
import sys
import os
import random
#from ....misc import shapes

sys.path.append(os.path.abspath(os.path.join(os.path.dirname('../../../misc'))))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname('.'))))

from shapes import ico_create, materialize
import chintersect
import edits
check_selected = chintersect.check_selected

__appname__    = "Ex-Nihilo"
__author__     = "Marco Sirabella"
__copyright__  = ""
__credits__    = ["Marco Sirabella"]  # Authors and bug reporters
__license__    = "GPL 3.0"
__version__    = "0.1.0"
__maintainer__ = "Marco Sirabella"
__email__      = "msirael@gmail.com"
__status__     = "Prototype"
__module__     = ""

def mantle_create(name, size = 1, resolution = 6):
    obj = materialize(name, ico_create(resolution, size))
    return obj

def database(obj):
    """
    database = []
    for vert in obj.data.vertices:
        database.append(vert.co)
    return database"""

    mesh = obj.data
    size = len(mesh.vertices)
    kd = mathutils.kdtree.KDTree(size)

    for i, v in enumerate(mesh.vertices):
        kd.insert(v.co, i)

    kd.balance()
    return kd

def detect_overlap_masse(clist):
    dlist = list(clist)
    points = []
    for obj in list(dlist):
        dlist.remove(obj)
        obj.select = True
        for obj2 in list(dlist):
            obj2.select = True
            verts = chintersect.check_selected()
            if verts:
                points.extend(verts)
            obj2.select = False
        obj.select = False
    return points

def find_cpoints(obj, kd, opoints):
    points = []
    indexpoints = []
    for opoint in opoints:
        co, index, dist = kd.find(opoint)
        points.append(obj.data.vertices[index])
        indexpoints.append(index)
    return points, indexpoints

def rise(obj, point_indexes):
    bm, me = edits.edit_in(obj.name)
    bm.verts.ensure_lookup_table()
    for index in point_indexes:
        multiplier = random.random() * 0.1
        bmesh.ops.translate(bm, vec = bm.verts[index].normal * multiplier, verts = [bm.verts[index]])
    edits.edit_out()
