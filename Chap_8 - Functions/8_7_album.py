
# Example of dictionary in functions and optional parameter in function
# ---------------------------------------------------------------------


'''
Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Add an optional parameter to make_album() that allows you to store the
number of tracks on an album. If the calling line includes a value for the number
of tracks, add that value to the album’s dictionary. Make at least one new
function call that includes the number of tracks on an album.
'''




def make_album(artist_name, album_title, no_of_tracks = 0):
	if no_of_tracks:
		album = {'artist name'.title(): artist_name.title(), 'album title'.title(): album_title.title(), 'tracks': str(no_of_tracks)}
	else:
		album = {'artist name'.title(): artist_name.title(), 'album title'.title(): album_title.title()}
	return album


print(make_album('linkin park', 'a new sunshine'))
print(make_album('two pilots', 'thousand miles'))
print(make_album('shakira', 'waka waka'))
print("\n\n")

# Function that contain optioanl argument 
print(make_album('blake shelton', 'sangria', 4))
print(make_album('pitbull', 'international', 12))
