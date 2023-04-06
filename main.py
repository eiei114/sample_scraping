import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = 'http://books.toscrape.com/'

response = requests.get(url)

titles = []
prices = []

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    for book in books:
        title = book.find('h3').find('a')['title']
        price = float(book.find('p', class_='price_color').text[1:].replace('£', ''))
        titles.append(title)
        prices.append(price)

    plt.bar(titles, prices)
    plt.xlabel('Book Titles')
    plt.ylabel('Prices (£)')
    plt.xticks(rotation=90)
    plt.title('Book Prices')
    plt.tight_layout()
    plt.savefig('book_prices.png', dpi=300)
    plt.show()

else:
    print('Failed to retrieve the webpage.')