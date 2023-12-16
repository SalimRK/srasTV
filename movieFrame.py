import customtkinter as ctk
import titles
from tmdbv3api import TMDb, Movie
import apiKeys

tmdb = TMDb()
tmdb.api_key = apiKeys.tmdb_api

movie = Movie()
popular = movie.popular()


class MovieFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        i = 0
        j = 0
        for p in popular:
            self.my_frame = titles.TitleFrame(master=self, title_id=p.id, title=p.title, img_path=p.poster_path)
            self.my_frame.grid(row=i, column=j, padx=10, pady=10)
            j += 1
            if j % 3 == 0:
                i += 1
                j = 0
