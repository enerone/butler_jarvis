import requests

def getComuna(calle, numero):
    response = requests.get("https://ws.usig.buenosaires.gob.ar/datos_utiles?calle=" +calle+ "&altura=" + numero)
    data = response.json()
    return(data['comuna'])

print(getComuna('Argerich', '5600'))