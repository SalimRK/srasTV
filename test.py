from tmdbv3api import TMDb, Movie

tmdb_api = '7efc97b2176e7c82962cab44ea126623'
if __name__ == '__main__':
    tmdb = TMDb()
    movie = Movie()
    tmdb.api_key = tmdb_api
    popular = movie.popular()

    for p in popular:
        print(p.id)
        print(p.title)
        print(p.poster_path)
