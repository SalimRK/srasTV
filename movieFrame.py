import customtkinter as ctk
import titles
import query


class MovieFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        popular = query.get_popular_movie()
        i = 0
        j = 0
        for p in popular:
            self.my_frame = titles.TitleFrame(master=self, title_id=p.id, title=p.title, img_path=p.poster_path,
                                              platform="movie")
            self.my_frame.grid(row=i, column=j, padx=10, pady=10)
            j += 1
            if j % 3 == 0:
                i += 1
                j = 0
