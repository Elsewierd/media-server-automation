import requests

movie_query = f"?query={movie_str.strip().replace(' ', '+')}"
search_url = f"{entry_dict['tmdb']['url']}/search/movie{movie_query}"
headers = entry_dict['tmdb']['headers']
response = requests.get(search_url, headers=headers)

print(response.status_code)
print(response.text)