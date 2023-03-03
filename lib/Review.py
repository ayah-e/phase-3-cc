from viewer import Viewer
from movie import Movie


class Review:
    
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating
    
        self.add_review_to_movie()
        self.add_review_to_viewer()
        self.add_movie_to_viewer()
        self.add_viewer_to_movie()

    # rating property goes here!
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating):
        if isinstance(rating, int) and 1 <= rating <= 5:
            self._rating = rating
        else:
            print("Rating must be an integer between 1 and 5")

            raise Exception("Rating must be an integer between 1 and 5")

    # viewer property goes here!
    @property
    def viewer(self):
        return self._viewer
    
    @viewer.setter
    def viewer(self, viewer):
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else:
            print("Viewer must be an instance of Viewer")

            raise Exception("Viewer must be an instance of Viewer")
        
    # movie property goes here!
    @property
    def movie(self):
        return self._movie
    
    @movie.setter
    def movie(self, movie):
        if isinstance(movie, Movie):
            self._movie = movie
        else:
            print("Movie must be an instance of Movie")

            raise Exception("Movie must be an instance of Movie")
    
    def add_review_to_movie(self):
        self._movie.reviews.append(self)

    
    def add_movie_to_viewer(self):
        if self._movie not in self._viewer.reviewed_movies:
            self._viewer.reviewed_movies.append(self._movie)
    
    def add_review_to_viewer(self):
        self._viewer.reviews.append(self)
    
    def add_viewer_to_movie(self):
        if self._viewer not in self._movie.reviewers:
            self._movie.reviewers.append(self._viewer)
    

    


