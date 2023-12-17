import os
import webbrowser

# Replace these values with the actual ID and episode information
TMDB_ID = 1403
seasonNumber = 1
episodeNumber = 2

# Determine the absolute path to the template HTML file
template_path = os.path.abspath('temp/template.html')
print(template_path)

# Generate TV series URL with query parameters
tv_src_url = f"file://{template_path}?TMDB_ID={TMDB_ID}&seasonNumber={seasonNumber}&episodeNumber={episodeNumber}"
print(tv_src_url)
