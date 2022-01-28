from bs4 import BeautifulSoup
import requests, json
# import pandas as pd

def lockup_split(string):
    first_part = []
    pointer = 0
    while string[pointer].isalpha() == True or string[pointer] == "-":
        first_part.append(string[pointer])
        pointer += 1

    first_part = "".join(first_part)
    second_part = string.replace(first_part, "")

    return first_part, second_part

def tokens_split(string):
    first_part = []
    pointer = 0
    while string[pointer].isalpha() == True or string[pointer] == " ":
        first_part.append(string[pointer])
        pointer += 1

    first_part = "".join(first_part)
    second_part = string.replace(first_part, "")

    return first_part, second_part

def minmax_split(string):
    first_part = []
    pointer = 0
    M_counter = 0

    while M_counter < 3:
        if string[pointer] == "M":
            M_counter += 1
        if M_counter < 3:
            first_part.append(string[pointer])
        pointer += 1

    first_part = "".join(first_part)
    second_part = string.replace(first_part, "")
    return first_part, second_part
 
def normal_split(string):
    first_part = []
    pointer = 0
    while string[pointer] != "$":
        first_part.append(string[pointer])
        pointer += 1

    first_part = "".join(first_part)
    second_part = string.replace(first_part, "")

    return first_part, second_part

response = requests.get(
                url="https://cryptorank.io/ico/zone",
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
                })

page_html = response.text
soup = BeautifulSoup(page_html, 'html.parser')

dados = []
lista = []

for div in soup.find_all("div", attrs={"class": "columns__Column-sc-1g8p74z-1 icQbwQ"}):
    try:
        dado = div.div.text
    except AttributeError:
        dado = div.text
    dados.append(dado)

h3_tableNames =  soup.find_all("h3", attrs={"class": "app-header__AppHeader-sc-13ssse4-0 styled__InnerHeader-sc-3j9k11-2 dBBTCt fUiwcC"})
for h3_tableName in h3_tableNames:
    # print(h3_tableName.text)
    info_divs = h3_tableName.nextSibling
    table_information = []
    for div in info_divs:

        info_splited = div.text.split('\n') #packs of name and info like ['Strategic 2 price$ 0.032']
        if info_splited != ['']: 
            column_info = "".join(info_splited)
            table_information.append(column_info)

    organized_table_information = {}
    for column in set(table_information):
        try:
            if "Lock-up" in column:
                column_row1, column_row2 = lockup_split(column)
                organized_table_information[column_row1] = column_row2
            if "Tokens" in column:
                column_row1, column_row2 = tokens_split(column)
                organized_table_information[column_row1] = column_row2
            if "Min/Max" in column:
                column_row1, column_row2 = minmax_split(column)
                organized_table_information[column_row1] = column_row2
            else:
                column_row1, column_row2 = normal_split(column)
                organized_table_information[column_row1] = column_row2
        except:
            pass
    dict = {h3_tableName.text : organized_table_information}
    print(dict, '\n')

# df = pd.DataFrame.from_dict(dados_estruturados)
# print(dados_estruturados)
# df.to_csv(f'specific_coin.csv', index=False, header=True)