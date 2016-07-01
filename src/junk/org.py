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


def getbm(name):
    global bm
    mode = bpy.context.mode
    edit_in(name)
    return bm
