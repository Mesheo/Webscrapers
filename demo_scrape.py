from bs4 import BeautifulSoup
import requests, json

'''
This code will display all cryptocurrency names from the website present on the URL
You can check the XPaths on the developer mode of your browser to find the same information
'''

response = requests.get(
                url="https://cryptorank.io/active-ico",
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
                })

page_html = response.text
soup = BeautifulSoup(page_html, 'html.parser')

for tr in soup.find_all("tr", attrs={"class": "styled__WrappedTableRow-sc-13ogi24-3 haOyIW"}):
    print(tr.div['title']) 
