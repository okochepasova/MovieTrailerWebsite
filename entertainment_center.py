import media
import fresh_tomatoes

avatar = media.Movie(
    "Avatar", "A marine on an alien planet.",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

big_hero_6 = media.Movie(
    "Big Hero 6",
    "The special bond that develops between plus-sized inflatable robot " +
    "Baymax, and prodigy Hiro Hamada, who team up with a group of friends " +
    "to form a band of high-tech heroes.",
    "https://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29" +
    "_poster.jpg",
    "https://www.youtube.com/watch?v=z3biFxZIJOQ")

interstellar = media.Movie(
    "Interstellar",
    "A team of explorers travel through a wormhole in space in an attempt " +
    "to ensure humanity's survival",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5" +
    "BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_UY1200_CR69,0,630,1200_AL_.jpg",
    "https://www.youtube.com/watch?v=0vxOhd4qlnA")

lio_and_stitch = media.Movie(
    "Lilo & Stitch", "A tale of a young girl's close encounter with the " +
    "galaxy's most wanted extraterrestrial",
    "http://www.gstatic.com/tv/thumb/movieposters/29095/p29095_p_v8_aa.jpg",
    "https://www.youtube.com/watch?v=5vMEOvZ1ODk")

monsters_inc = media.Movie(
    "Monsters, Inc.",
    "Two monsters must return a human girl back to her world",
    "https://upload.wikimedia.org/wikipedia/en/6/63/Monsters_Inc.JPG",
    "https://www.youtube.com/watch?v=8IBNZ6O2kMk")

ratatouille = media.Movie(
    "Ratatouille", "A rat is a chef in Paris",
    "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk")

the_cat_returns = media.Movie(
    "The Cat Returns", "A human girl gets " +
    "involved with the cat kingdom, and It's up to the Cat Bureau to help her",
    "http://vignette3.wikia.nocookie.net/voiceacting/images/c/c8/The_Cat" +
    "_Returns_DVD_Cover.jpg/revision/latest?cb=20121216105125",
    "https://www.youtube.com/watch?v=Gp-H_YOcYTM")

toy_story = media.Movie(
    "Toy Story", "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

zootopia = media.Movie(
    "Zootopia", "A story about " +
    "an unlikely partnership between a rabbit police officer and a red " +
    "fox con artist as they uncover a conspiracy in a mammalian metropolis",
    "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
    "https://www.youtube.com/watch?v=jWM0ct-OLsM")

# Homework Results: http://screencast.com/t/2LkIPaq7UL

"""============================================================================
                            START RUNTIME CODE
============================================================================"""


def main():
    movies = [avatar, big_hero_6, interstellar, lio_and_stitch, monsters_inc,
              ratatouille, the_cat_returns, toy_story, zootopia]
    fresh_tomatoes.open_movies_page(movies)

    # print(media.Video.__doc__)

if __name__ == '__main__':
    main()
