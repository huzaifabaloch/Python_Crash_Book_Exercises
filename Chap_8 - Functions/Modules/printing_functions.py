

def make_car(manufacturer, model, **other_info):
	
	car_profile = {}
	car_profile['manufacturer'.title()] = manufacturer.title()
	car_profile['model'.title()] = model.title()
	
	for key, value in other_info.items():
		if type(value) != int and type(value) != bool:
			car_profile[key.title()] = value.title()
		else:
			car_profile[key.title()] = value
	
	return car_profile
