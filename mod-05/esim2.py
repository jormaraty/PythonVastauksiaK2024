# range-funktio ja for-toisto

# tulostan parilliset luvut väliltä 10 .. 20
for nro in range(10, 21, 2):
    # muuttuja nro saa arvot väliltä 10 ..21
    # Huom: alkuarvo 10 otetaan mukaan, loppuarvo 21 EI.
    # Muuttujan nro kasvatetaan arvolla 2.
    print(nro)

# tulostan kaikki kokonaisluvut väliltä 5 .. 10  (huom. loppuarvo 11)
for nro in range(5, 11):
    # oletusarvo 3. parametrille on 1 (ei ole pakko antaa)
    print(nro)

# teen toiston 4 kertaa
for nro in range(4):
    # Vain 1 parametri -> se on loppuparametri.
    # Alkuarvo on oletuksena 0, lisäys oletuksena 1
    
    # Nyt siis muuttuja nro saa arvot 0, 1, 2, 3
    print("Hei")
