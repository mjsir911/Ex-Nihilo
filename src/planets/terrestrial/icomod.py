import bpy
import bmesh
import random

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
    

def edit_in(sname=''):
    global bm
    global me
    global obj
    global name
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
    else:
        pass
#    for v in bm.verts:
#        v.co.x += 1.0

def edit_out():
    scene = bpy.context.scene
    bpy.ops.object.mode_set(mode='OBJECT')
    scene.objects.active = None
    
def edit_tog(name):
    global bm
    global me
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

def materialize(name, bm):
    scene = bpy.context.scene
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    me.update()
    obj = bpy.data.objects.new(name, me)
    scene.objects.link(obj)
    
def metagen(name, coords):
    core = bpy.data.objects.new(name, None)
    scene = bpy.context.scene
    scene.objects.link(core)
    scene.update()
    bpy.ops.curve.primitive_bezier_circle_add(location = (0,0,0), radius = (2), rotation = (math.radians(0), math.radians(0), math.radians(0)))
    core.location = coords
    return core, pole, orbit
    
    
def getbm(name):
    global bm
    mode = bpy.context.mode
    edit_in(name)
    return bm

def transout(dist):
    for face in [f for f in bm.faces if f.select]:
            bmesh.ops.translate(bm, vec=face.normal * (dist), verts = face.verts[:])

def autogen(name, size = 6):
    materialize(name, ico_create(size, 1))
    edit_in(name)
    
def selectrand(num, expanse):
    #obj = bpy.context.edit_object
    #me = obj.data
    #bm = bmesh.from_edit_mesh(me)
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
        x = x+1
    bmesh.update_edit_mesh(me, True)

def continent_gen(expanse = 1/6, size = 5):
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
        selectrand(random.random()*size * 2, expanse)
        centerpoint = center.verts[random.randrange(len(center.verts[:]))]
        print(radrange(centerpoint))
        #print(y)
        if radrange(centerpoint) > 0.4 and circlyness() < expanse * 1.5:
        #if len([f for f in bm.faces if f.select]) > size* 5:
        #print(centercoords)
            bpy.ops.mesh.separate(type='SELECTED')
            print('good')
            #x = x+1
            #x+=1
            if x:
                break
        else:
            bpy.ops.mesh.select_all(action = 'DESELECT')
            print('too bad')
        bmesh.update_edit_mesh(me, True)
        me.update()
    #print(len(bm.faces))
    bpy.ops.mesh.separate(type='LOOSE')
    c_after = []
    c_after.append(bpy.data.objects[:])
    continents = [item for item in c_after[0] if item not in c_before[0]]
    continents.append(bpy.data.objects[obj.name])
    edit_out()
    erode(continents, size)
    for cont in continents:
        obj = cont
        #edit_in(cont.name)
        #move each plate out 0.02-- replaced by smooth
        #for face in bm.faces:
        #    face.select = True
        #transout(0.02)
        
        #Smooth the plates(shrink a bit)
        obj.modifiers.new('Smooth', 'SMOOTH')
        obj.modifiers['Smooth'].factor = 2
        obj.modifiers['Smooth'].iterations = 2
        
        #Porbably add solidify with th* of 0.2 and cla of 0
        obj.modifiers.new('Solidify', 'SOLIDIFY')
        obj.modifiers['Solidify'].thickness = 0.05
        
        #edit_out()
        
        #recalc centerpoint to center of mass
        obj.select = True
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
    return continents
    
def continent_drift(age):
    """for cont in continents:
        obj = bpy.data.objects[cont.name]
        obj.scale[0] = random.randrange(75, 125, 5) / 100
        obj.scale[1] = random.randrange(75, 125, 5) / 100
        obj.scale[2] = random.randrange(75, 125, 5) / 100"""

def radrange(pointp):
    import numpy
    global points
    #print(pointp)
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
    #print(numpy.subtract(point.co[0], points0[len(points0)-1]))
    #print(numpy.subtract(point.co[0], points0[0]))
    #print(numpy.subtract(point.co[1], pointas1[len(points1)-1]))
    #print(numpy.subtract(point.co[1], points1[0]))    
    #print(numpy.subtract(point.co[2], points2[len(points2)-1]))
    #print(numpy.subtract(point.co[2], points2[0]))
    y = numpy.mean([
    numpy.absolute([numpy.subtract(pointp.co[0], points0[len(points0)-1]) - numpy.subtract(pointp.co[0], points0[0])]),
    numpy.absolute([numpy.subtract(pointp.co[1], points1[len(points1)-1]) - numpy.subtract(pointp.co[1], points1[0])]),
    numpy.absolute([numpy.subtract(pointp.co[2], points2[len(points2)-1]) - numpy.subtract(pointp.co[2], points2[0])])])
    return y
    #points = []
    #points.append(numpy.std(points0))
    #points.append(numpy.std(points1))
    #points.append(numpy.std(points2))
    #print(numpy.mean(points))
    
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

def selper():
    perimiter = 0
    for face in [f for f in bm.faces if f.select]:
        for edge in face.edges:
            sfaces = 0
            for lface in edge.link_faces:
                if lface.select == True:
                    sfaces += 1
            if sfaces == 1:
                perimiter+= edge.calc_length()
    return perimiter

def selarea():
    area = 0
    for face in [f for f in bm.faces if f.select]:
        area +=face.calc_area()
    return area

def circlyness():
    import math
    circly = (4 * math.pi * selarea()) / (selper() ** 2)
    return circly

def erode(list, size):
    for item in bpy.context.selectable_objects:  
        item.select = False 
    for conts in list:
        if len(conts.data.vertices) < size:
            conts.select = True
            list.remove(conts)
            bpy.ops.object.delete()
            #print(conts.name)
            
def mountaingen():
    pass
    #build modifier to randomly get faces from sphere
    
def planet_gen(
    seed = '',
    planet_name = 'planet',
    planet_resolution = 6,
    planet_size = 1,
    planet_age = None,
    continent_roundness = 1/6,
    continent_size = 5
    ):
    import random
    if seed:
        random.seed(seed)
    if planet_age == None:
        planet_age = random.randrange(50000, 10000000)
    materialize('{0}_tectplates'.format(planet_name), ico_create(planet_resolution, planet_size))
    edit_in('{0}_tectplates'.format(planet_name))
    continent_gen(expanse = continent_roundness, size = continent_size)
    continent_drift(planet_age)
        