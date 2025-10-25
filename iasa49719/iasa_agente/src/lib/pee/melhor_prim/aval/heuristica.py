from abc import ABC, abstractmethod

"""
Interface que estabelece o contrato para implementações de heurísticas. A heurística é uma função definida pelo 
utilizador que estima o custo ou distância restante a partir de um dado estado até ao objetivo, orientando algoritmos 
de procura informada. O método abstrato 'h' deve ser implementado para devolver esse valor estimado, adaptado às 
características específicas do problema em questão.
"""

class Heuristica(ABC):
    @abstractmethod
    def h(self, estado):
        """h Heuristica"""