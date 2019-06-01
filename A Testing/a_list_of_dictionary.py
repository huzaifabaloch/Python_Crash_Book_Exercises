# NESTING
# A LIST OF DICTIONARIES 

#-----------------------------------------------

# a dictionary objects that contain different kinds of information of an alien
alien_0 = {'color': 'green', 'points': '5', 'speed': 'low'}
alien_1 = {'color': 'green', 'points': '5', 'speed': 'low'}
alien_2 = {'color': 'green', 'points': '5', 'speed': 'low'}

aliens = [alien_0, alien_1, alien_2]


# ------------------------------------
# an easy way to do

# a list that will contain a number of aliens of same characteristics
aliens = []

# a for loop that will generate 30 aliens objects of same characteristics
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': '5', 'speed': 'low'}
	aliens.append(new_alien)
	

for each in aliens[:15]:
	print(each)
	
	
print("\nThe total aliens generated : " + str(len(aliens)))
 

# to modify some aliens as game progresses

for each_alien in aliens[:5]:
	if each_alien['color'] == 'green':
		each_alien['color'] = 'yellow'
		each_alien['points'] = 10
		each_alien['speed'] = 'medium'


for each_alien in aliens[:15]:
	print(each_alien)
