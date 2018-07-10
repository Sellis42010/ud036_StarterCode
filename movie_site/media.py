import webbrowser


class Movie():
#Store arguments for movies with self being the instance created in enterainment center file 
    def __init__(self, title, storyline, poster, trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

#Create instance and store the arg self to open a webbrowser with the movie instances trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
