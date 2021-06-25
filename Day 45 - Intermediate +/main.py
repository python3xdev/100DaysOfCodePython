from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/news"
response = requests.get(url)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_up_votes = [int(score.getText().split()[0]) if score is not None else (score, 0) for score in
                    soup.find_all(name="td", class_="subtext")] # Just in case an article has no up votes it appends a 0.

largest_number = max(article_up_votes)
largest_index = article_up_votes.index(largest_number)

print(largest_index)

# PRINTING THE MOST UPVOTED ARTICLE
print(f'''
{article_texts[largest_index]}
{article_links[largest_index]}
{article_up_votes[largest_index]}
''')

# PRINTING ALL ARTICLES
# print(f'''
# {article_texts}
# {article_links}
# {article_upvotes}
# ''')





# SCRAPING A LOCAL FILE

# with open("website.html") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
#
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.p)
#
# # all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
# #
# # for tag in all_anchor_tags:
# #     # print(tag.getText())
# #     print(tag.get('href'))
#
#
# # heading = soup.find(name="h1", id="name")
# # print(heading)
#
#
# # section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.getText())
# # print(section_heading.name)
# # print(section_heading.get("class"))
#
#
# company_url = soup.select_one(selector="p a")
# name = soup.select_one(selector="#name")  # ID
# headings = soup.select(".heading")  # all elements with the CLASS ".heading"
# print(headings)
