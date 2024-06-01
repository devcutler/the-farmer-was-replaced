# type: ignore

def tree():
	if (is_even(get_pos_x())):
		if (is_odd(get_pos_y())):
			ensure_ground(Grounds.Turf)
			if (can_harvest()):
				harvest()
			if (get_water() < 0.9):
				use_item(Items.Water_Tank)
			plant(Entities.Tree)
	if (is_odd(get_pos_x())):
		if (is_even(get_pos_y())):
			ensure_ground(Grounds.Turf)
			if (can_harvest()):
				harvest()
			if (get_water() < 0.9):
				use_item(Items.Water_Tank)
			plant(Entities.Tree)