import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin  # импортируйте urljoin

url = "https://rapsoil.ee"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('link', rel='stylesheet'):  
    css_url = link.get('href')
    
    if 'http' in css_url:
        css_content = requests.get(css_url).text
    else:
        # замените os.path.join на urljoin
        css_content = requests.get(urljoin(url, css_url)).text

    css_filename = css_url.split('/')[-1]
    with open(os.path.join('/Users/tlnc/Documents/new/', css_filename), 'w') as file:
        file.write(css_content)


