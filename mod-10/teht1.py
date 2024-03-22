'''
    Määritellään Hissi-luokka
'''
class Hissi:
    def __init__(self, alin_kerros, ylin):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin
        # missä kerroksessa myt ollaan?
        self.kerros = alin_kerros       # hissi on aluksi aina alimmassa kerroksessa

    # hissi siirtyy haluttuun kerrokseen
    def siirry_kerrokseen(self, tavoite):
        # siirrytäänkö ylöspäin?
        if tavoite > self.kerros:
            # niin kauan kun ollaan liian alhalla, niin siirrytään 1 kerros ylöspäin
            while self.kerros < tavoite:
                self.kerros_ylos()
        # siirryttänkö alaspäin?
        elif tavoite < self.kerros:
            while self.kerros > tavoite:
                self.kerros_alas()

        print("* Hissi on halutussa kerroksessa *")
        return

    # hissi siirtyy yhden kerroksen ylöspäin
    def kerros_ylos(self):
        # tässä oletetaan ettei hissi voi nousta liian ylös
        self.kerros = self.kerros + 1
        print(f"Hissi on kerroksessa {self.kerros}")
        return

    # hissi siirtyy yhden kerroksen alaspäin
    def kerros_alas(self):
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