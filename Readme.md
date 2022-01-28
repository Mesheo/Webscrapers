>Esse é um projeto simples onde eu faço uma "raspagem" de dados no site do cryptorank para obter informações sobre moedas que vão ser lançadas/foram lançadas. Eu não entendo nada de cripto mas entendo de python. Espero que ajude algum cripto enthusiast ou só algum dev inciando seu caminho no mundo do scraping

# Definindo os passos

* Find the URL that you want to scrape
* Inspect the Page.
* Find the data you want to extract. (Search for Xpath and html navigation)
* Write the code.
* Store the data in the required format.

```bash
>python -m venv venv #criando ambiente virtual na sua versao do python
>./venv/Scripts/Activate.ps1 #Ativando o ambiente virtual
>pip install django djangorestframework #instalação local das nossas dependências
>pip install pillow #biblioteca pra lidar com imagens
```
O lance do ambiente virtual é que todas suas dependências *(que no python costumam ser muitas)*  ficam apenas num diretório específico. <br>
Logo, com uma venv você pode criar projetos que usam versões diferentes da mesma biblioteca sem que haja conflito na hora do import.

# Projeto x App
No django cada **project** pode carregar múltiplos **apps**, como um projeto site de esportes que pode ter um app para os artigos, outro para rankings etc.<br>
Ainda no terminal usamos os comandos a seguir para criar o project **library** que vai carregar nosso app **books**. 

```bash
>django-admin startproject library . #ponto indica diretório atual
>django-admin startapp books
>python manage.py runserver #pra levantarmos o servidor local com a aplicação
```
Sua estrutura de pastas deve estar assim:

![imagem da estrutura](img/imagem-estrutura.jpg)

Para criar as tabelas no banco de dados (Por enquanto *Sqlite3*) executamos o comando
```bash
>python manage.py migrate
```
Isso evita que a notificação *unapplied migrations* apareça na próxima vez que você levantar o servidor 

![imagem unapplied](img/18unapplied.png)

# Criando os modelos e API
No arquivo **./library/settings.py** precisamos indicar ao nosso projeto library sobre a existência do app books e também o uso do rest framework. Portanto adicionamos as seguintes linhas sublinhadas

![imagem das linhas](img/library_settings.jpg)

Já que nossa API suporta imagens como atributos também sera necessário o seguite acrescimo de codigo em **./library/settings.py**
```py
MEDIA_URL = '/media'
 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

Agora em **./library/books/models.py** iremos criar nosso modelo com os atributos que um livro deve ter.

```py
from django.db import models
from uuid import uuid4

#funcao pra receber as imagens e gerar endereço
def upload_image_books(instance, filename):
    return f"{instance.id_book}-{filename}"

class Books(models.Model):
    #criando os atributos do livro
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year = models.IntegerField()
    image = models.ImageField(upload_to=upload_image_books, blank=False, null=True)
```
## Serializers e Viewsets
Dentro de **./library/books** iremos criar a pasta **/api** com os arquivos 
* serializers.py 
* viewsets.py 

### Serializers
```py
from rest_framework import serializers
from books import models

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Books
        fields = '__all__' #todos os campos do model id_book, author..
```

### Viewsets
```py
from rest_framework import viewsets
from books.api import serializers
from books import models

class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BooksSerializer
    queryset = models.Books.objects.all() #tambem todos os campos do nosso modelo
```
# Criação das rotas
Agora com o viewset e o serializer a única coisa que falta é uma rota. Portanto vamos para **./library/urls.py** resolver esse problema

```py
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers
from books.api import viewsets as booksviewsets
#criando nosso objeto de rota
route = routers.DefaultRouter()
route.register(r'books', booksviewsets.BooksViewSet, basename="Books")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
Como criamos um modelo novo lá em cima, precisamos avisar e em seguida migrar todos essas novas informações para o banco de dados

```bash
>python manage.py makemigrations 
>python manage.py migrate
>python manage.py runserver 
```
Agora você pode usar um programa como <a href="https://insomnia.rest/">Insomnia</a> para testar os métodos http no link do seu servidor local. 🥰

![insomnia](img/insomnia.png)

>O python facilita bastante coisas para a gente, como os serializers (que convertem objetos para strings na comunicação cliente-servidor) e os verbos http (GET, POST, PUT, DELETE) que de certa forma também vem por padrão. Não me aprofundei neles durante o readme porque também preciso entender melhor como essas coisas funcionam

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