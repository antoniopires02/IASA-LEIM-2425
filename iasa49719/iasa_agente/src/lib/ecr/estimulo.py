from abc import ABC, abstractmethod

""" 
Para que um estímulo detatado em ambiente de jogo origine uma resposta
sob a forma de Comportamento é necessário definir o método abstracto detectar.
Primeiro é obtida uma percepção que por sua vez irá corresponder a um estímulo com intensidade característica.
"""

class Estimulo(ABC):
    
    @abstractmethod
    def detectar(self, percepcao):
        """Detectar estímulo na percepção"""
    