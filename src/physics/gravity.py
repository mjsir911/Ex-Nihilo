import bge
import math

G = 1.0 	# gravitational constant
D = 3 		# Number of spatial dimensions

cont = bge.logic.getCurrentController()
own = cont.owner

# If the owner has the hasGravity property set to true
if own.get('hasGravity'):
	scene = bge.logic.getCurrentScene()

	# Set totalForce to a zero vector
	totalForce = [0 for i in range(D)]

	# For every object in the scene that has the hasGravity property set to true
	for obj in scene.objects if obj.get('hasGravity'):
		# displacement is vector difference between worldPosition of obj and own
		displacement = [\
			obj.worldPosition[i] - own.worldPosition[i]\ 
			for i in range(D)\
		]

		# yields the sum of the square of every displacement
		distSquared = sum( map( 
			lambda x: pow(x, 2),
			displacement
		))
		dist = math.sqrt(distSquared)

		if distSquared != 0.0:
			Fg = G * own.mass * obj.mass / distSquared
		else:
			continue # We can skip the rest of this loop

		# The force acting on own due to obj is negative 
		force = map(
			lambda x: - x * Fg / dist,
			displacement
		)

		totalForce += force
	own.applyForce(totalForce, 0)