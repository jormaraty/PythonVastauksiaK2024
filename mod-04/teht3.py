'''
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
'''

import math

'''
Havaitaan ongelma: kun käyttäjä antaa lopetusmerkin 
eli pelkän Enter. Jos tätä yritetään muuntaa numeroksi, niin
python kaatuu.
Nyt meidän on pakko kysyä kaikki arvot merkkijojoina.
'''

# alkuarvot pienimmälle ja suurimmalle arvolle.
pienin = math.inf       # aluksi pienin = äärettömän suuri
suurin = -math.inf

# kysytään eka arvo merkkijonona (lopetusmerkin takia)
lukuStr = input("Anna luku, tyhjä lopettaa: ")

# toistetaan lukujen kysymistä, kunnes käyttäjä antaa tyhjän merkkijonon
while lukuStr != "":
    # muutetaan saatu merkkijono desimaaliluvuksi
    luku = float(lukuStr)
    # TODO: tarkista onko saatu luku pienin tai suurin tähänastisista
    # päivitä muuttujia pienin tai suurin tarvittaessa

    # Muista kysyä uusi arvo!

# TODO: tulostetaan suurin ja pienin käyttäjän antama arvo.
