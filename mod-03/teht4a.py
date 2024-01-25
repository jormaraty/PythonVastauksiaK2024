# Karkausvuosi vai ei?

vuosi = int( input("Anna vuosiluku: "))

# Jos vuosi on jaollinen 400:lla -> ON karkausvuosi
if vuosi % 400 == 0:
    print("ON karkausvuosi")
# muuten jos vuosi on jaollinen 100:lla -> EI ole karkausvuosi
elif vuosi % 100 == 0:
    print("EI ole karkausvuosi")
# TODO: koodaa loppuun itse
# muuten jos vuosi on jaollinen 4:llä -> ON karkausvuosi

# muuten, EI ole karkausvuosi

# Testiarvot: 1900 -> EI, 2000 -> ON, 2023 -> EI, 2024 -> ON