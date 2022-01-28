## A receita do bolo

* Achar a URL de onde você quer retirar informação
* Inspecionar a página
* Achar na página os dados que você quer extrair. (Pesquise por Xpath e tags html)
* Escreva o código que automatiza esse processo
* Armazene os dados no formato desejado :D

## Exemplo de saida
![imagem_do_output_pasticos](./print_pasticos.png)

## Gostei, como faz?
Depois de clonar esse repo é só copiar essas 3 linhas no seu terminal pra sair arrancado dado de site por ai
```bash
>python -m venv venv #criando ambiente virtual 
>./venv/Scripts/Activate.ps1 #Ativando o ambiente virtual 
>pip install -r requirements.txt #Adicionando as libs necessárias
```
O lance do ambiente virtual é que todas suas dependências *(que no python costumam ser muitas)*  ficam apenas num diretório específico. <br>
Logo, com uma venv você pode criar projetos que usam versões diferentes da mesma biblioteca sem que haja conflito na hora do import.

# Getting Started
```bash
# Clone repository
git clone https://github.com/Mesheo/Biblioteca-API.git && cd Biblioteca-API

# Create Virtual Environment
python -m venv venv && ./venv/Scripts/Activate.ps1

# Install dependencies
pip install django djangorestframework

# Run Application
python manage.py runserver
```