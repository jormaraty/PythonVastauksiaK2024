# Funktio saa yhden parametrin eli alkuarvon, gallonien määrän.
# Funktio palauttaa vastaavan litramäärän.
def muunna(gallons):
    # muunnetaan gallonat litroiksi
    litrat = 3.785 * gallons
    # palautetaan laskettu litramäärä
    return litrat

# - pääohjelma -

# kysytään käyttäjältä lähtötiedot,
# muunnetaan saatu tieto heti desimaaliluvuksi (float)
gallonat = float( input("Anna gallonien lkm: "))

# kutsutaan funktiota, se vaatii yhden parametrin.
# Funktion palauttama arvo otetaan talteen muuttujan 'vastaus' arvoksi
vastaus = muunna(gallonat)

# tulostetaan saatu vastaus 2:lla desimaalilla
print(f"{gallonat} gallonaa on {vastaus:.2f} litraa")