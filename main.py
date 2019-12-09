from ExtratoArgumentos import ExtratoArgumento

'''
url = "pagina?argumentos"
indice = url.find("?")
print(url[indice + 1: )
'''
url = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar"

argumentosUrl = ExtratoArgumento(url)
moedaOrigen, moedaDestino = argumentosUrl.extraiArgumentos()
print(moedaDestino, moedaOrigen)
