import customtkinter as ctk
import titles


class HomeFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        for i in range(5):
            for j in range(4):
                self.my_frame = titles.TitleFrame(master=self)
                self.my_frame.grid(row=i, column=j, padx=20, pady=20)
