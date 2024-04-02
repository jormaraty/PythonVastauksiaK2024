'''
    Määritellään Julkaisu-luokka.
    Luokalla on 1 ominaisuus: nimi
'''
class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


'''
    Määritellään Kirja-luokka, se periytyy luokasta Julkaisu.
    Kirja-luokalla on automaattisesti Julkaisu-luokan ominaisuus: nimi.
    Kirja-luokalla on lisäksi 2 uutta ominaisuutta: kirjoittaja ja sivumäärä.  
'''
class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivu_lkm):
        # kutsutaan yliluokan metodia, joka asettaa nyt ominaisuuden: nimi.
        super().__init__(nimi)
        # asetetaan luokan lisäominaisuudet
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivu_lkm

    def tulosta_tiedot(self):
        # metodi tulostaa luokan kaikki tiedot
        print("- Kirjan tiedot:")
        print(f"Nimi: {self.nimi}, kirjoittaja: {self.kirjoittaja}, sivuja: {self.sivumäärä}")


'''
    Määritellään Lehti-luokka, joka myös perityy Julkaisu-luokasta.
    Lehti-luokalla on 1 lisäominaisuus: päätoimittaja.
    Lisäksi luokka perii kaikki (nyt 1 kpl) yliluokan ominaisuudet.
'''
class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        # kutsutaan yliluokan metodia, joka asettaa nyt ominaisuuden: nimi.
        super().__init__(nimi)
        # asetetaan luokan lisäominaisuudet
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        # metodi tulostaa luokan kaikki tiedot
        print("- Lehden tiedot:")
        print(f"Nimi: {self.nimi}, päätoimittaja: {self.päätoimittaja}")


# -- pääohjelma --
# luodaan 2 julkaisua, 1 lehti ja 1 kirja

# luodaan Lehti-tyyppinen olio
lehtiA = Lehti("Aku Ankka", "Aki Hyyppä")
# luodaan Kirja-tyyppinen olio
kirjaB = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

# tulostetaan molempien olioiden kaikki tiedot
lehtiA.tulosta_tiedot()
kirjaB.tulosta_tiedot()

