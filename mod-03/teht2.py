# Sanallinen selitys hyttiluokalle

hytti = input("Anna hyttiluokka: ")

# Huom: hytti.lower() muuttaa kaikki käyttäjän antamat merkit pieniksi,
# esim. Lux -> lux.

if hytti.lower() == "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hytti == 'A' or hytti == 'a':
    print("A on ikkunallinen hytti autokannen yläpuolella")
elif hytti == "B" or hytti == "b":
    print("B on ikkunaton hytti autokannen yläpuolella")
elif hytti == 'C' or hytti == 'c':
    print("C on ikkunaton hytti autokannen alapuolella")
else:
    print("Virheellinen hyttiluokka")
