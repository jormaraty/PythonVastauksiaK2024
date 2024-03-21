# määritellään Auto-luokka
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


# - pääohjelma -
# Luodaan uusi Auto-tyyppinen olio, jonka nimeksi annetaan ekaAuto.
# Uuden olion luonti vaatii 2 parametria: rekisterinumero ja huippunopeus.
ekaAuto = Auto("ABC-123", 142)

# testataan kulje-metodia
ekaAuto.kiihdyta(60)        # auton nopeus on 60 km/h
ekaAuto.kulje(1.5)          # ajetaan 1,5 tuntia

print(f"Auto on kulkenut 1,5 tunnin ajon jälkeen: {ekaAuto.matka} km.")


