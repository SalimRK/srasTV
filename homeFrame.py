import customtkinter as ctk


class HomeFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.text = """
        This project is an app for streaming movies and tv shows for free with no fees or ads

        Author: salim rizk
        Github: https://github.com/SalimRK/
        Gmail: rk@salimrk@gmail.com
        Number: PRIVET 
        linkedin: https://www.linkedin.com/in/salim-rizk/
        """
        self.label = ctk.CTkLabel(self, text=self.text)
        self.label.grid(row=0, column=0, padx=10, pady=10)
