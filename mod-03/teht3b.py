# Hemoglobiiniarvon tarkastelua.
# Nyt käytetään hyväksi loogisia operaattoreita (and, or)

# kysytään käyttäjältä lähtöarvot
sukup = input("Oletko nainen vai mies (N/M) ")
hgb = int( input("Anna hemoglobiiniarvosi: ") )

# Huomaa, muista tarkistaa kaikki eri vaihtoehdot.
# Muista myös testata ns. sauma-arvot eli naisilla 117 ja 175

# tarkastellaan kaikki eri naisen hgb arvot
if sukup == "N" and hgb < 117:
    print("Nainen, hemoglobiiniarvosi on liian alhainen")
elif sukup == "N" and hgb >= 117 and hgb <= 175:
    print("Nainen, hemoglobiiniarvosi on normaali")
elif sukup == "N":
    print("Nainen, hemoglobiiniarvosi on korkea")
elif sukup == "M" and hgb >= 134:
    print("Mies, hemoglobiiniarvosi ei ole ainakaan liian matala")
# TODO: koodaa miehen tarkastelu itse, muista myös testata!
else:
    print("Jotain meni pieleen...")