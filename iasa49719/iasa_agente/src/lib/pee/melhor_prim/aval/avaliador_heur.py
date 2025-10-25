from abc import ABC
from pee.melhor_prim.aval.avaliador import Avaliador

"""
Classe base para avaliadores que utilizam uma heuristica como criterio de avaliacao. Esta classe permite definir 
dinamicamente a heuristica a ser utilizada, oferecendo flexibilidade na seleccao da estrategia de avaliacao consoante 
o tipo de problema e contexto. Serve de fundacao para avaliadores mais especificos, como os usados em metodos 
de procura informada no dominio da inteligencia artificial e planeamento autonomo.
"""

class AvaliadorHeur(Avaliador, ABC):
    def __init__(self):
        self._heuristica = None
        
    @property
    def heuristica(self):
        return self._heuristica
    
    @heuristica.setter
    def heuristica(self, valor):
        self._heuristica = valor