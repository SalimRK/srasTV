import customtkinter as ctk
import titles
from tmdbv3api import TMDb, TV

tmdb_api = '7efc97b2176e7c82962cab44ea126623'
tmdb = TMDb()
tmdb.api_key = tmdb_api

tv = TV()
popular = tv.popular()


class SeriesFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        i = 0
        j = 0
        for p in popular:
            self.my_frame = titles.TitleFrame(master=self, title_id=p.id, title=p.name, img_path=p.poster_path)
            self.my_frame.grid(row=i, column=j, padx=10, pady=10)
            j += 1
            if j % 3 == 0:
                i += 1
                j = 0
