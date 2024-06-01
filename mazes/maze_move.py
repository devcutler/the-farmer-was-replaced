# type: ignore

def maze_move(i):
	directions = [North, East, South, West]
	direction = directions[i % 4]
	x = get_pos_x()
	y = get_pos_y()
	move(direction)
	return not (x == get_pos_x() and y == get_pos_y())