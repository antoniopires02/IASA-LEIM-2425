from mod.estado import Estado

"""
Classe que representa o estado do agente, contendo a sua posição no ambiente. Esta classe herda da classe base Estado,
e utiliza o método hash para gerar um identificador único do estado, facilitando a sua gestão e comparação no sistema.
"""

class EstadoAgente(Estado):
    def __init__(self, posicao):
        self.__posicao = posicao
        
    def id_valor(self):
        return hash(self.__posicao)
    
    @property
    def posicao(self):
        return self.__posicao