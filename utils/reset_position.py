# type: ignore

def reset_position():
	while get_pos_y() != 0:
		move(North)
	while get_pos_x() != 0:
		move(East)