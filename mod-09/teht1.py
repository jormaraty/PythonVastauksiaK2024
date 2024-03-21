# määritellään Auto-luokka
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        # alla olevia ominaisuuksia ei voi asettaa oliota luodessa
        self.nopeus = 0         # tämän hetken nopeus
        self.matka = 0          # auton kulkema matka


# - pääohjelma -
# Luodaan uusi Auto-tyyppinen olio, jonka nimeksi annetaan ekaAuto.
# Uuden olion luonti vaatii 2 parametria: rekisterinumero ja huippunopeus.
ekaAuto = Auto("ABC-123", 142)

# tulostetaan luodun olion kaikki ominaisuudet
print("Auton tiedot")
print(f"rekkari: {ekaAuto.rekisteritunnus}")
print(f"huippunopeus: {ekaAuto.huippunopeus}")
print(f"nopeus nyt: {ekaAuto.nopeus} ja kuljettu matka: {ekaAuto.matka}")
