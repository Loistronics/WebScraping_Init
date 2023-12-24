import bs4 #Libreria que nos permite navegar por el contenido de la pagina
import requests
from pathlib import Path
import os

url = "https://books.toscrape.com/catalogue/page-{}.html"

libros_best_seller = []

contador = 0

for i in range(1,5):
    print(url.format(i))
    resultado = requests.get(url.format(i))
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
    libros = sopa.select('.product_pod')
    contador+=1
    directorio = Path(os.getcwd(), str(contador))
    for i in libros:
        if len(i.select('.star-rating.Four')) != 0 or len(i.select('.star-rating.Five')) != 0:
            if not Path.exists(directorio):
                os.mkdir(directorio)
            print(i.select('a')[1]['title'])
            titulo = i.select('a')[1]['title']
            libros_best_seller.append(titulo)
            imagen = requests.get('https://books.toscrape.com/' + i.select('img')[0]['src'])

            f = open(Path(directorio)/f'{titulo}.jpg','wb')
            f.write(imagen.content)
            f.close()








