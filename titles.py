import customtkinter as ctk
from PIL import Image
import urllib.request
import io


class TitleFrame(ctk.CTkFrame):
    def __init__(self, master, title, title_id, img_path, **kwargs):
        super().__init__(master, **kwargs)

        with urllib.request.urlopen("https://www.themoviedb.org/t/p/w600_and_h900_bestv2" + img_path) as u:
            raw_data = u.read()
        image = Image.open(io.BytesIO(raw_data))
        self.poster_path = ctk.CTkImage(image, size=(120, 170))

        self.grid_rowconfigure(1, weight=1)  # configure grid system
        self.grid_columnconfigure(1, weight=1)

        self.title_poster = ctk.CTkLabel(self, text="", image=self.poster_path)
        self.title_poster.grid(row=0, column=0)

        # add widgets onto the frame, for example:
        self.title_label = ctk.CTkLabel(self, text="Title: " + title + "\nID: " + str(title_id), wraplength=150)
        self.title_label.grid(row=1, column=0, padx=10, pady=10)
