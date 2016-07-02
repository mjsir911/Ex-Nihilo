#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bmesh
import bpy
import sys
import os
# from ..icomod import selectrand, radrange, circlyness, erode
from ...misc import edits, selection

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname('../../../misc'))))

# from edits import edit_in, edit_out
# from selection import selectrand, radrange, circlyness

__appname__    = "Ex-Nihilo"
__author__     = "Marco Sirabella"
__copyright__  = ""
__credits__    = ["Marco Sirabella"]
__license__    = "GPL 3.0"
__version__    = "0.2.0"
__maintainer__ = "Marco Sirabella"
__email__      = "msirael@gmail.com"
__status__     = "Prototype"
__module__     = ""


def generate(bm, me, expanse=1 / 6, size=5, randomrange=0.10):
    import random
    import math
    expanse = 1 - expanse
    size = (10 - size) * 50
    res = math.log(len(bm.faces) / 20, 4) + 1
    obj = bpy.context.edit_object
    print(obj.name)
    continents = []
    size = len(bm.faces) / (size * (4 ** (res - 6)))
    print(size)
    x = False
    # x = 1
    c_before = []
    c_before.append(bpy.data.objects[:])
    while len(bm.faces) > 1000:
        bm.faces.ensure_lookup_table()
        center = bm.faces[random.randrange(len(bm.faces))]
        center.select = True
        selection.selectrand(bm, me, random.random() * size * 2, expanse)
        centerpoint = center.verts[random.randrange(len(center.verts[:]))]
        # print(radrange(centerpoint))
        # print(y)
        # if len([f for f in bm.faces if f.select]) > size* 5:
        if selection.radrange(bm, centerpoint) > 0.4 and selection.circlyness(bm) < expanse * 1.5:
            # print(centercoords)
            bpy.ops.mesh.separate(type='SELECTED')
            # print('good')
            # x = x+1
            # x+=1
            if x:
                break
        else:
            bpy.ops.mesh.select_all(action='DESELECT')
            # print('too bad')
        bmesh.update_edit_mesh(me, True)
        me.update()
    # print(len(bm.faces))
    bpy.ops.mesh.separate(type='LOOSE')
    c_after = []
    c_after.append(bpy.data.objects[:])
    continents = [item for item in c_after[0] if item not in c_before[0]]
    edits.edit_out()
    erode(continents, size)
    continents.insert(0, obj)
    # print(len(continents))
    # continents[0].select = True
    # bpy.ops.object.parent_set()
    drift(1, continents)
    rescale(continents, randomrange)
    return continents


def drift(age, list):
    from random import uniform
    from math import radians
    for item in list:
        item.rotation_euler =\
            radians(uniform(-1, 1) * age),\
            radians(uniform(-3, 3) * age),\
            radians(uniform(-3, 3) * age)
    """for cont in continents:
        obj = bpy.data.objects[cont.name]
        obj.scale[0] = random.randrange(75, 125, 5) / 100
        obj.scale[1] = random.randrange(75, 125, 5) / 100
        obj.scale[2] = random.randrange(75, 125, 5) / 100"""


def erode(list, size):
    for item in bpy.context.selectable_objects:
        item.select = False
    for conts in list:
        if len(conts.data.vertices) < size:
            conts.select = True
            list.remove(conts)
            bpy.ops.object.delete()
            # print(conts.name)


def rescale(list, randomrange):
    import random
    bpy.ops.object.select_all(action='DESELECT')
    for item in list:

        """
        #Categorize under original object
        print('parent = ' + obj.name)
        print('child = ' + cont.name)
        bpy.ops.outliner.parent_drop(child = cont.name, parent = obj.name)
        """
        """
        edit_in(cont.name)
        move each plate out 0.02-- replaced by smooth
        for face in bm.faces:
            face.select = True
        transout(0.02)"""

        # Smooth the plates(shrink a bit)
        item.modifiers.new('Smooth', 'SMOOTH')
        item.modifiers['Smooth'].factor = 2
        item.modifiers['Smooth'].iterations = 2

        # Porbably add solidify with th* of 0.2 and cla of 0
        item.modifiers.new('Solidify', 'SOLIDIFY')
        item.modifiers['Solidify'].thickness = 0.05

        # edit_out()

        # recalc centerpoint to center of mass
        item.select = True
        bpy.context.scene.objects.active = item
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier='Smooth')
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier='Solidify')
    # print('recalc com')
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
    bpy.ops.object.select_all(action='DESELECT')

    # Scale by 1.1
    for item in list:
        # print('spam')
        scale = random.uniform(1.05, 1.05 + randomrange)
        item.scale = (scale, scale, scale)
