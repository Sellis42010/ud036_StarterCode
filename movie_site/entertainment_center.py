import fresh_tomatoes
import media

#connects movie instances to class Movie in the media file to call the init function
equalizer_two = media.Movie ("Equalizer 2", "Retired agent is hunted down by CIA hired assassins",
                             "https://m.media-amazon.com/images/M/MV5BMTU5MDYwMjMzMV5BMl5BanBnXkFtZTgwOTYyMDQzNTM@._V1_UX182_CR0,0,182,268_AL_.jpg",
                            "https://www.youtube.com/watch?v=eAKrgwCnkGM")

fight_club = media.Movie ("Fight Club", "A consumerized middle-aged man starts an underground fighting ring",
                        "https://images-na.ssl-images-amazon.com/images/I/81D%2BKJkO4SL._SL1500_.jpg",
                        "https://www.youtube.com/watch?v=SUXWAEX2jlg")

midnight_in_paris = media.Movie ("Midnight In Paris", "While visiting Paris a Hollywood writer gets transported in time to meet his favorite writers",
                                 "https://images-na.ssl-images-amazon.com/images/I/61uuYEUFw4L._SY450_.jpg",
                                 "https://www.youtube.com/watch?v=U_3gIxrcWK8")

now_you_see_me = media.Movie ("Now You See Me", "A group of magicians steal millions while performing daring feets of magic",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/c/c7/Now_You_See_Me_Poster.jpg/220px-Now_You_See_Me_Poster.jpg",
                              "https://www.youtube.com/watch?v=u_diRgwPCS8")

john_wick = media.Movie ("John Wick", "A highly trained assassin seeks the individuals who killed his dog",
                         "https://vignette.wikia.nocookie.net/john-wick8561/images/2/29/John_Wick_Poster_003.jpg/revision/latest?cb=20161128160703",
                         "https://www.youtube.com/watch?v=C0BMx-qxsP4")

bridesmaid = media.Movie ("Bridesmaid", "A friend struggles to maintain her sanity, love life, and a frienship while her best friend is getting married",
                          "https://www.movieartarena.com/imgs/bridesmaidsi.jpg",
                          "https://www.youtube.com/watch?v=FNppLrmdyug")
    


#Create a list variable and fill it with the list of movie instances
movies = [equalizer_two, fight_club, midnight_in_paris, now_you_see_me, john_wick, bridesmaid]
#Use fresh tomatoe to use open movies function to import list of movies and ouput website that shows movie instances given
fresh_tomatoes.open_movies_page(movies)
