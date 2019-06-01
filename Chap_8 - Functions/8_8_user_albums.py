'''
Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop

'''


def make_album():
	
	print("(Enter q to exit program at anywhere anytime.)\n")
	while True:
		artist_name = input("Please enter artist name: ")
		if artist_name == 'q':
			break
			
		album_title = input("Now enter album title: ")
		if album_title == 'q':
			break
			
		if artist_name == '' or album_title == '':
			print("No Empty values are accepted!\n")
			
		else:
			album = {'artist name'.title(): artist_name.title(), 'album title'.title(): album_title.title()}
			print(album)
			print("\n")

make_album()
		
		
