while True:

    current_movies = {'Revengers: Lastplay' : '10:00am',
                  'Christopher Nolan: The Movie: The Game: The Dream' : '12:00pm',
                  'Scatman John, scatting in the stars' : '1:00pm'}

    print("! Don't forget, buy tickets online and get a hotdog and popcorn mega-deal for only £79.99 !")
    print('Movies currently running at our cinema:')
    for key in current_movies:
        print(key)

    movie = input('What movie would you like the showtime for?\n')

    showtime = current_movies.get(movie)
    if showtime == None:
        print('That movie is not playing')
    else:
        print('Here are the showtimes for ' + str(movie) + '.\n' + showtime)


    while True:
        cont = input('Anything else? y/n \n')
        if cont == 'y':
            break
        if cont == 'n':
            break           
        else:
            print('Please answer with y or n.\n')
            continue

    if cont == 'y':
        print("Good choice, buy cinema tickets for movies both showing at the same time and take advantage of our 25% discount!")
        continue
    if cont == 'n':
        print('Thanks for coming!')
        break     
    