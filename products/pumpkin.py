# type: ignore

def pumpkin():
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			if (num_items(Items.Pumpkin_Seed) == 0):
				trade(Items.Pumpkin_Seed)
			plant(Entities.Pumpkin)
			while not can_harvest():
				if (get_entity_type() == None):
					if (num_items(Items.Pumpkin_Seed) == 0):
						trade(Items.Pumpkin_Seed)
					plant(Entities.Pumpkin)
				while (get_water() < 0.9):
					use_item(Items.Water_Tank)
				if (num_items(Items.Fertilizer) == 0):
					trade(Items.Fertilizer, 100)
				use_item(Items.Fertilizer)
			move(North)
		move(East)
	harvest()