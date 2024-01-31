# tehdään tyhjä lista numeroita varten
import random

numerot = []

# kysytään arpakuutioiden lkm
lkm = int( input("Kuinka monta noppaa: "))

# toistetaan noppien lkm kertaa
# aluksi while-toistolla
heitetty = 0        # aluksi ei ole heitetty kertaakaan

while heitetty < lkm:
    # heitä noppa, ota silmäluku talteen
    silmaluku = random.randint(1, 6)
    # tulostetaan heiton arvo toiminnan tarkistusta varten
    print(f"silmäluku: {silmaluku}")
    # lisää nopan silmäluku listaan
    numerot.append(silmaluku)
    # Muista lisätä heittyjen noppien lkm arvoa
    heitetty += 1   # heitetty = heitetty + 1

# olisiko listalla valmis summa toiminto?
summa = sum(numerot)    # olihan sillä!

# tulostetaan vastaus
print(f"Noppien summa: {summa}")

# TODO: tee vastaa ohjelma for-toiston avulla!

