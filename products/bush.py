# type: ignore

def bush():
	ensure_ground(Grounds.Turf)
	if (can_harvest()):
		harvest()
	plant(Entities.Bush)
	pass