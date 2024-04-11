'''
    Funktio saa parametrina kokonaisluvun.
    Funktio palauttaa tiedon (true/false),
    että oliko saatu parametri alkuluku vai ei
'''

def alkuluku(tutkittava):
    # alkuoletus: 'tutkittava' on alkuluku
    onAlku = True

    # käydään jokainen luku väliltä 2 ... (tutkittava -1) läpi
    for jakaja in range(2, tutkittava):
        # onko 'tutkittava' jaollinen jakajalla?
        if tutkittava % jakaja == 0:
            # oli jaollinen -> ei ole alkuluku
            onAlku = False
            # lopetetaan tutkiminen saman tien
            break

    # palautetaan saatu tieto: onko alkuluku vai ei? (True/False)
    return onAlku
