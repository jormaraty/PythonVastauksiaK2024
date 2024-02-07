# luodaan tyhjä joukko nimiä varten
nimet = set()

# kysytään käyttäjältä nimiä, kunnes saadaan tyhjä
# Jokaisen nimen jälkeen tulostetaan joko
# 'uusi nimi' tai 'nimi on jo annettu'.
# Muista lisätä uusi nimi joukkoon.

# annan muuttujalle 'name' sellaisen alkuarvon,
# jolla pääsen varmasti while toistoon
name = "dummy"      # tämä ei talletu joukon alkioksi

while name != "":
    # kysy käyttäjältä nimi
    name = input("Anna nimi: ")
    # testaa, onko annettu nimi jo joukossa
    if name in nimet:
        print("nimi on jo annettu")
    else:
        # lopetusmerkkiä ei lisätä listaan
        if name != "":
            print("Uusi nimi")
            # muista lisätä uusi nimi joukkoon
            nimet.add(name)
    # tästä siirrytään testaamaan while-ehtoa

# while-toisto on päättynyt.
print("- tulostan kaikki joukossa olevat alkiot -")
# Tulostan nyt kaikki joukon alkiot yksitellen allekkain
# käytän  for..in -tekniikkaa.
# muuttujan 'nimi' saa itse keksiä vapaasti
for nimi in nimet:
    print(nimi)
