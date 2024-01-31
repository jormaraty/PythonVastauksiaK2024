# kysytään käyttäjältä nimiä ja
# talletetaan ne listaan

# teen tyhjän listan
nimet = []

# kysytään eka nimi
name = input("Anna eka nimi: (Enter lopettaa: ")

# while-toisto jatkuu, kunnes saadaan tyhjä merkkijono
while name != "":
    # lisätään saatu nimi listan loppuun
    nimet.append(name)
    # HUOM: muista kysyä uusi nimi
    name = input("Anna seuraava nimi (Enter lopettaa: ")

# len() palauttaa listan pituuden
print(f"Annoit { len(nimet) } kpl nimiä: ")
print(nimet)    # tulostaa koko listan sisällön

# lajitellaan nimet aakkosjärjestykseen
nimet.sort()
print("Nimet aakkosjärjestyksessä: ")
print(nimet)

# muokataan listan toisen alkion sisältöä (huom. indeksin numero)
nimet[1] = 'Toka'
# tulostetaan muokatun listan sisältö
print(nimet)




