import customtkinter as ctk
import querys


class SeriesInfoFrame(ctk.CTkToplevel):
    def __init__(self, master, title_id, **kwargs):
        super().__init__(master, **kwargs)
        self.geometry("600x500")
        series_data = querys.get_tv_info(title_id)

        img_path = series_data.poster_path
        title = series_data.name
        overview = series_data.overview
        genres = series_data.genres
        original_language = series_data.original_language
        origin_country = series_data.origin_country
        vote_average = series_data.vote_average
        vote_count = series_data.vote_count

        image = querys.get_poster(img_path)

        self.poster_path = ctk.CTkImage(image, size=(150, 200))
        self.title_poster = ctk.CTkLabel(self, text="", image=self.poster_path)
        self.title_poster.grid(row=0, column=0, rowspan=5, padx=10, pady=10)

        # Display series information
        self.title_label = ctk.CTkLabel(self, text=title, font=("Helvetica", 16, "bold"))
        self.title_label.grid(row=0, column=1, sticky=ctk.W, padx=10, pady=10)

        self.overview_label = ctk.CTkLabel(self, text=overview, wraplength=400, justify=ctk.LEFT)
        self.overview_label.grid(row=1, column=1, sticky=ctk.W, padx=10, pady=5)

        self.details_label = ctk.CTkLabel(self,
                                          text=f"Vote Average: {vote_average}\n"
                                               f"Vote Count: {vote_count}\n"
                                               f"Genres: {', '.join(genre['name'] for genre in genres)}\n"
                                               f"Original Language: {original_language}\n"
                                               f"Origin Country: {', '.join(str(country) for country in origin_country)}",
                                          justify=ctk.LEFT)
        self.details_label.grid(row=2, column=1, sticky=ctk.W, padx=10, pady=5)
