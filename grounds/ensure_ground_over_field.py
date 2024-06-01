# type: ignore

def ensure_ground_over_field(ground):
	if (ground == Grounds.Turf):
		clear()
		return ground
	for x in range(get_world_size()):
			for y in range(get_world_size()):
				harvest()
				ensure_ground(ground)
				move(North)
			move(East)