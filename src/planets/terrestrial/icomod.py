import bpy
import bmesh
import random
import os
import sys
#try:
#    from tectonics import create
#except ImportError:
#    from create import generate_tectonic_plates as tectgen
#such a cheaty way to do it
sys.path.append(os.path.abspath(os.path.join(os.path.dirname('./tectonics'))))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname('../../misc'))))
#from .tectonics.create import generate_tectonic_plates

from tcreate import generate_tectonic_plates as tectgen
from edits import edit_in, edit_out
from shapes import ico_create, materialize
from bodies import metagen    
            
def mountaingen():
    pass
    #build modifier to randomly get faces from sphere
    
def planet_gen(
    seed = '',
    start_revolution = None,
    orbital_distortion = 250,
    planet_name = 'planet',
    tectonic_resolution = 6,
    tectonic_size = 0.75,
    planet_age = None,
    continent_roundness = 1/6,
    continent_size = 5
    ):
    import random
    if seed:
        random.seed(seed)
    if planet_age is None:
        planet_age = random.randrange(50000, 10000000)
    if start_revolution is None:
        start_revolution = random.randint(0, 99)
    core, orbit = metagen(planet_name, start_revolution, orbital_distortion)
    materialize('{0}_tectplates'.format(planet_name), ico_create(tectonic_resolution, tectonic_size))
    bm, me= edit_in('{0}_tectplates'.format(planet_name))
    print(bm)
    continents = tectgen(bm, me, expanse = continent_roundness, size = continent_size)
    continent_drift(planet_age)
    group(continents)