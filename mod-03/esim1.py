# ehtolause (if)

# kysytään käyttäjän ikä,
# muutetaan käyttäjän antama arvo heti kokonaisluvuksi
ika = int( input("Anna ikäsi: "))

if ika >= 18:
    # jos yllä oleva ehto on totta,
    # niin tullaan tähän lohkoon (block).
    print("Olet siis täysi-ikäinen,")
    print("lähdetkö kahville?")

# tämä koodi suoritetaan aina
print("Ohjelma loppui.")
