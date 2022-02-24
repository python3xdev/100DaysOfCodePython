import requests
import csv
import os
from pprint import pprint
from bs4 import BeautifulSoup

URL = "https://www.trackmania.com/news/page/"

headers = {
    "User-Agent": YOUR_USER_AGENT!
}


def get_posts_from_pages():
    more_posts = True
    page = 1
    while more_posts:
        print(f"Working on page {page}.")
        print("Scraping...")
        response = requests.get(f'{URL}{page}', headers=headers)
        data = response.content

        soup = BeautifulSoup(data, "html.parser")
        posts = soup.select("article.post")
        extract_and_save_data(posts)
        page += 1
        if len(posts) == 0:
            print("No more posts. DONE!")
            more_posts = False


def extract_and_save_data(posts):
    print("Writing data...")
    for post in posts:
        title = post.select_one("h3.elementor-post__title a").getText().strip()
        link = post.select_one("h3.elementor-post__title a")['href'].strip()
        date = post.select_one("span.elementor-post-date").getText().strip()

        with open("TrackmaniaNews.csv", "a", newline='') as file:
            new_row = [date, title, link]
            writer = csv.writer(file)
            writer.writerow(new_row)
    print("Finished writing data.")


def create_file():
    # if not os.path.isfile("TrackmaniaNews.csv"):  # we will not be checking if the file already exists
    with open("TrackmaniaNews.csv", "w", newline='') as file:  # we are just going to write over the file...
        csv_headers = ['Date', 'Title', 'Link']
        writer = csv.writer(file)
        writer.writerow(csv_headers)


def run():
    create_file()
    get_posts_from_pages()


if __name__ == "__main__":
    run()
