from bs4 import BeautifulSoup
import requests, json, pandas as pd

response = requests.get(
                url="https://cryptorank.io/trending#recently-added",
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
                })

page_html = response.text
soup = BeautifulSoup(page_html, 'html.parser')

table = soup.find("table", {'class': "ui sortable unstackable right aligned table"})


dados = []
for tr in table.tbody("tr"):
    name_tag = tr.find('div')
    price_tag = tr.find('td', {'class': 'single line'})
    market_cap_tag = price_tag.nextSibling

    rank = tr.td.text
    name = name_tag.text
    price = price_tag.text
    market_cap = market_cap_tag.text
    print(market_cap_tag.text)

    dado = {
        "rank": rank,
        "name": name,
        "price": price,
        "market_cap": market_cap
    }

    dados.append(dado)
 
df = pd.DataFrame.from_dict(dados)
# df.to_csv(f'recently_add.csv', index=False, header=True)

[print(dado) for dado in dados]