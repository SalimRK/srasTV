import customtkinter as ctk
import movieInfo
import query
import seriesInfo
import threading


class TitleFrame(ctk.CTkFrame):
    def __init__(self, master, title, title_id, img_path, platform, **kwargs):
        super().__init__(master, **kwargs)

        self.movie_window = None
        self.series_window = None
        self.title = title
        self.title_id = title_id
        self.img_path = img_path
        self.platform = platform

        # Load image in a separate thread
        threading.Thread(target=self.load_image).start()

        self.grid_rowconfigure(1, weight=1)  # configure grid system
        self.grid_columnconfigure(1, weight=1)

        # Rest of your code...

    def load_image(self):
        image = query.get_poster(self.img_path)
        self.poster_path = ctk.CTkImage(image, size=(120, 170))

        # Update the GUI in the main thread
        self.master.after(0, self.update_gui)

    def update_gui(self):
        self.title_poster = ctk.CTkLabel(self, text="", image=self.poster_path)
        self.title_poster.grid(row=0, column=0)
        self.title_label = ctk.CTkLabel(self, text="Title: " + self.title + "\nID: " + str(self.title_id), wraplength=150)
        self.title_label.grid(row=1, column=0, padx=10, pady=10)
        self.title_poster.bind("<Button-1>", lambda event: self.show_info(self.title_id, self.platform))

    def show_info(self, title_id, title_platform):
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
