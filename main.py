import customtkinter as ctk
from tmdbv3api import TMDb


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.attributes("-fullscreen", "False")
        self.geometry("700x700")
        self.title("srasTV")

        # self.bind("<F11>", self.key_handler)
        # self.fullScreen = False

        self.grid_rowconfigure(1, weight=1)  # configure grid system
        self.grid_columnconfigure(1, weight=1)

        import topframe

        self.top_frame = topframe.TopFrame(master=self)
        self.top_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew", columnspan=5)

        import homeFrame
        self.home_frame = homeFrame.HomeFrame(master=self)
        self.home_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew", columnspan=5)

    # def key_handler(self, event):
    #     if event.keysym == "F11" and self.fullScreen is False:
    #         self.go_full_screen()
    #     elif event.keysym == "F11" and self.fullScreen is True:
    #         self.go_minimised_screen()
    #
    # # add methods to app
    # def go_full_screen(self):
    #     self.attributes("-fullscreen", "True")
    #     self.columnconfigure(0, weight=1)
    #     self.rowconfigure(0, weight=1)
    #     self.fullScreen = True
    #
    # def go_minimised_screen(self):
    #     self.attributes("-fullscreen", "False")
    #     self.geometry("600x500")
    #     self.fullScreen = False


if __name__ == '__main__':
    tmdb_api = '7efc97b2176e7c82962cab44ea126623'
    tmdb = TMDb()
    tmdb.api_key = tmdb_api

    app = App()
    app.mainloop()
