# Funktio saa parametrina (alkuarvona) listan kokonaislukuja.
# Funktio laskee listassa olevien lukujen summan.
# Tässä versiossa käytetään listan valmista sum()-metodia.
# Funktio palauttaa lukujen summan.
def summaa(lista):
    # lasketaan listan alkioiden summa
    summa = sum(lista)
    # palautetaan saatu summa
    return summa



# - pääohjelma, sama kuin tehtävässä 4a -
# Laiskottaa: ei kysytä lukuja käyttäjältä vaan annetaan
# itse keksityt arvot listalle samalle kun se luodaan.
luvut = [1, 3, 5, 7, 9]

# kutsutaan funktiota, se vaatii parametriksi listan kokonaislukuja.
# Otetaan funktion palauttama arvo talteen muuttujan 'vastaus' arvoksi
vastaus = summaa(luvut)

# tulostetaan funktion palauttama arvo
print(f"Listassa olevien lukujen summa = {vastaus}")
