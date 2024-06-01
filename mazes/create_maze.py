# type: ignore

def create_maze():
	clear()
	reset_position()
	harvest()
	plant(Entities.Bush)
	while get_entity_type() != Entities.Hedge:
		if (get_entity_type() != Entities.Bush):
			plant(Entities.Bush)
		if (num_items(Items.Fertilizer) == 0):
			trade(Items.Fertilizer)
		use_item(Items.Fertilizer)
		if (get_entity_type() == Entities.Treasure):
			harvest()
			return True