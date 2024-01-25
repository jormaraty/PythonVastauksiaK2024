# Onko luku parillinen?

# Luvun jaollisuutta toisella tarkastellaan jakojäännös (%)
# eli modulo-operaattorilla.

luku = int( input("Anna jokin parillinen luku: "))

if luku % 2 == 0:
    # tänne päästään, jos käyttäjän luku on jaollinen 2:lla.
    print("Osasit!")

luku = int( input("Anna jokin parillinen luku, joka on jaollinen myös 7:llä: "))

if (luku % 2 == 0) and (luku % 7 == 0):
    print("Wau, osasit tämänkin")
else:
    print("Tämä ei nyt onnistunut")


