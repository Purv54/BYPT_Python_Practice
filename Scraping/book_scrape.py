import requests
import bs4

# get every book with rating of 2

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

# res = requests.get(base_url.format(1))
# soup = bs4.BeautifulSoup(res.text, "lxml")

# products = soup.select('.product_pod')
# ex = products[0]
# three = ex.select('.star-rating.Two')
# print(three)
# print(ex.select('a')[1]["title"])
two_star_books = []
for i in range(1, 51):
    res = requests.get(base_url.format(i))
    soup = bs4.BeautifulSoup('res.text', "lxml")

    books = soup.select('.product_pod')

    for book in books:
        if len(book.select('.start-rating.Two')) > 0:
            two_star_books.append(book.select('a')[1]['title'])
print(two_star_books)