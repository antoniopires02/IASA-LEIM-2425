from mod.problema import Problema

"""
Esta classe representa um problema de planeamento para sistemas autonomos, derivando da classe base Problema. 
Durante a inicializacao, e definido o estado inicial e as operacoes disponiveis atraves do modelo de planeamento, assim como o estado final que corresponde ao objetivo a atingir. 
O metodo objectivo verifica se um dado estado corresponde ao estado final definido, permitindo assim avaliar se o agente alcançou o objetivo estabelecido. 
"""

class ProblemaPlan(Problema):
    def __init__(self, modelo_plan, estado_final):
        super().__init__(modelo_plan.obter_estado(), modelo_plan.obter_operadores())
        self.__estado_final = estado_final
        
    def objectivo(self, estado):
        if estado == self.__estado_final:
            return True
        return False