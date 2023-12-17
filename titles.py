import io
import urllib.request

import customtkinter as ctk
from PIL import Image

import movieInfo
import seriesInfo


class TitleFrame(ctk.CTkFrame):
    def __init__(self, master, title, title_id, img_path, platform, **kwargs):
        super().__init__(master, **kwargs)

        self.movie_window = None
        self.series_window = None
        try:
            with urllib.request.urlopen("https://www.themoviedb.org/t/p/w600_and_h900_bestv2" + img_path) as u:
                raw_data = u.read()
            image = Image.open(io.BytesIO(raw_data))
        except:
            image = Image.open("Assets/no poster.png")
        self.poster_path = ctk.CTkImage(image, size=(120, 170))
        self.grid_rowconfigure(1, weight=1)  # configure grid system
        self.grid_columnconfigure(1, weight=1)

        self.title_poster = ctk.CTkLabel(self, text="", image=self.poster_path)
        self.title_poster.grid(row=0, column=0)

        # add widgets onto the frame, for example:
        self.title_label = ctk.CTkLabel(self, text="Title: " + title + "\nID: " + str(title_id), wraplength=150)
        self.title_label.grid(row=1, column=0, padx=10, pady=10)

        self.title_poster.bind("<Button-1>", lambda event: self.show_series_info(title_id, platform))

    def show_series_info(self, title_id, title_platform):
        if title_platform == "series":
            # Create and display the SeriesInfoWindows

            if self.series_window is None or not self.series_window.winfo_exists():
                self.series_window = seriesInfo.SeriesInfoFrame(self.master, title_id)
                self.series_window.grab_set()
            else:
                self.series_window.focus()  # if window exists focus it
        elif title_platform == "movie":
            # Create and display the SeriesInfoWindows

            if self.movie_window is None or not self.movie_window.winfo_exists():
                self.movie_window = movieInfo.MovieInfoFrame(self.master, title_id)
                self.movie_window.grab_set()
            else:
                self.movie_window.focus()  # if window exists focus it
