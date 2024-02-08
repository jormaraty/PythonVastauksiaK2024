'''
    Tässä on eka ratkaisu tehtävään 1.
    Tässä versiossa kutsutaan funktiota heita() kerran ennen while-toistoa.
'''

import random

# Funktio, joka arpoo satunnaisluvun väliltä 1..6,
# ja palauttaa saamansa luvun.
# Funktio ei tarvitse parametreja eli alkuarvoja -> tyhjät sulut ()
def heita():
    # arvotaan kokonaisluku väliltä 1 .. 6
    arvottu = random.randint(1,6)
    # palautetaan saatu arvo kutsujalle
    return arvottu

# -- pääohjelma alkaa --

# Kutsutaan funktiota kerran ennen while-toistoa.
# Funktion palauttama arvo otetaan telteen muuttujan 'silmäluku' arvoksi.
# Muuttujalla 'silmäluku' täytyy olla jokin arvo ennen while-ehtoa.
silmaluku = heita()
# tulostetaan saatu silmäluku
print(f"Nopan tulos: {silmaluku}")

# toistorakenne, joka päättyy vasta kun funktio palauttaa arvon 6
while silmaluku != 6:
    # kutsutaan funktiota heita(), otetaan vastaus talteen muuttujan
    # 'silmaluku' arvoksi
    silmaluku = heita()
    # tulostetaan saatu silmäluku
    print(f"Nopan tulos: {silmaluku}")
    # tästä palataan tarkistamaan while-ehtoa

# tänne päästään vasta kun while toisto on loppunut
print("Tulihan se kuutonen sieltä!")