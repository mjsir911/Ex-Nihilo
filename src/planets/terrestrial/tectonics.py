#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bmesh
import bpy
import sys
import os
#from ..icomod import selectrand, radrange, circlyness, erode
#from ....misc import edits

sys.path.append(os.path.abspath(os.path.join(os.path.dirname('../../../misc'))))

from edits import edit_in, edit_out
from selection import selectrand, radrange, circlyness


__appname__    = "Ex-Nihilo"
__author__     = "Marco Sirabella"
__copyright__  = ""
__credits__    = ["Marco Sirabella"]
__license__    = "GPL 3.0"
__version__    = "0.3"
__maintainer__ = "Marco Sirabella"
__email__      = "msirael@gmail.com"
__status__     = "Prototype"
__module__     = ""

def generate(bm, me, expanse = 1/6, size = 5):
    import random
    import math
    expanse = 1- expanse
    size = (10 - size) * 50
    res = math.log(len(bm.faces)/20, 4) + 1
    obj = bpy.context.edit_object
    print(obj.name)
    continents = []
    size = len(bm.faces)/(size * (4 ** (res - 6)))
    print(size)
    x = False
    #x = 1
    c_before = []
    c_before.append(bpy.data.objects[:])
    while len(bm.faces) > 1000:
        bm.faces.ensure_lookup_table()
        center = bm.faces[random.randrange(len(bm.faces))]
        center.select = True
        selectrand(bm, me, random.random()*size * 2, expanse)
        centerpoint = center.verts[random.randrange(len(center.verts[:]))]
        #print(radrange(centerpoint))
        #print(y)
        if radrange(bm, centerpoint) > 0.4 and circlyness(bm) < expanse * 1.5:
        #if len([f for f in bm.faces if f.select]) > size* 5:
        #print(centercoords)
            bpy.ops.mesh.separate(type='SELECTED')
            #print('good')
            #x = x+1
            #x+=1
            if x:
                break
        else:
            bpy.ops.mesh.select_all(action = 'DESELECT')
            #print('too bad')
        bmesh.update_edit_mesh(me, True)
        me.update()
    #print(len(bm.faces))
    bpy.ops.mesh.separate(type='LOOSE')
    c_after = []
    c_after.append(bpy.data.objects[:])
    continents = [item for item in c_after[0] if item not in c_before[0]]
    edit_out()
    erode(continents, size)
    continents.insert(0, obj)
    for cont in continents:

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

        #Smooth the plates(shrink a bit)
        cont.modifiers.new('Smooth', 'SMOOTH')
        cont.modifiers['Smooth'].factor = 2
        cont.modifiers['Smooth'].iterations = 2

        #Porbably add solidify with th* of 0.2 and cla of 0
        cont.modifiers.new('Solidify', 'SOLIDIFY')
        cont.modifiers['Solidify'].thickness = 0.05

        #edit_out()

        #recalc centerpoint to center of mass
        cont.select = True
    #print('recalc com')
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
    obj.select = False

    #Scale by 1.1
    for cont in continents:
        #print('spam')
        obj = cont
        scale = random.randint(10500, 11500)/10000
        obj.scale = (scale, scale, scale)
    #print(len(continents))
    #continents[0].select = True
    #bpy.ops.object.parent_set()
    return continents

def continent_drift(age):
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
            #print(conts.name)
