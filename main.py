# type: ignore

def main():
	# trade(Items.Empty_Tank, 5000)
	clear()
	enabled_resources = [Items.Hay, Items.Wood, Items.Carrot, Items.Pumpkin, Items.Power, Items.Gold]
	enabled_unlocks = [Unlocks.Speed, Unlocks.Expand]
	ground = get_ground_type()
	product = Items.Hay
	while True:
		for locked in enabled_unlocks:
			while can_afford(locked):
				unlock(locked)
		reset_position()
		if (product != least_resource(enabled_resources)):
			product = least_resource(enabled_resources)
			if (ground != map_product_to_ground(product)):
				ground = map_product_to_ground(product)
			ensure_ground_over_field(ground)
		for i in range(5):
			run_product(product)