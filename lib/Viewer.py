class Viewer:
    
    def __init__(self, username):
        self.username = username
        
        #made empty list arrays for reviews and viewers
        self.reviewed_movies = []
        self.viewers = []
        self.reviews = []

        # self.reviewed_movie()
        # self.rate_movie()

    # username property goes here!
    @property
    def username(self):
        return self._username 
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username) >= 6 and len(username) <= 16:
            self._username = username
        else:
            raise Exception("Username must be between 6 and 16 characters long")


    def reviewed_movie(self, movie):
        if movie in self.reviewed_movies:
            return True
        else:
            return False

    def rate_movie(self, movie, rating):
        from review import Review
        Review(self, movie, rating)