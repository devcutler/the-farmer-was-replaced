# type: ignore

def run_product(product):
	if (product == Items.Carrot):
		if (num_items(Items.Carrot_Seed) < get_world_size() * get_world_size()): 
			trade(Items.Carrot_Seed, get_world_size() * get_world_size())
		for x in range(get_world_size()):
			for y in range(get_world_size()):
				while (get_active_power() < 15):
					use_item(Items.Power)
				while (get_water() < 0.5):
					use_item(Items.Water_Tank)
				carrots()
				move(North)
			move(East)
	elif (product == Items.Pumpkin):
		pumpkin()
	elif (product == Items.Wood):
		for x in range(get_world_size()):
			for y in range(get_world_size()):
				tree()
				move(North)
			move(East)
	elif (product == Items.Hay):
		for x in range(get_world_size()):
			for y in range(get_world_size()):
				hay()
				move(North)
			move(East)
	elif (product == Items.Power):
		power()
	elif (product == Items.Gold):
		gold()