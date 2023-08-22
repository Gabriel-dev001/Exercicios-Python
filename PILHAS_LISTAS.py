class Pilha(object):
    def __init__(self):
        self.dados = []

    def Empilha(self, elemento):
        self.dados.append(elemento)

    def Desempliha(self):
        return self.dados.pop(-1) #ESSE MENOS UM É A FORMA PYTHONICA DE SE REFERIR AO ULTIMO INDICE DO VETOR.
    
class Fila(object):
    def __init__(self):
        self.dados = []

    def Inserir(self, elemento):
        self.dados.append(elemento)

    def Retirar(self):
        return self.dados.pop(0)