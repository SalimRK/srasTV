from tmdbv3api import TMDb, Movie, TV
import apiKeys
import urllib
from PIL import Image
import io

tmdb = TMDb()
tmdb.api_key = apiKeys.tmdb_api

movie = Movie()
tv = TV()


def get_popular_movie():
    results = movie.popular()
    return results


def get_movie_info(title_id):
    results = movie.details(title_id)
    return results


def search_movie(search_for):
    results = movie.search(search_for)
    return results


def get_popular_tv():
    results = tv.popular()
    return results


def get_tv_info(title_id):
    results = tv.details(title_id)
    return results


def search_tv(search_for):
    results = tv.search(search_for)
    return results


def get_poster(img_path):
    # Download and display the poster
    try:
        with urllib.request.urlopen("https://www.themoviedb.org/t/p/w600_and_h900_bestv2" + img_path) as u:
            raw_data = u.read()
        image = Image.open(io.BytesIO(raw_data))
        return image
    except TypeError:
        image = Image.open("Assets/no poster.png")
        return image
