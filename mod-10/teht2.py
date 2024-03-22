'''
    Määritellään Hissi-luokka.
    Tämä on nyt kopio tiedostosta teht1b
'''
class Hissi:
    def __init__(self, alin_kerros, ylin):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin
        # missä kerroksessa myt ollaan?
        self.kerros = alin_kerros       # hissi on aluksi aina alimmassa kerroksessa

    # hissi siirtyy haluttuun kerrokseen
    def siirry_kerrokseen(self, tavoite):
        # toistetaan, kunnes ollaan halutussa kerroksessa
        while self.kerros != tavoite:
            if tavoite > self.kerros:
                # ollaan tavoitteen alapuolella
                self.kerros_ylos()
            elif tavoite < self.kerros:
                self.kerros_alas()

        print("* Hissi on halutussa kerroksessa *")
        return

    # hissi siirtyy yhden kerroksen ylöspäin
    def kerros_ylos(self):
        # siirrytään ylöspäin vain jos ei olla ylimmässä kerroksessa
        if self.kerros < self.ylin_kerros:
            self.kerros = self.kerros + 1
        print(f"Hissi on kerroksessa {self.kerros}")
        return

    # hissi siirtyy yhden kerroksen alaspäin
    def kerros_alas(self):
        # siirrytään alaspäin vain ei olla alimmassa kerroksessa
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
        print(f"Hissi on kerroksessa {self.kerros}")
        return


'''
    Määritellään Talo-luokka
'''
class Talo:
    def __init__(self, alin_kerros, ylin, lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin
        self.hissien_lkm = lkm
        self.hissit = []        # tyhjä lista talon hissejä varten
        # luodaan talon hissit ja lisätään ne hissit-listaan.
        for nro in range(lkm):
            # luodaan uusi hissi
            uusiHissi = Hissi(self.alin_kerros, self.ylin_kerros)
            # lisätään luotu olio hissit-listaan
            self.hissit.append(uusiHissi)

    def aja_hissia(self, hissin_nro, kohdekerros):
        # sopimus: hissit numeroidaan 1, 2, 3, ...
        # etsitään oikea hissi, siitä tulee Hissi-tyyppinen olio
        # huom: hissit-listan indeksointi alkaa nollasta.
        ajettavaHissi = self.hissit[hissin_nro - 1]
        # ajetaan hissi kohdekerrokseen
        ajettavaHissi.siirry_kerrokseen(kohdekerros)


# - pääohjelma -
# luon uuden talon, 3 kpl hissejä
ekaTalo = Talo(1, 5, 3)
# ajetaan eka hissi 3. kerrokseen
ekaTalo.aja_hissia(1, 3)
# ajetaan toka hissi kerrokseen 4
ekaTalo.aja_hissia(2, 4)

# testaus: tulostetaan talon kaikkien hissien sijainnit.
for tutkittava_hissi in ekaTalo.hissit:
    print(f"Hissi on kerroksessa {tutkittava_hissi.kerros} ")
