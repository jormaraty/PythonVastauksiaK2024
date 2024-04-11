# ladataan päätepisteen vaatimat palikat mukaan
from flask import Flask
# ladataan oma apufunktio mukaan
from apufunktiot import alkuluku

app = Flask(__name__)
@app.route('/alkuluku/<int:luku>')
def onko_alkuluku(luku):
    # tutkitaan onko parametri alkuluku vai ei?
    # <int:luku> kertoo että parametri 'luku' luetaan kokonaislukuna.

    # varsinainen logiikka sijaitsee toisessa tiedostossa,
    # funktio 'alkuluku' palauttaa True/False
    tulos = alkuluku(luku)

    # määritellään web-sivulle palautettava json-data
    vastaus = {
        "Number": luku,
        "isPrime": tulos
    }

    # palautetaan saatu json-data kutsujalle (selaimelle)
    return vastaus

# alla määritellään, että tämä päätepiste käyttääkin porttia 3001
# -> kutsu oltava esim. http://127.0.0.1:3001/alkuluku/31
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3001)

