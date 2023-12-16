import customtkinter as ctk
import titles
from PIL import Image

search_icon_path = ctk.CTkImage(Image.open("Assets/Search icon.png"))


class SearchFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.search_entry = ctk.CTkEntry(self, placeholder_text="search")
        self.search_entry.grid(row=0, column=0, padx=10, pady=10, sticky=ctk.EW)  # Use sticky=ctk.EW

        self.search_button = ctk.CTkButton(self, text="Search", image=search_icon_path,
                                           command=self.search_button_clicked)
        self.search_button.grid(row=0, column=1, padx=10, pady=10)

        # Configure column 0 to expand horizontally
        self.grid_columnconfigure(0, weight=1)

        # Radio buttons
        self.selected_option = ctk.StringVar(value="Series")  # Default option
        self.series_radio = ctk.CTkRadioButton(self, text="Series", variable=self.selected_option, value="Series")
        self.series_radio.grid(row=1, column=0, padx=10, pady=5, sticky=ctk.W)

        self.movie_radio = ctk.CTkRadioButton(self, text="Movie", variable=self.selected_option, value="Movie")
        self.movie_radio.grid(row=2, column=0, padx=10, pady=5, sticky=ctk.W)

    def display_result(self, search, selected_option):
        print(search)
        i = 3
        j = 0
        for res in search:
            if selected_option == "Series":
                self.my_frame = titles.TitleFrame(master=self, title_id=res.id, title=res.name,
                                                  img_path=res.poster_path)
            elif selected_option == "Movie":
                self.my_frame = titles.TitleFrame(master=self, title_id=res.id, title=res.title,
                                                  img_path=res.poster_path)
            self.my_frame.grid(row=i, column=j, padx=10, pady=10)
            j += 1
            if j % 3 == 0:
                i += 1
                j = 0

    def search_button_clicked(self):
        search_for = self.search_entry.get()
        selected_option = self.selected_option.get()
        if selected_option == "Series":
            from tmdbv3api import TMDb, TV

            tmdb_api = '7efc97b2176e7c82962cab44ea126623'
            tmdb = TMDb()
            tmdb.api_key = tmdb_api

            tv = TV()
            search = tv.search(search_for)

            self.display_result(search, selected_option)

        elif selected_option == "Movie":
            from tmdbv3api import TMDb, Movie

            tmdb_api = '7efc97b2176e7c82962cab44ea126623'
            tmdb = TMDb()
            tmdb.api_key = tmdb_api

            movie = Movie()
            search = movie.search(search_for)

            self.display_result(search, selected_option)
