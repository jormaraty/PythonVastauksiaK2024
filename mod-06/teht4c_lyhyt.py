# Tässä on käytetty ns. pikakoodausta.
# Koodirivien määrä on pieni, koodin ymmärtäminen aluksi on hieman haastavaa.

def pika_summaa(lista):
    # lyhyt versio:
    # Suoritetaan ensin toiminto 'sum(lista)', joka palauttaa listan alkioiden summan.
    # Saatu tulos palautetaan saman tien kutsujalle
    return sum(lista)


# - pääohjelma -
# Laiskottaa: ei kysytä lukuja käyttäjältä vaan annetaan
# itse keksityt arvot listalle samalle kun se luodaan.
luvut = [1, 3, 5, 7, 9]

# lyhyt versio
# Aluksi suoritetaan sulkujen {} sisällä oleva lauseke 'pika_summaa(luvut)'.
# Saatu tulos (25) sijoitetaan tulostettaessa edellä mainitun lausekkeen paikalle
print(f"Listassa olevien lukujen summa: { pika_summaa(luvut)}")
