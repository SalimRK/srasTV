import os

# Replace these values with the actual ID and episode information
TMDB_ID = 1403
seasonNumber = 1
episodeNumber = 2

# Determine the absolute path to the template HTML file
template_path = os.path.abspath('temp/templateTv.html')
print(template_path)

# Generate TV series URL with query parameters
tv_src_url = f"file://{template_path}?TMDB_ID={TMDB_ID}&seasonNumber={seasonNumber}&episodeNumber={episodeNumber}"
print(tv_src_url)



import query

series_data = query.get_tv_info(1403)
for tabs in range(series_data.number_of_seasons):
    season_data = query.get_seasons(1403, tabs)
    for episode_data in season_data.episodes:
        print("episodes name:" + str(episode_data.name))
        print("episodes overview:" + str(episode_data.overview))
        print("episodes data:" + str(episode_data.air_date))
        print("episodes number:" + str(episode_data.episode_number))
        print("______________________________________________________________________________________________________")

    print("###########################################################################################################")

