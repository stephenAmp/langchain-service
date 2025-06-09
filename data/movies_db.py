#  data would come from a database or a regularly updated file.
# For this example, we'll use a simple list of dictionaries.
# Each dictionary represents a movie with its title, a brief description/plot, genre, and release year.

def get_movie_data():
    """Returns a list of sample movie data."""
    return [
        {
            "title": "Inception",
            "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
            "genre": "Sci-Fi",
            "year": 2010
        },
        {
            "title": "The Matrix",
            "description": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
            "genre": "Sci-Fi",
            "year": 1999
        },
        {
            "title": "Parasite",
            "description": "Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.",
            "genre": "Thriller",
            "year": 2019
        },
        {
            "title": "The Godfather",
            "description": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
            "genre": "Crime",
            "year": 1972
        },
        {
            "title": "Pulp Fiction",
            "description": "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
            "genre": "Crime",
            "year": 1994
        },
        {
            "title": "Forrest Gump",
            "description": "The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood sweetheart.",
            "genre": "Drama",
            "year": 1994
        },
        {
            "title": "The Dark Knight",
            "description": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
            "genre": "Action",
            "year": 2008
        },
        {
            "title": "Interstellar",
            "description": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
            "genre": "Sci-Fi",
            "year": 2014
        },
        {
            "title": "Spirited Away",
            "description": "During her family's move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits, and where humans are changed into beasts.",
            "genre": "Animation",
            "year": 2001
        },
        {
            "title": "The Lion King",
            "description": "A young lion prince is cast out of his pride by his cruel uncle, who claims he killed his father, and must learn the true meaning of responsibility and bravery.",
            "genre": "Animation",
            "year": 1994
        }
    ]

