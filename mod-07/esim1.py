# määritellään monikko (tuple) eri palkkatasoja varten (vakio, ei voi muokata)
palkkaluokat = ("pieni", "keskitasoa", "iso", "tosi iso")

# kysytään käyttäjän palkka
palkka = int( input("Paljonko saat palkkaa: "))

# määritellään eri palkkatasojen rajat
# pieni = alle 1800, keskitasoa = 1800..2500,
# iso = yli 2500 ... 4000, tosi iso = yli 4000

# annetaan käyttäjälle vastaus
if palkka < 1800:
    print(f"Palkkasi on { palkkaluokat[0] }")
elif palkka >= 1800 and palkka <= 2500:
    print(f"Palkkasi on {palkkaluokat[1]}")
elif 2500 < palkka <= 4000:
    print(f"Palkkasi on { palkkaluokat[2] }")
else:
    print(f"Palkkasi {palkka} on {palkkaluokat[3]}")
