from abc import ABC, abstractmethod

"""
Contrato do ModeloPlan
"""

class ModeloPlan(ABC):
    """ ModeloPlan """
    
    @abstractmethod
    def obter_estado(self):
        """ Obter estado """
        
    @abstractmethod
    def obter_estados(self):
        """ Obter estados """
       
    @abstractmethod    
    def obter_operadores(self):
        """ Obter operadores """