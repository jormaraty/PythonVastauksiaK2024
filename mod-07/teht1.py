# Tehdään monikko, joka sisältää eri vuodenaikojen nimet.
# Monikko on aina vakio eli sitä ei voi muokata.
vuodenajat = ('kevät', 'kesä', 'syksy', 'talvi' )

# kysytään käyttäjältä kuukauden numero (1 = tammikuu, 12 = joulukuu)
nro = int( input("Anna kuukauden numero: "))

# Kevät on kuukaudet 3..5, kesä 6..8, syksy 9..11, talvi = 1,2 tai 12

# Määritellään kuukauden avulla, mikä monikon 'vuodenajat'
# alkio (vuodenaika) valitaan.
if nro >= 3 and nro <= 5:
    print(f"vuodenaika on: { vuodenajat[0] }")
elif 6 <= nro <= 8:     # lyhennys normaalista 2 eri ehdon yhdistelmästä
    print(f"vuodenaika on: {vuodenajat[1]}")
elif nro >= 9 and nro <= 11:
    print(f"vuodenaika on: {vuodenajat[2]}")
# nyt tulee hankalampi vertailu, sulut (ehkä) selkeyttävät ehtoa
# sanallisesti: (jos nro on välillä 1 ... 2) tai nro on 12
elif (nro >= 1 and nro <= 2)  or nro == 12:
    print(f"vuodenaika on: {vuodenajat[3]}")
else:
    # nro ei ole välillä 1..12
    print("Kuukauden numero ei ole kelvollinen")



