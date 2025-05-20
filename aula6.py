from math import sqrt
co = float(input('Digite quande mede o cateto oposto:'))
ca = float(input('Digite quanto mede o cateto adjacente:'))
h = sqrt((co ** 2) + (ca ** 2))
print(
    f'Se o CO for {co} e o CA for {ca} a hipotenusa desse triangulo retangulo mede {h:.2f}')
