from unicodedata import category
from bs4 import BeautifulSoup
import requests, json, pprint

response = requests.get(
                url="https://cryptorank.io/upcoming-ico",
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
                })

page_html = response.text
soup = BeautifulSoup(page_html, 'html.parser')

dados = []

for div in soup.find_all("div", attrs={"class" : "styled__StyledIcoCard-sc-u5bvc5-1 cdQCms"}):

    card_lines = div.find_all("div", attrs={"class": "card-line"})
    name_span = div.find("span", attrs={"class": "name"})
    category_spans = card_lines[0].find_all("span")
    initial_cap_spans = card_lines[1].find_all("span")
    raise_goal_spans = card_lines[2].find_all("span")

    name = name_span.a.text
    category = category_spans[1].text
    initial_cap = initial_cap_spans[1].text
    raise_goal = raise_goal_spans[1].text
    
    dado = {
        "name": name,
        "category": category,
        "initial_cap": initial_cap,
        "raise_goal": raise_goal
    }

    dados.append(dado)
 
[print(dado) for dado in dados]
