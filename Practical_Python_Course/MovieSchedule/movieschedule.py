current_movies = {'Revengers: Lastplay' : '10:00am',
                  'Christopher Nolan: The Movie: The Game: The Dream' : '12:00pm',
                  'Scatman John, scatting in the stars' : '1:00pm'}

print("! Don't forget, buy tickets online and get a a hotdog and popcorn mega-deal for only £79.99 !")
print('Movies currently running at our cinema:')
for key in current_movies:
    print(key)

movie = input('What movie would you like the showtime for?\n')

print('Here are the showtimes for ' + str(movie) + ' .\n' + current_movies.get(movie))



