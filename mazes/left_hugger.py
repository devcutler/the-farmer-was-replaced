# type: ignore

def left_hugger():
	i = 0
	while get_entity_type() != Entities.Treasure:
		if (maze_move(i)):
			i = (i - 1) % 4
		else:
			i = (i + 1) % 4
	harvest()