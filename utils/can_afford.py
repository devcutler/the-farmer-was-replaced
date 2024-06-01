# type: ignore

def can_afford(locked):
	affordable = True
	cost = get_cost(locked)
	for c in cost:
		item = c[0]
		amount = c[1]
		if (num_items(item) < amount):
			affordable = False
	return affordable