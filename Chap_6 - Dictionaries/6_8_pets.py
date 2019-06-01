
tuna = {
	'kind': 'fish',
	'owner': 'huzaifa baloch'
	}

maverick = {
	'kind': 'parrot',
	'owner': 'logan paul',
	}
	
pets = [tuna, maverick]

for each_pet in pets:
	for key, value in each_pet.items():
		print("The " + key.title() + " of pet is " + value.title())
		
