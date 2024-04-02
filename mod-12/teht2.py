# Tässä on vain ratkaisun runko (ope yrittää kovasti ratkaista tehtävää, ehkä ;)

# Tämä ratkaisu on muokattu noudattamaan teoriassa esitettyä tapaa.
# Joudut tekemään itsellesi palveluunoman API-avaimen, se on ilmainen.
# Ks. https://home.openweathermap.org/users/sign_in
# Keväällä 2024 väliaikaisesti toimii myös open temp-avain: d5617b002ed2b89c33043122a30586b8

# tämä kirjasto sisältää nettihakujen tarvitsemia toimintoja
import requests


# kysytään käyttäjältä haun tarvitsemat lähtötiedot
hakusana = input("Anna hakusana: ")

# Pyynnön malli: https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# Huom: kun lisäät todellisen hakuehdon, niin poista myös sulut { }, esim. q={city name} => q=helsinki
# Nettiin lähetettävä lopullinen hakulause
pyyntö = "tähän_tulee_lopullinen_hakulause"

# Debug: tulostetaan lopullinen hakulause testausvaiheessa.
# Vinkki: kopioi hakulause selaimeen ja katso toimiiko se.
# Voit poistaa tämän, kun homma pelittää...
print(pyyntö)

try:
    # haetaan netistä json-muotoinen data, otetaan se vastaan sellaisena ('raakadata')
    vastaus = requests.get(pyyntö)
    # tarkistetaan että onnistuiko hakuoperaatio (200 = ok)
    if vastaus.status_code==200:
        # jos haku onnistui, niin muutetaan saatu data Pythonin sanakirja-muotoon
        sanakirja_vastaus = vastaus.json()
        # json-datan käsittely tähän
except requests.exceptions.RequestException as e:
    # tänne tullaan, jos hakutapahtumassa tuli poikkeustilanne (virhe)
    print ("Hakua ei voitu suorittaa.")

# tämä tulostetaan aina, onnistuiko datan haku tai ei
print("Hakutapahtuma on ohi.")