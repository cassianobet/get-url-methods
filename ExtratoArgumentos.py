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

        buscaMoedaOrigem  = "moedaorigem=" 
        buscaMoedaDestino = "moedadestino="

        indiceFinalMoedaOrigem    = self.url.find("&")
        indiceInicialMoedaOrigem  = self.encontraIndexInicial(buscaMoedaOrigem) 

        moedaOrigen = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

        if moedaOrigen == "moedadestino":
            self.trocaMoedaOrigem()
            indiceFinalMoedaOrigem    = self.url.find("&")
            indiceInicialMoedaOrigem  = self.encontraIndexInicial(buscaMoedaOrigem) 

            moedaOrigen = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]
            
        indiceInicialMoedaDestino = self.encontraIndexInicial(buscaMoedaDestino)
        moedaDestino = self.url[indiceInicialMoedaDestino:]

        return moedaOrigen, moedaDestino

    def encontraIndexInicial(self,moedaBuscada):
        return self.url.find(moedaBuscada)+len(moedaBuscada)

    def trocaMoedaOrigem(self):
        self.url = self.url.replace("moedadestino", "real", 1)
        print(self.url)

