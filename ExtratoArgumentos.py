class ExtratoArgumento:
    def __init__(self,url):                               # Metodo contrutor
        if self.urlEhValida(url):
            self.url = url
        else:
            raise LookupError("Url invalida")             # Retorna um erro para o usuário
    
    @staticmethod
    def urlEhValida(url):                                 # Metodo que valida URL                
        if url:
            return True
        else:
            return False

    def extraiArgumentos(self):

        buscaMoedaOrigem  = "moedaorigem" 
        buscaMoedaDestino = "moedadestino"

        indiceFinalMoedaOrigem    = self.url.find("&")
        indiceInicialMoedaOrigem  = self.encontraIndexInicial(buscaMoedaOrigem)

        indiceFinalMoedaDestino   = self.url.find("&",50)
        indiceInicialMoedaDestino = self.encontraIndexInicial(buscaMoedaDestino)

        

        moedaOrigen = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]
        moedaDestino = self.url[indiceInicialMoedaDestino:indiceFinalMoedaDestino]

        return moedaOrigen, moedaDestino

    def encontraIndexInicial(self,moedaBuscada):
        return self.url.find(moedaBuscada)+len(moedaBuscada)+1

