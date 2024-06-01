# type: ignore

def least_resource(resources):
	least = resources[0]
	for item in resources:
		if (num_items(item) < num_items(least)):
			least = item
	return least