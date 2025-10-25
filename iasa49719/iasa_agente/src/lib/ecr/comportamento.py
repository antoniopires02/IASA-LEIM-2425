from abc import ABC, abstractmethod

""" 
A classe abstrata comportamento define o modelo reactivo no âmbito de ser a resposta a estúmlos recebidos.
Um comportamento é conjunto de ações modularizadas entre si.
"""

class Comportamento(ABC):
    
    @abstractmethod
    def activar(self, percepcao):
        """Ativar acção comportamento"""
    