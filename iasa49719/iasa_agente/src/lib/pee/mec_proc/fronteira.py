from abc import ABC, abstractmethod

"""
A classe Fronteira é uma abstração que define a estrutura necessária para controlar os estados
a serem explorados durante o processo de resolução de problemas através de raciocício automático.
A Fronteira armazena os nós que representam estados pendentes na árvore de procura.
Permite controlar os estados a serem expandidos.
"""

class Fronteira(ABC):
    def __init__(self):
        self.iniciar()
        
    @property
    def vazia(self):
        return len(self._nos) == 0
    
    def iniciar(self):
        self._nos = []
    
    @abstractmethod
    def inserir(self, no):
        """Inserir (Fronteira)"""
        
    #
    def remover(self):
        return self._nos.pop(0)