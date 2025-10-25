from abc import ABC, abstractmethod

"""
Esta interface define o contrato para classes que implementam mecanismos de planeamento para agentes autonomos. 
O seu objetivo e permitir a criacao de planos eficientes a partir de um modelo do ambiente e de um conjunto de objetivos. 
"""


class Planeador(ABC):
    """ Planeador """
    
    @abstractmethod
    def planear(self, modelo_plan, objectivos):
        """ Planear"""