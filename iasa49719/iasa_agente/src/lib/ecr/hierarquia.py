from .comport_comp import ComportComp

""" 
No âmbito da implementação de um sistema de hierarquia é criada a classe Hierarquia 
que necessita de uma prioridade de comportamentos internos fixa para tomada de decisões do agente.
Hierarquia de subsunção: topo da hierarquia substitui e suprime ação de menor prioridade.
"""

class Hierarquia(ComportComp):        
        
    def seleccionar_accao(self, accoes):
        if accoes:
            return accoes[0]