import customtkinter as ctk

from PIL import Image

home_icon_path = ctk.CTkImage(Image.open("Assets/home icon.png"))
movies_icon_path = ctk.CTkImage(Image.open("Assets/movies icon.png"))
series_icon_path = ctk.CTkImage(Image.open("Assets/series icon.png"))
search_icon_path = ctk.CTkImage(Image.open("Assets/Search icon.png"))
downloads_icon_path = ctk.CTkImage(Image.open("Assets/download icon.png"))


class TopFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.home_button = ctk.CTkButton(self, image=home_icon_path, text="", command=self.home_click, height=70,
                                         width=70)
        self.home_button.pack(side=ctk.LEFT, padx=30, pady=10)

        self.movies_button = ctk.CTkButton(self, image=movies_icon_path, text="", command=self.movies_click, height=70,
                                           width=70)
        self.movies_button.pack(side=ctk.LEFT, padx=30, pady=10)

        self.series_button = ctk.CTkButton(self, image=series_icon_path, text="", command=self.series_click, height=70,
                                           width=70)
        self.series_button.pack(side=ctk.LEFT, padx=30, pady=10)

        self.search_button = ctk.CTkButton(self, image=search_icon_path, text="", command=self.search_click, height=70,
                                           width=70)
        self.search_button.pack(side=ctk.LEFT, padx=30, pady=10)

        self.downloads_button = ctk.CTkButton(self, image=downloads_icon_path, text="", command=self.downloads_click,
                                              height=70, width=70)
        self.downloads_button.pack(side=ctk.LEFT, padx=30, pady=10)

    def home_click(self):
        pass

    def movies_click(self):
        pass

    def search_click(self):
        pass

    def series_click(self):
        pass

    def downloads_click(self):
        pass
