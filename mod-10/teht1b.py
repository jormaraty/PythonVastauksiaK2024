'''
    Määritellään Hissi-luokka.
    Tässä versiossa metodi siirry_kerrokseen on koodattu hieman tehokkaammin.
    Metodeihin kerros_ylos ja kerros_alas on lisätty tarkistus ettei mennä rajojen yli.
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


# - pääohjelma -
# luon uuden hissin
ekaHissi = Hissi(1, 7)
# siirrytään kerrokseen 4
ekaHissi.siirry_kerrokseen(4)
# siirrytään takaisin alimpaan kerrokseen
ekaHissi.siirry_kerrokseen(1)