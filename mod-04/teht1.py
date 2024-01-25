'''
Kirjoita while-toistorakennetta käyttävä ohjelma,
joka tulostaa kolmella jaolliset luvut väliltä 1..1000
'''

# muuttuja, joka saa kaikki arvot väliltä 1..1000
luku = 1

# tehdään while-toisto, jossa muuttuja
# 'luku' käy läpi kaikki arvot väliltä 1..1000
while luku <= 1000:
    if luku % 3 == 0:
        # muuttuja luku on jaollinen 3:lla,
        # jos tänne tullaan
        print(luku)
    # HUOM: muista kasvattaa muuttujan luku arvoa!!!
    luku = luku + 1

# tämä tulostetaan aina (jos ei jäädä ikuiseen silmukkaan :)
print("Huh huh, olipa siinä toistossa pyörimistä!!!")