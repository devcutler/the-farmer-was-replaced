# type: ignore

def ensure_ground(ground):
	if (ground == Grounds.Turf):
		if (get_ground_type() != Grounds.Turf):
			till()
	if (ground == Grounds.Soil):
		if (get_ground_type() != Grounds.Soil):
			till()