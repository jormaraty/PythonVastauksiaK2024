# if - elif - else rakenne.

# Suoritetaan korkeintaa yksi if tai elif
# ehtojen lohkoista (sisennetyt rivit).
# Else-osa ei ole pakollinen.

ika = int( input("Anna ikäsi: "))

# luokitellaan ihmiset iän mukaan (ikärasismia?)
if ika >= 40:
    print("Olet kalkkis")
elif ika >= 25:
    print("Alkaako ikä painaa? ")
elif ika >= 18:
    print("Hottis!!!")
else:
    # tänne tullaan vain, jos mikään edellä
    # olevista ehdoista ei ole totta.
    print("Olet siis alaikäinen")

print("Mutta ikähän on vain pelkkä numero!")

