# if - else rakenne

# Vain täysi-ikäinen pääsee bileisiin.
# Tämä on ns. joko-tai rakenne, eli
# aina suoritetaan jompi kumpi haara (if tai else)

ika = int( input("Anna ikäsi: "))

if ika >= 18:
    # jos if-ehto-oli totta, tullaan tähän lohkoon.
    print("Tervetuloa bileisiin!")
else:
    # if-ehto ei ollut totta, jos tänne tullaan
    print("Go home, baby!")

# tämä rivi suoritetaan aina
print("Hyvää päivän jatkoa!")


