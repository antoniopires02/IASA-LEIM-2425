from pee.melhor_prim.aval.heuristica import Heuristica


class HeuristicaContagem(Heuristica):
    def __init__(self, valor_final):
        self.__valor_final = valor_final
        
    def h(self, estado):
        return abs(estado.valor - self.__valor_final)