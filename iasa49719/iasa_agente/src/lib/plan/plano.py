from abc import ABC, abstractmethod

"""
Esta interface especifica o comportamento esperado de um plano para um agente autonomo. 
O plano e responsavel por determinar a acao que o agente deve executar dado o seu estado atual, permitindo assim a tomada de decisao fundamentada. 
A interface tambem inclui um metodo para visualizacao do plano 
"""

class Plano(ABC):
    """ Plano """
    @abstractmethod
    def obter_accao(self, estado):
        """ Obter acao """
        
    @abstractmethod   
    def mostrar(self, vista):
        """ Mostrar """