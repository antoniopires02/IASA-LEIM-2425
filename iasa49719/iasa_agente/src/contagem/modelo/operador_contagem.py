from .estado_contagem import EstadoContagem
from mod.operador import Operador

"""
Classe OperadorContagem

Esta classe deriva da classe base Operador e é usada no problema "Contagem". 
Tem como objetivo definir a operação de incremento sobre um estado, onde o novo estado é o resultado 
da soma do valor atual com um valor fixo de incremento. Esta operação é usada para gerar sucessores 
num grafo de estados.

Atributos:
- incremento: valor fixo somado ao valor atual do estado.

Métodos:
- aplicar(estado): retorna um novo EstadoContagem resultante do incremento do estado atual.
- custo(estado, estado_suc): retorna o custo da operação, definido como o quadrado do valor do incremento.
"""

class OperadorContagem(Operador):
    
    def __init__(self, incremento):
        self.__incremento = incremento
        
    @property
    def incremento(self):
        return self.__incremento
    
    def custo(self, estado, estado_suc):
        return self.__incremento**2
    
    # Estado é um objeto imutável
    def aplicar(self, estado):
        novo_valor = estado.valor + self.__incremento
        return EstadoContagem(novo_valor)