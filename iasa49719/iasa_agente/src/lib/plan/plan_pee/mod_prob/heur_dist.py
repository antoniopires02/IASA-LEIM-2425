import math
from pee.melhor_prim.aval.heuristica import Heuristica

"""
Esta classe representa uma heuristica utilizada em algoritmos de procura informada, que calcula a distancia entre o estado atual e o estado objetivo. 
Herda da superclasse Heuristica, define a funcao heuristica h como a distancia euclidiana entre as posicoes dos estados fornecidos. 
"""


class HeurDist(Heuristica):
    def __init__(self, estado_final):
        self.__estado_final = estado_final
        
    def h(self, estado):
        dist = math.dist(estado.posicao, self.__estado_final.posicao)
        return dist
    
    # Agente deliberativo que utiliza esta maquinaria desenvolvida (Controlo Deliberativo, e procura PEE), para colocar o agente a recolher os alvos.