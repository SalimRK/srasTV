# display the popular tv series

import customtkinter as ctk
import titles
from tmdbv3api import TMDb, TV
import apiKeys

# initialize TDMb
tmdb = TMDb()
tmdb.api_key = apiKeys.tmdb_api

# initialize tv functions
tv = TV()
popular = tv.popular()


class SeriesFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # display the titles in 3 columns, x rows patterns
        i = 0
        j = 0
        for p in popular:
            # create title object for each show
            self.my_frame = titles.TitleFrame(master=self, title_id=p.id, title=p.name, img_path=p.poster_path)
            self.my_frame.grid(row=i, column=j, padx=10, pady=10)
            j += 1
            if j % 3 == 0:
                i += 1
                j = 0
