import customtkinter as ctk

from PIL import Image
search_icon_path = ctk.CTkImage(Image.open("Assets/Search icon.png"))


class SearchFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.search_entry = ctk.CTkEntry(self, placeholder_text="search")
        self.search_entry.grid(row=0, column=0, padx=10, pady=10, sticky=ctk.EW)  # Use sticky=ctk.EW

        self.search_button = ctk.CTkButton(self, text="Search", image=search_icon_path, command=self.search_button_clicked)
        self.search_button.grid(row=0, column=1, padx=10, pady=10)

        # Configure column 0 to expand horizontally
        self.grid_columnconfigure(0, weight=1)

    def search_button_clicked(self):
        search_for = self.search_entry.get()
        print(search_for)
