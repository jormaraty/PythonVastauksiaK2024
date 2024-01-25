# Hemoglobiiniarvon tarkastelua

# kysytään käyttäjältä lähtöarvot
sukup = input("Oletko nainen vai mies (N/M)")
hgb = int( input("Anna hemoglobiiniarvosi: ") )

# jaetaan tarkastelu erikseen naisiin ja miehiin
if sukup == "N":
    if hgb < 117:
        print("Nainen, hemoglobiiniarvosi on liian alhainen")
    elif hgb > 175:
        print("Nainen, hemoglobiiniarvosi on liian korkea")
    else:
        print("Nainen, hemoglobiiniarvosi on normaali")
elif sukup == "M":
    # TODO: koodaa itse
    print("Käytetään miesten raja-arvoja")
else:
    print("Tuntematon sukupuoli")


