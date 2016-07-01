#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bpy
import bmesh
import random

__appname__    = "Ex-Nihilo"
__author__     = "Marco Sirabella"
__copyright__  = ""
__credits__    = "Marco Sirabella"
__license__    = "GPL 3.0"
__version__    = "0.2.0"
__maintainer__ = "Marco Sirabella"
__email__      = "msirael@gmail.com"
__status__     = "Prototype"
__module__     = ""


def selectrand(bm, me, num, expanse):
    import random
    # obj = bpy.context.edit_object
    # me = obj.data
    # bm = bmesh.from_edit_mesh(me)
    # just assume now there is only one selected face
    x = 0
    while x < num:
        for face in [f for f in bm.faces if f.select]:
            selected_face = face
            for edge in selected_face.edges:
                linked = edge.link_faces
                if random.random() > expanse:
                    for face in linked:
                        face.select = True
        x = x + 1
    bmesh.update_edit_mesh(me, True)


def radrange(bm, pointp):
    import numpy
    global points
    # print(pointp)
    points = []
    global points0
    points0 = []
    global points1
    points1 = []
    global points2
    points2 = []
    for face in [f for f in bm.faces if f.select]:
        for vert in face.verts:
            points.append(vert.co)
    for point in points:
        points0.append(point[0])
        points1.append(point[1])
        points2.append(point[2])
    points0 = sorted(points0)
    points1 = sorted(points1)
    points2 = sorted(points2)
    # print(numpy.subtract(point.co[0], points0[len(points0)-1]))
    # print(numpy.subtract(point.co[0], points0[0]))
    # print(numpy.subtract(point.co[1], pointas1[len(points1)-1]))
    # print(numpy.subtract(point.co[1], points1[0]))
    # print(numpy.subtract(point.co[2], points2[len(points2)-1]))
    # print(numpy.subtract(point.co[2], points2[0]))
    y = numpy.mean([
        numpy.absolute([numpy.subtract(pointp.co[0], points0[len(points0) - 1]) - numpy.subtract(pointp.co[0], points0[0])]),
        numpy.absolute([numpy.subtract(pointp.co[1], points1[len(points1) - 1]) - numpy.subtract(pointp.co[1], points1[0])]),
        numpy.absolute([numpy.subtract(pointp.co[2], points2[len(points2) - 1]) - numpy.subtract(pointp.co[2], points2[0])])])
    return y
    # points = []
    # points.append(numpy.std(points0))
    # points.append(numpy.std(points1))
    # points.append(numpy.std(points2))
    # print(numpy.mean(points))


def orgpoints():
    points = []
    pointsx = []
    pointsy = []
    poi
    for face in [f for f in bm.faces if f.select]:
        for vert in face.verts:
            points.append(vert.co)
    for point in points:
        pointsx.append(point[0])
        pointsy.append(point[1])
        pointsz.append(point[2])
    pointsx = sorted(pointsx)
    pointsy = sorted(pointsy)
    pointsz = sorted(pointsz)
    points = [pointsx, pointsy, pointsz]
    return points


def selper(bm):
    perimiter = 0
    for face in [f for f in bm.faces if f.select]:
        for edge in face.edges:
            sfaces = 0
            for lface in edge.link_faces:
                if lface.select:
                    sfaces += 1
            if sfaces == 1:
                perimiter += edge.calc_length()
    return perimiter


def selarea(bm):
    area = 0
    for face in [f for f in bm.faces if f.select]:
        area += face.calc_area()
    return area


def circlyness(bm):
    import math
    circly = (4 * math.pi * selarea(bm)) / (selper(bm) ** 2)
    return circly
