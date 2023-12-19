import customtkinter as ctk
import homeFrame
import movieFrame
import seriesFrame
import searchFrame
from PIL import Image
import os

# icons
icon_names = ["home icon.png", "movies icon.png", "series icon.png", "Search icon.png", "download icon.png"]
icon_paths = [os.path.abspath(os.path.join("Assets", name)) for name in icon_names]
icon_images = [ctk.CTkImage(Image.open(path)) for path in icon_paths]

home_icon_path, movies_icon_path, series_icon_path, search_icon_path, downloads_icon_path = icon_images


class TopFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Set the initial width range
        self.min_width = 70
        self.max_width = 120

        # home button
        self.home_button = ctk.CTkButton(
            self, image=home_icon_path, text="", command=self.home_click, height=70, width=self.min_width
        )
        self.home_button.pack(side=ctk.LEFT, padx=30, pady=10)

        # Movie button
        self.movies_button = ctk.CTkButton(
            self, image=movies_icon_path, text="", command=self.movies_click, height=70, width=self.min_width
        )
        self.movies_button.pack(side=ctk.LEFT, padx=30, pady=10)

        # Series button
        self.series_button = ctk.CTkButton(
            self, image=series_icon_path, text="", command=self.series_click, height=70, width=self.min_width
        )
        self.series_button.pack(side=ctk.LEFT, padx=30, pady=10)

        # Search button
        self.search_button = ctk.CTkButton(
            self, image=search_icon_path, text="", command=self.search_click, height=70, width=self.min_width
        )
        self.search_button.pack(side=ctk.LEFT, padx=30, pady=10)

        # Download button
        self.downloads_button = ctk.CTkButton(
            self, image=downloads_icon_path, text="", command=self.downloads_click, height=70, width=self.min_width
        )
        self.downloads_button.pack(side=ctk.LEFT, padx=30, pady=10)

        # Bind the resize event to adjust button widths
        self.bind("<Configure>", self.on_resize)

    def home_click(self):
        self.switch_frame(homeFrame.HomeFrame)

    def movies_click(self):
        self.switch_frame(movieFrame.MovieFrame)

    def series_click(self):
        self.switch_frame(seriesFrame.SeriesFrame)

    def search_click(self):
        self.switch_frame(searchFrame.SearchFrame)

    def downloads_click(self):
        pass

    # switch frames: delete the old and add the new one
    def switch_frame(self, frame_class):
        if hasattr(self, 'current_frame'):
            self.current_frame.destroy()

        self.current_frame = frame_class(self.master)
        self.current_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew", columnspan=5)

    # Event handler for resizing the window
    def on_resize(self, event):
        # Calculate the new width based on the window size
        new_width = min(max(self.min_width, event.width // 10), self.max_width)

        # Set the new width for each button
        for button in [
            self.home_button,
            self.movies_button,
            self.series_button,
            self.search_button,
            self.downloads_button,
        ]:
            button.configure(width=new_width)
