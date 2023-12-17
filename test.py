from tmdbv3api import TMDb, Movie, TV
import apiKeys

# Replace 'your_api_key' with your actual TMDb API key
tmdb = TMDb()
tmdb.api_key = apiKeys.tmdb_api

# Example: Get information about a movie or TV series by ID
item_id = 1403  # Replace with the actual ID of the movie or TV series you want to check

# Initialize movie and TV objects
movie = Movie()
tv = TV()

try:
    movie_details = movie.details(item_id)
    print(movie_details)
    print(f"Item {item_id} is a movie. Title: {movie_details.title}")
except:
    # If it's not a movie, it may be a TV series
    try:
        tv_details = tv.details(item_id)
        print(tv_details)
        print(f"Item {item_id} is a TV series. Title: {tv_details.name}")
    except Exception as e:
        print(f"Error: {e}")
        print(f"Item {item_id} is neither a movie nor a TV series.")
