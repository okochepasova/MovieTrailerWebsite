import webbrowser


class Rating():
    """A class that stores a review.

Attributes:
    stars (int): The number of stars this review has. value between 0-5.
    words (str): Any comments this review has.
    """
    # Constructor
    def __init__(self, stars, words):
        self.stars = stars
        self.words = words

    # Methods
    def __repr__(self): return ("("+str(self.stars)+", '"+self.words+"')")

    def __str__(self): return (str(self.stars)+"* "+self.words)


class Video():
    """A class that stores the basics any movie or series will have.

Attributes:
    title (str): The Title of the instance
    poster_image_url (str): The cover picture of the instance.
    trailer_youtube_url (str): A url to the trailer of this instance on youtube
    ratings (list): A list of all ratings this instance will have.
    """
    # Construct
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.ratings = []

    # Methods
    def add_rating(self, stars, words):
        if ((type(stars) is int) and (type(words) is str)):
            if stars < 0:
                stars = 0
            elif stars > 5:
                stars = 5
            self.ratings.append(Rating(stars, words))
        else:
            print("wrong inputs: stars= "+stars+", words= '"+words+"'")

    def show_ratings(self):
        total = 0.0
        # rates = []
        if len(self.ratings) > 0:
            for r in self.ratings:
                total = total+r.stars
                # if(r.words != ""): rates.append(r)
            total = total / len(self.ratings)
        print(str(total)+"/5.0")
        # print(rates)
        print(self.ratings)


class Movie(Video):
    """This class provides a way to store movie related information

Attributes:
    storyline (str): A short summary of the movie.
    """
    # Class Variables
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # Constructor
    def __init__(self, movie_title, storyline, poster_image,
                 trailer_youtube):
        Video.__init__(self, movie_title, poster_image, trailer_youtube)
        self.storyline = storyline

    # Methods
    def show_trailer(self): webbrowser.open(self.trailer_youtube_url)

"""============================================================================
                            START RUNTIME CODE
============================================================================"""


def trial():
    # Main useage
    x = ['a']
    print("x = "+str(x))
    x.extend(["lasy", "string"])
    print("x = "+str(x))
    x.append("bye-bye")
    print("x = "+str(x))
    print("")

    # Other usage
    y = ['a']
    print("y = "+str(y))
    y.append(["lasy", "string"])
    print("y = "+str(y))
    y.extend("bye-bye")
    print("y = "+str(y))


def main():
    m = Movie('a', 'b', 'c', 'd')

    m.add_rating(5, "This is Wonderfull!!!")
    m.add_rating(3, "Meh. I've seen better.")
    m.add_rating(0, '')
    m.add_rating(1, "Horibble! Aufull! Terrible!")
    m.add_rating(4, "")

    m.show_ratings()
    print("")

    print(m.ratings)
    print(Rating(5, "This is Wonderfull!!!"))
    # trial()

if __name__ == '__main__':
    main()
