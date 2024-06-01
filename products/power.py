# type: ignore

def power():
	reset_position()
	consensus = get_world_size() * get_world_size()
	current = 0
	current = 0
	while current != consensus:
		while get_active_power() < 25:
			use_item(Items.Power)
		current = 0
		for x in range(get_world_size()):
			for y in range(get_world_size()):
				while get_water() < 0.9 and num_items(Items.Water_Tank) > 0:
					use_item(Items.Water_Tank)
				if (get_entity_type() != Entities.Sunflower):
					if (num_items(Items.Sunflower_Seed) == 0):
						trade(Items.Sunflower_Seed)
					plant(Entities.Sunflower)
				if (measure() == 15):
					if (can_harvest()):
						harvest()
						if (num_items(Items.Sunflower_Seed) == 0):
							trade(Items.Sunflower_Seed)
						plant(Entities.Sunflower)
				else:
					current += 1
				move(North)
			move(East)
	harvest()