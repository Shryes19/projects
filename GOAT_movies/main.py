from bs4 import BeautifulSoup
import requests
movie_list = []
new_lsit = []

responce = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
responce.raise_for_status()
text = responce.text

soup = BeautifulSoup(text,"html.parser")
all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

for movies in all_movies:
    movie_list.append(movies.get_text())


new_lsit = movie_list[::-1]

with open("GOAT_MOVIES.txt","w") as file:
    for movie in new_lsit:
        file.write(f"{movie}\n")