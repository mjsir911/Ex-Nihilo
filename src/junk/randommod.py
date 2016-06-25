import bpy
import bmesh
from mathutils import Vector
from random import random

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