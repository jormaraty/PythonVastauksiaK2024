# Suomen lentoasemien koodeja löytyy esimerkiksi
# https://fi.wikipedia.org/wiki/Suomen_lentoasemat_ja_-paikat

# Tehdään uusi sanakirja lentoasemista.
# Avaimena on kentän ICAO-koodi, ja arvona lentoaseman nimi.
# Sijoitetaan sanakirjaan aluksi yksi alkio (Helsinki-Vantaan lentoasema)
airports = { "EFHK" : "Helsinki-Vantaan lentoasema"}

# Ohje käyttäjälle
print("1 = haku, 2 = kentän lisäys, 3 = lopetus")
# kysytään käyttäjältä toiminto
toiminto = int( input("Valitse toiminto: "))

# toistetaan, kunnes käyttäjä lopettaa (toiminto 3)
while toiminto != 3:
    if toiminto == 1:
        # hakutoiminto
        avain = input("Anna kentän ICAO-koodi: ")
        # testataan löytyykö icao-koodi sanakirjasta
        if avain in airports:
            print(f"Lentoaseman nimi: {airports[avain]}")
        else:
            print("Koodillasi ei löytynyt lentokenttää")

    # TODO: tee uuden kentän lisäys

    # Ohje käyttäjälle (\n = rivin vaihto)
    print("\n1 = haku, 2 = kentän lisäys, 3 = lopetus")
    # kysytään käyttäjältä toiminto
    toiminto = int(input("Valitse toiminto: "))

# while-toisto on loppunut
print("Lopetit ohjelman käytön, hyvää päiväjatkoa!")

