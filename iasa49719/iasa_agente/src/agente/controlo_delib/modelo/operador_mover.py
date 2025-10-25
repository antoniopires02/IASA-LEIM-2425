import math
from agente.controlo_delib.modelo.estado_agente import EstadoAgente
from mod.operador import Operador
from sae.agente.accao import Accao

"""
Classe que define o operador mover. Esta classe herda a classe Operador e tem o objectivo de definir os operadores de 
movimentação para o agente. Este precisa de um modelo do mundo e de uma direção para poder realizar o movimento. A partir
da direção que recebe este consegue criar uma acção.
"""


class OperadorMover(Operador):
    def __init__(self, modelo_mundo, direccao):
        self.__modelo_mundo = modelo_mundo
        self.__ang = direccao.value
        self.__accao = Accao(direccao)

    def aplicar(self, estado):
        nova_posicao = self.translacao(estado.posicao, self.__accao.passo, self.__ang)
        novo_estado = EstadoAgente(nova_posicao)

        if novo_estado in self.__modelo_mundo:
            return novo_estado
        return None
        
    def translacao(self, posicao, distancia, angulo):
        x, y = posicao
        dx = round(distancia * math.cos(angulo))
        dy = -round(distancia * math.sin(angulo))
        nova_posicao = x + dx, y + dy
        return nova_posicao
        
    def custo(self, estado, estado_suc):
        custo = math.dist(estado.posicao, estado_suc.posicao)
        return max(1, custo)
        
    @property
    def ang(self):
        return self.__ang
        
    @property
    def accao(self):
        return self.__accao