import customtkinter as ctk


class SeriesInfoFrame(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.geometry("200x150")
        self.title("Search Error")

        self.error_label = ctk.CTkLabel(self, text="There is no such titles")
        self.error_label.pack(padx=20, pady=20)

        self.ok_button = ctk.CTkButton(self, text="ok", command=self.ok)
        self.ok_button.pack(padx=20, pady=20)

    def ok(self):
        self.destroy()
