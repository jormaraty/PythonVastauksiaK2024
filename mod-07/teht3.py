# Suomen lentoasemien koodeja löytyy esimerkiksi
# https://fi.wikipedia.org/wiki/Suomen_lentoasemat_ja_-paikat

# Tehdään uusi sanakirja lentoasemista.
# Avaimena on kentän ICAO, ja arvona lentoaseman nimi.
# Sijoitetaan sanakirjaan aluksi yksi alkio (Helsinki-Vantaan lentoasema)
airports = { "EFHK" : "Helsinki-Vantaan lentoasema"}

# Ohje käyttäjälle, valintaa 4 ei vaadittu tehtävässä
print("1 = haku, 2 = kentän lisäys, 3 = lopetus, 4 = tulosta kaikki kentät")
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

    elif toiminto == 2:
        # uuden lentoaseman lisääminen
        # kysytään aluksi uuden lentoaseman tiedot
        koodi = input("Anna uuden lentoaseman ICAO-koodi: ")
        nimi = input("MIkä on uuden lentoaseman nimi: ")
        # lisätään uuden lentoaseman tiedot sanakirjaan
        airports[koodi] = nimi
        print("Uusi lentoasema on lisätty.")

    elif toiminto == 3:
        # lopetus
        # elif-haara vaatii jonkin suorituslauseen, pass on ns. 'tyhjä lause', se ei tee mitään.
        pass

    elif toiminto == 4:
        # tulostetaan kaikki alkiot (avain ja arvo) sanakirjasta, xtra toiminto
        print("Sanakirjan kaikki tiedot: ")
        for avain in airports:
            # muuttujaan 'avain' tulee yksitellen kaikki sanakirjan avaimet
            print(f"{avain} : {airports[avain]}")

    else:
        # väärä valinta
        print("Virheellinen valinta.")

    # Ohje käyttäjälle (\n = rivin vaihto), tulostetaan joka toiminnon jälkeen
    print("\n1 = haku, 2 = kentän lisäys, 3 = lopetus, 4 = tulosta kaikki kentät")
    # kysytään käyttäjältä toiminto
    toiminto = int(input("Valitse toiminto: "))

# while-toisto on loppunut
print("Lopetit ohjelman käytön, hyvää päiväjatkoa!?!")

