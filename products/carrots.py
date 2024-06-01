# type: ignore

def carrots():
	if (can_harvest()):
		harvest()
	if (get_entity_type() == None):
		plant(Entities.Carrots)