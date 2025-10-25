from .operador_contagem import OperadorContagem
from .estado_contagem import EstadoContagem
from mod.problema import Problema

"""
Classe ProblemaContagem

Esta classe deriva da classe base Problema e representa o problema "Contagem". 
A sua finalidade é definir um problema em que o agente deve alcançar ou ultrapassar um valor final 
a partir de um valor inicial, utilizando operadores de incremento.

Atributos:
- valor_final: valor que o estado final deve atingir ou ultrapassar.

Inicialização:
- Recebe o valor inicial, valor final e uma lista de incrementos possíveis.
- Cria o estado inicial e uma lista de operadores correspondentes a esses incrementos.

Métodos:
- objectivo(estado): retorna True se o valor do estado for maior ou igual ao valor final.
"""

class ProblemaContagem(Problema):
    def __init__(self, valor_inicial, valor_final, incrementos):
        super().__init__(EstadoContagem(valor_inicial), 
                         [OperadorContagem(incremento)
                         for incremento in incrementos])
        self.__valor_final = valor_final

        
    def objectivo(self, estado):
        return estado.valor >= self.__valor_final