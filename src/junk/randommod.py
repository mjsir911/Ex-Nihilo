import bpy
import bmesh
from mathutils import Vector
from random import random

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

ob = bpy.context.object
me = ob.data

bm = bmesh.new()
bm.from_mesh(me)
faces = bm.faces[:]

for face in faces:
    if random() > 0.9:
        new_faces = bmesh.ops.extrude_discrete_faces(bm, faces=[face])['faces']
        new_face = new_faces[0]
        bmesh.ops.translate(bm, vec=new_face.normal * (1), verts=new_face.verts)

#for v in bm.verts:
#    bmesh.ops.remove_doubles(bm, verts=bm.verts , dist=random())

bm.to_mesh(me)
me.update()

def transout(dist):
    for face in [f for f in bm.faces if f.select]:
            bmesh.ops.translate(bm, vec=face.normal * (dist), verts = face.verts[:])
