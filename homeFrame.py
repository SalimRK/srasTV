import customtkinter as ctk


class HomeFrame(ctk.CTkFrame):

    text = """
    This project is an app for streaming movies and tv shows for free with no fees or ads
    author: salim rizk
    github: 
    
    
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.label = ctk.CTkLabel(self, text="")
        self.label.grid(row=1, column=0, padx=10, pady=10)

