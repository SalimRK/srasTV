import customtkinter as ctk
from PIL import Image


class TitleFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.x = 120
        self.y = 180
        self.poster_path = ctk.CTkImage(Image.open("TMP/marvel agent of shield post.jpg"), size=(self.x, self.y))

        self.grid_rowconfigure(1, weight=1)  # configure grid system
        self.grid_columnconfigure(1, weight=1)

        self.title_poster = ctk.CTkLabel(self, text="", image=self.poster_path)
        self.title_poster.grid(row=0, column=0)


        # add widgets onto the frame, for example:
        self.label = ctk.CTkLabel(self)
        self.label.grid(row=1, column=0, padx=20, pady=20)
