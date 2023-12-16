import customtkinter as ctk
from PIL import Image
import io
import urllib.request

class SeriesInfoFrame(ctk.CTkFrame):
    def __init__(self, master, title_id, title, img_path, overview, first_air_date, vote_average, vote_count, genres, original_language, origin_country, **kwargs):
        super().__init__(master, **kwargs)

        # Download and display the poster
        with urllib.request.urlopen("https://www.themoviedb.org/t/p/w600_and_h900_bestv2" + img_path) as u:
            raw_data = u.read()
        image = Image.open(io.BytesIO(raw_data))
        self.poster_path = ctk.CTkImage(image, size=(120, 170))
        self.title_poster = ctk.CTkLabel(self, text="", image=self.poster_path)
        self.title_poster.grid(row=0, column=0, rowspan=5, padx=10, pady=10)

        # Display series information
        self.title_label = ctk.CTkLabel(self, text=title, font=("Helvetica", 16, "bold"))
        self.title_label.grid(row=0, column=1, sticky=ctk.W, padx=10, pady=10)

        self.overview_label = ctk.CTkLabel(self, text=overview, wraplength=400, justify=ctk.LEFT)
        self.overview_label.grid(row=1, column=1, sticky=ctk.W, padx=10, pady=5)

        self.details_label = ctk.CTkLabel(self, text=f"First Air Date: {first_air_date}\n"
                                                      f"Vote Average: {vote_average}\n"
                                                      f"Vote Count: {vote_count}\n"
                                                      f"Genres: {', '.join(genres)}\n"
                                                      f"Original Language: {original_language}\n"
                                                      f"Origin Country: {', '.join(origin_country)}",
                                          justify=ctk.LEFT)
        self.details_label.grid(row=2, column=1, sticky=ctk.W, padx=10, pady=5)