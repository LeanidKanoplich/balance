import requests
from bs4 import BeautifulSoup
import os

url = "http://127.0.0.1:5500/balance/index.html"  

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('link', rel='stylesheet'):  
    css_url = link.get('href')
    
    if 'http' in css_url:
        css_content = requests.get(css_url).text
    else:
        css_content = requests.get(os.path.join(url, css_url)).text

    css_filename = css_url.split('/')[-1]
    with open(os.path.join('/Users/tlnc/Documents/scrypt/', css_filename), 'w') as file:
        file.write(css_content)
