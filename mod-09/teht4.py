'''
    Auto-luokka on kopioitu sellaisenaan tehtävästä 3.
'''

import random       # kirjasto satunnaislukujen arvontaan

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        # alla olevia ominaisuuksia ei voi asettaa oliota luodessa
        self.nopeus = 0  # tämän hetken nopeus
        self.matka = 0  # auton kulkema matka

    def kiihdyta(self, muutos):
        # muutetaan auton nopeutta
        self.nopeus = self.nopeus + muutos
        # nopeus ei saa nousta yli huippunopeuden
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        # nopeus ei saa mennä negatiiviseksi
        if self.nopeus < 0:
            self.nopeus = 0
        return

    def kulje(self, aika):
        # lisätään auton kulkemaa matkaa
        self.matka += self.nopeus * aika
        return


# autokilpailu (pääohjelma)

# luodaan tyhjä lista, johon tulee myöhemmin 10 kpl kilpa-autoja
autot = []

# luodaan 10 autoa, ja lisätään ne listaan
for nro in range(1, 11):
    # nro saa arvot 1, 2, 3, .. 10
    rekkari = "ABC-" + str(nro)
    maxnopeus = random.randint(100, 200)    # arvotaan väliltä 100 .. 200
    # luodaan uusi Auto-tyyppinen olio ja lisätään se autot-nimiseen listaan
    kilpuri = Auto(rekkari, maxnopeus)
    autot.append(kilpuri)

# alustetaan kilpailun arvoja
kesto = 0           # kuinka monta tuntia on kilpailtu
tavoite = 10000     # kuinka monta km on kilpailun pituus
jatkuu = True       # jatkuuko kilpailu(k/e)

while jatkuu:
    # lyhennus lausekkeesta 'while jatkuu == True'

    # käydään jokainen listan auto läpi
    for kilpailija in autot:
        muutos = random.randint(-10, 15)        # arvotaan nopeuden muutos -10 .. 15
        kilpailija.kiihdyta(muutos)                # auto muuttaa nopeutta
        kilpailija.kulje(1)                        # kuljetaan 1 tunti uudella opeudella
        # onko kilpailija päässyt maaliin?
        if kilpailija.matka >= tavoite:
            jatkuu = False                  # kilpailu loppuu, jos päästiin maaliin

    # lisätään kilpailuun käytettyä aikaa tunnilla
    kesto += 1

# kilpailu on ohi, kerrotaan tulokset
print(f"Kilpailu päättyyi, se kesti {kesto} tuntia")

# \t on tab eli sarkainnäppäin
print("Rekkkari\t huippunopeus\t nopeus\t kuljettu matka")
# käydään listn kaikki autot läpi
for kaara in autot:
    # termillä ':15d' numero tulostetaan 15 merkkiä leveään kenttään
    print(f"{kaara.rekisteritunnus:10s} {kaara.huippunopeus:10d} {kaara.nopeus:10d} {kaara.matka:12d}")

# huom: autot saisi järjestettyä myös kuljetun matkan mukaan, mutta ei nyt jaksanu..