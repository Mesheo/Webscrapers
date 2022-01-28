from bs4 import BeautifulSoup
import requests, json, pandas as pd

response = requests.get(
                url="https://cryptorank.io/ico",
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
                })

page_html = response.text
soup = BeautifulSoup(page_html, 'html.parser')

dados = []
for tr in soup.find_all("tr", attrs={"class": "styled__WrappedTableRow-sc-13ogi24-3 haOyIW"}):
    td_tags = tr.find_all("td")

    name = tr.div['title'] 
    price = td_tags[1].text
    sale_price = td_tags[2].text
    market_cap = td_tags[3].text

    dado = {
        "name": name,
        "price": price,
        "sale_price": sale_price,
        "market_cap": market_cap
    }

    dados.append(dado)
df = pd.DataFrame.from_dict(dados)
# df.to_csv(f'past_ICOs.csv', index=False, header=True)
 
[print(dado) for dado in dados]