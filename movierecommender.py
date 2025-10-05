
class Movie:
    def __init__(self, title, genres):
        self.title = title
        self.genres = genres

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Genres: {', '.join(self.genres)}")
        print("-" * 30)


movie_database = [
    Movie("Saaho", ["Action", "Sci-Fi"]),
    Movie("Bahubali", ["Action", "Drama"]),
    Movie("little hearts", ["Romance", "Drama"]),
    Movie("Interstellar", ["Sci-Fi", "Drama"]),
    Movie("Avengers: Endgame", ["Action", "Adventure"])
]


user_genre = input("Enter a genre you like: ").strip().title()


recommendations = [movie for movie in movie_database if user_genre in movie.genres]


if recommendations:
    print("\nMovies you might like:")
    for movie in recommendations:
        movie.display_info()
else:
    print("Sorry, no movies found in this genre.")
