# Funktio saa parametrina (alkuarvona) listan kokonaislukuja.
# Funktio laskee listassa olevien lukujen summan.
# Tässä versiossa lukujen summa lasketaan itse summaamalla arvoja.
# Funktio palauttaa lasketun summan
def summaa(lista):
    # alkuarvo listassa olevien lukujen summalle
    summa = 0
    # käydään listan jokainen alkio yksitellen läpi
    for luku in lista:
        # muuttuja luku sisältää yhden listassa olevista luvuista,
        # lisätään sen arvo muuttujaan summa
        summa += luku
    # palautetaan saatu summan arvo
    return summa


# - pääohjelma -
# Laiskottaa: ei kysytä lukuja käyttäjältä vaan annetaan
# itse keksityt arvot listalle samalle kun se luodaan.
luvut = [1, 3, 5, 7, 9]

# kutsutaan funktiota, se vaatii parametriksi listan kokonaislukuja.
# Otetaan funktion palauttama arvo talteen muuttujan 'vastaus' arvoksi
vastaus = summaa(luvut)

# tulostetaan funktion palauttama arvo
print(f"Listassa olevien lukujen summa = {vastaus}")
