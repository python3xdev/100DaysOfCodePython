import requests
from bs4 import BeautifulSoup

print("Scraping website...")

URL = "https://www.theguardian.com/film/2019/sep/13/100-best-films-movies-of-the-21st-century"

response = requests.get(URL)
website_html = response.text

print("Website scraped.")

soup = BeautifulSoup(website_html, "html.parser")

titles_reversed = [title.getText() for title in soup.select(selector="div h2 strong")][::-1]
for index in range(0, 100):
    with open("movies.txt", "a") as file:
        file.write(f"{index+1}) {titles_reversed[index]}\n")

print("Writing data to 'movies.txt' file completed.")
