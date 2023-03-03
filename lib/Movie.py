class Movie:

    all = []
    
    def __init__(self, title):
        self.title = title
        
        self.reviews = []
        self.reviewers = []
    

    # title property
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title

            Movie.all.append(self)
        else:
            print("Title must be a non-empty string")

            raise Exception("Title must be a non-empty string")
        
    
    def average_rating(self):
        total = 0
        for review in self.reviews:
            total += review.rating
        
        average = total / len(self.reviews)

        return average
        

    @classmethod
    def highest_rated(cls):
        print(cls.all)

