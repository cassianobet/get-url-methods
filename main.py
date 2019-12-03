from ExtratoArgumentos import ExtratoArgumento

'''
url = "pagina?argumentos"
indice = url.find("?")
print(url[indice + 1: )
'''
url = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=700"

argumentosUrl = ExtratoArgumento(url)
moedaOrigen, moedaDestino = argumentosUrl.extraiArgumentos()
print(moedaOrigen, moedaDestino)
