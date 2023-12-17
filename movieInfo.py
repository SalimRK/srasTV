import customtkinter as ctk
import query
import titles


class MovieInfoFrame(ctk.CTkToplevel):
    def __init__(self, master, title_id, **kwargs):
        super().__init__(master, **kwargs)

        series_data = query.get_movie_info(title_id)
        self.title_id = title_id
        img_path = series_data.poster_path
        title = series_data.title
        overview = series_data.overview
        genres = series_data.genres
        original_language = series_data.original_language
        vote_average = series_data.vote_average
        vote_count = series_data.vote_count

        self.geometry("600x700")
        self.title(title)

        image = query.get_poster(img_path)
        self.poster_path = ctk.CTkImage(image, size=(150, 200))
        self.title_poster = ctk.CTkLabel(self, text="", image=self.poster_path)
        self.title_poster.grid(row=0, column=0, rowspan=2, padx=10, pady=10)

        # Display series information
        self.title_label = ctk.CTkLabel(self, text=title, font=("Helvetica", 16, "bold"))
        self.title_label.grid(row=0, column=1, sticky=ctk.W, padx=10, pady=10)

        self.overview_label = ctk.CTkLabel(self, text=overview, wraplength=400, justify=ctk.LEFT)
        self.overview_label.grid(row=1, column=1, sticky=ctk.W, padx=10, pady=5)

        self.details_label = ctk.CTkLabel(self,
                                          text=f"Vote Average: {vote_average}\n"
                                               f"Vote Count: {vote_count}\n"
                                               f"Genres: {', '.join(genre['name'] for genre in genres)}\n"
                                               f"Original Language: {original_language}\n",
                                          justify=ctk.LEFT)
        self.details_label.grid(row=2, column=1, sticky=ctk.W, padx=10, pady=5)

        self.watch_button = ctk.CTkButton(self, text="Watch Movie", command=self.launch_movie_function)
        self.watch_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.url_textbox = ctk.CTkTextbox(self, width=400, height=50)
        self.url_textbox.configure(state="disabled")
        self.url_textbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.recommendations_frame = ctk.CTkFrame(self)
        self.recommendations_frame.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
        recommendations = query.get_movie_recommendations(title_id)

        i = 0
        j = 0
        for r in recommendations:
            self.my_frame = titles.TitleFrame(master=self.recommendations_frame, title_id=r.id, title=r.title, img_path=r.poster_path,
                                         platform="movie")
            self.my_frame.grid(row=i, column=j, padx=10, pady=10)

            j += 1
            if j % 3 == 0:
                break

    def launch_movie_function(self):
        # Assuming you have a function in the query file that you want to call
        url = query.watch_movie(self.title_id)
        self.url_textbox.configure(state="normal")
        self.url_textbox.insert("0.0", url)
        self.url_textbox.configure(state="disabled")
