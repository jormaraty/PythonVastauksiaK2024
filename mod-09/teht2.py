# määritellään Auto-luokka
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        # alla olevia ominaisuuksia ei voi asettaa oliota luodessa
        self.nopeus = 0         # tämän hetken nopeus
        self.matka = 0          # auton kulkema matka

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

    
# - pääohjelma -
# Luodaan uusi Auto-tyyppinen olio, jonka nimeksi annetaan ekaAuto.
# Uuden olion luonti vaatii 2 parametria: rekisterinumero ja huippunopeus.
ekaAuto = Auto("ABC-123", 142)

# tulostetaan luodun olion kaikki ominaisuudet
print("Auton tiedot")
print(f"rekkari: {ekaAuto.rekisteritunnus}")
print(f"huippunopeus: {ekaAuto.huippunopeus}")
print(f"nopeus nyt: {ekaAuto.nopeus} ja kuljettu matka: {ekaAuto.matka}")

# kiihdytetään autoa
ekaAuto.kiihdyta(30)
ekaAuto.kiihdyta(70)
ekaAuto.kiihdyta(50)
# tulostetaan auton nykyinen nopeus
print(f"Auton nopeus kiihdytysten jälkeen: {ekaAuto.nopeus}")

# hätäjarrutus
ekaAuto.kiihdyta(-200)
# tulostetaan auton nykyinen nopeus
print(f"Auton nopeus hätäjarrutuksen jälkeen: {ekaAuto.nopeus}")

