import requests
import bs4

# res = requests.get("https://quotes.toscrape.com/")
# soup = bs4.BeautifulSoup(res.text, "lxml")

# authors = soup.select('.author')
# print(authors[0].getText())

# tags = soup.select('.tag')
# print(tags[1].getText())

# wheen page numbers are known in advance


# authors = set()
# url = "https://quotes.toscrape.com/page/"
# for i in range(1, 11):
#     page_url = url + str(i)
#     res = requests.get(page_url)
#     soup = bs4.BeautifulSoup(res.text, "lxml")

#     for author in soup.select('.author'):
#         authors.add(author.getText())


# print(authors)

# when age numbers are not known in advance

authors = set()
page = 1
page_valid = True
url = "https://quotes.toscrape.com/page/"

while page_valid:

    page_url = url + str(page)
    res = requests.get(page_url)
    soup = bs4.BeautifulSoup(res.text, "lxml")

    if "No quotes found!" in soup.getText():
        page_valid = False
    else:
        if len(soup.select('.author')) > 0:

            for author in soup.select('.author'):
                authors.add(author.getText())
    page += 1

print(authors)