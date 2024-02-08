'''
    Tässä on toinen ratkaisu tehtävään 1.
    Tässä versiossa annetaan muuttujalle 'silmaluku'
     sopiva arvo ennen while-toistoa.
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

# muuttuja, johon otetaan talteen funktion palauttama arvo.
# Annetaan nyt muuttujalle sellainen alkuarvo, että se menee varmasti toistorakenteeseen.
silmaluku = 0

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