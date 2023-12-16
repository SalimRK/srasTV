import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.attributes("-fullscreen", "False")
        self.geometry("700x700")
        self.title("CTk example")

        # self.bind("<F11>", self.key_handler)
        # self.fullScreen = False

        self.grid_rowconfigure(1, weight=1)  # configure grid system
        self.grid_columnconfigure(1, weight=1)

        import topframe

        self.my_frame = topframe.TopFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew", columnspan=5)

        import homeFrame
        self.my_frame = homeFrame.HomeFrame(master=self)
        self.my_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew", columnspan=5)

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
    app = App()
    app.mainloop()
