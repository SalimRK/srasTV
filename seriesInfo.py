import customtkinter as ctk
import query


class SeriesInfoFrame(ctk.CTkToplevel):
    def __init__(self, master, title_id, **kwargs):
        super().__init__(master, **kwargs)
        self.geometry("700x700")
        self.title_id = title_id
        self.title(self.title_id)

        self.info_frame = Info_Scrollable_Frame(self, title_id=title_id)
        self.info_frame.pack(expand=True, fill="both", padx=20, pady=20)


class Info_Scrollable_Frame(ctk.CTkScrollableFrame):
    def __init__(self, master, title_id, **kwargs):
        super().__init__(master, **kwargs)

        series_data = query.get_tv_info(title_id)
        img_path = series_data.poster_path
        title = series_data.name
        overview = series_data.overview
        genres = series_data.genres
        original_language = series_data.original_language
        origin_country = series_data.origin_country
        vote_average = series_data.vote_average
        vote_count = series_data.vote_count
        image = query.get_poster(img_path)

        self.poster_path = ctk.CTkImage(image, size=(150, 200))
        self.title_poster = ctk.CTkLabel(self, text="", image=self.poster_path)
        self.title_poster.grid(row=0, column=0, rowspan=3, padx=10, pady=10)

        # Display series information
        self.title_label = ctk.CTkLabel(self, text=title, font=("Helvetica", 20, "bold"))
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

        self.series_tab_view = SeriesTabView(self, series_data, title_id=title_id)
        self.series_tab_view.grid(row=3, column=0, columnspan=2)


class SeriesTabView(ctk.CTkTabview):
    def __init__(self, master, series_data, title_id, **kwargs):
        super().__init__(master, **kwargs)
        self.title_id = title_id

        for tabs in range(series_data.number_of_seasons):
            self.add("S" + str(tabs + 1))
            self.season_data = query.get_seasons(self.title_id, tabs)
            for episode_data in self.season_data.episodes:
                self.episode = episode_frame(master=self.tab(f"S{tabs + 1}"), episode_data_name=episode_data.name,
                                             episode_data_overview=episode_data.overview,
                                             episode_data_number=episode_data.episode_number,
                                             season_number=tabs + 1,
                                             title_id=title_id)
                self.episode.pack(anchor='w')


class episode_frame(ctk.CTkFrame):
    def __init__(self, master, episode_data_name, episode_data_overview, episode_data_number, season_number,
                 title_id, **kwargs):
        super().__init__(master, **kwargs)
        self.title_id = title_id
        self.episode_data_name = episode_data_name
        self.episode_data_overview = episode_data_overview
        self.episode_data_number = episode_data_number
        self.season_number = season_number

        self.watch_button = ctk.CTkButton(self, text="Watch", command=self.episode, width=50, height=50)
        self.watch_button.grid(row=0, column=0, padx=10, pady=10, rowspan=2, sticky=ctk.W)

        self.ep_number_label = ctk.CTkLabel(master=self, text=f"E{self.episode_data_number}S{self.season_number}",
                                            font=("Helvetica", 16, "bold"))
        self.ep_number_label.grid(row=0, column=1, padx=20, pady=10, sticky=ctk.W)

        self.ep_name_label = ctk.CTkLabel(master=self, text=self.episode_data_name, font=("Helvetica", 16, "bold"))
        self.ep_name_label.grid(row=0, column=2, padx=20, pady=10, sticky=ctk.W)

        self.ep_overview_label = ctk.CTkLabel(master=self, text=self.episode_data_overview, wraplength=400)
        self.ep_overview_label.grid(row=1, column=1, padx=20, pady=10, columnspan=2, sticky=ctk.W)

    def episode(self):
        self.url_window = UrlWindow(self, title_id=self.title_id, episode_data_number=self.episode_data_number,
                                    season_number=self.season_number)
        self.url_window.grab_set()


class UrlWindow(ctk.CTkToplevel):
    def __init__(self, master, title_id, episode_data_number, season_number, **kwargs):
        super().__init__(master, **kwargs)
        self.geometry("450x100")
        self.title(f"S{season_number}E{episode_data_number}")

        url = query.watch_episode(title_id=title_id, episode_number=episode_data_number, season_number=season_number)

        self.url_textbox = ctk.CTkTextbox(self, width=400, height=50)
        self.url_textbox.insert("0.0", url)
        self.url_textbox.configure(state="disabled")
        self.url_textbox.grid(row=0, column=0, padx=10, pady=10)

