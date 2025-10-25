from pdm.mec_util import MecUtil

"""
A classe PDM implementa o Processo de decisão de Markov. 
É útil para modelar problemas de decisão em casos de incerteza.
"""

class PDM:
    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__mec_util = MecUtil(modelo, gama, delta_max)
        
    """
    O método politica implementa a política do processo. 
    Serve de componente de decisão que orienta o agente à tomada de decisões em cada estado.
    """
    
    def politica(self, U):
        S, A = self.__modelo.S, self.__modelo.A
        politica = {}
        for s in S():
            if A(s):
                util_accao = self.__mec_util.util_accao
                politica[s] = max(A(s), key=lambda a: util_accao(s, a, U))
        return politica
    
        
    def resolver(self):
        U = self.__mec_util.utilidade()
        politica = self.politica(U)
        return U, politica
        