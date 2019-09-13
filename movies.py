#!/usr/bin/env python3
import json

INITIAL_BALANCE = 100

def read_movies(filename):
	try:
		with open(filename) as file:
			movies = json.load(file)
			for genre in movies: movies[genre].sort(key=lambda movie: movie["title"].strip().casefold())
			return dict(sorted(movies.items()))
	except FileNotFoundError: # treats no-file as empty json data, but invalid json is still considered an error
		return {}

def print_movie(movie):
	field = "watched" if "watched" in movie else "cost"
	print(f'\ntitle: "{movie["title"]}",\nrating: {movie["rating"]},\n{field}: {movie[field]}')

def print_movies(movies):
	for genre in movies:
		print("\n\nGenre:", genre.title())
		for movie in movies[genre]:
			print_movie(movie)

def cost(movies):
	total = 0
	for genre in movies:
		for movie in movies[genre]:
			total += movie["cost"]
	return total

def find_movie(title, movies):
	title = title.strip().casefold()
	for genre in movies:
		for movie in movies[genre]:
			if title == movie["title"].strip().casefold():
				movie["watched"] = genre # hack to return genre from function - used by purchase_movie()
				return movie

def purchase_movie(title):
	movies = read_movies("my_movies.json")
	if find_movie(title, movies): return print("You have already purchased this movie")
	movie = find_movie(title, read_movies("available_movies.json"))
	if not movie: return print("That movie is not available")
	if movie["cost"] + cost(movies) > INITIAL_BALANCE: return print("Not enough credit remaining to purchase this movie")
	genre = movie["watched"] # hack used by find_movie() to return genre - refactor if decoupling is needed
	movie["watched"] = False
	if genre not in movies: movies[genre] = []
	movies[genre].append(movie)
	with open("my_movies.json", "w") as file: json.dump(movies, file, indent="\t")
	print("Purchase successful")
	return movie

def list_from_genre(movies):
	i = 0
	for genre in movies:
		i += 1
		print(f"{i}.", genre.title())
	genre = input("Select a genre: ").strip().casefold()
	try:
		genre = int(genre) # throws ValueError on non-integer input
		if 1 <= genre <= len(movies):
			for movie in list(movies.values())[genre-1]: print_movie(movie)
		else:
			print("Invalid genre index")
	except ValueError:
		if genre in movies:
			for movie in movies[genre]: print_movie(movie)
		else:
			print("Invalid genre name")

def search_movies(key):
	if len(key) < 3: return print("Must enter at least 3 characters")
	key = key.casefold()
	matches = {}
	for filename in ["available_movies.json", "my_movies.json"]:
		movies = read_movies(filename)
		for genre in movies:
			for movie in movies[genre]:
				title = movie["title"].strip().casefold()
				if key in title:
					movie["genre"] = genre
					matches[title] = movie
	if not matches: return print(f'No movies found matching "{key}"')
	i = 0
	for match in matches.values():
		i += 1
		print(f'{i}.\t${match["cost"]}\t{match["rating"]}/10\t{match["genre"]}\t"{match["title"]}"\t{match["watched"] if "watched" in match else ""}')
	movie = input("Select an option to purchase: ").strip().casefold()
	try:
		movie = int(movie) # throws ValueError on non-integer input
		return purchase_movie(list(matches.keys())[movie-1]) if 1 <= movie <= len(matches) else print("Invalid movie index")
	except ValueError:
		return purchase_movie(movie) if movie in matches else print("Invalid movie title")

selection = 1
while 1 <= selection <= 6:
	try: selection = int(input("""
1. List all available movies
2. Show my movies
3. Purchase a movie
4. Show credit balance
5. List all available movies in a specific genre
6. Search for a movie
Select an action: """))
	except ValueError: selection = 0
	if   selection == 1: print_movies(read_movies("available_movies.json"))
	elif selection == 2: print_movies(read_movies("my_movies.json"))
	elif selection == 3: purchase_movie(input("Enter title of movie to purchase: "))
	elif selection == 4: print("Your current balance is", INITIAL_BALANCE - cost(read_movies("my_movies.json")), "credits")
	elif selection == 5: list_from_genre(read_movies("available_movies.json"))
	elif selection == 6: search_movies(input("Enter a search term: "))