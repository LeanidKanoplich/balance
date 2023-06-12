import requests
from bs4 import BeautifulSoup

url = "http://example.com"  # Замените на URL сайта, который хотите скопировать

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

html = soup.prettify()

with open('output.html', 'w') as file:
    file.write(html)
