# Vuorovaikutteinen ohjelma

# input pysäyttää ohjelman ja odottaa käyttäjän vastausta
nimi = input("Anna nimesi: ")
# muuttujan arvo tulostetaan kahden merkkijonon väliin
print("Moi " + nimi + ", mitä kuuluu?")

# input lukee kaikki arvot merkkijonona
ikaStr = input("Mikä on henkinen ikäsi? ")     # ikaStr on merkkijono

# muutetaan saatu arvo numeroksi muuttujaan ika
ika = int(ikaStr)
# lisätään muuttujan 'ika' arvoa yhdellä
ika = ika + 1

print(nimi + " onko henkinen ikäsi vuoden kuluttua " + str(ika) + " vuotta?")



