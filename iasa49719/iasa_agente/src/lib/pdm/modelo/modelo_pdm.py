from abc import ABC, abstractmethod

"""
A interface Modelo PDM cumpre as boas práticas de programação em python ao referenciar ABC.
Pode ser considerada como uma 'Blueprint' do processo de decisão de Markov.
"""

class ModeloPDM(ABC):
    
    """
    O método S() define e trata o conjunto de estados do mundo
    """
    
    @abstractmethod
    def S(self):
        """ S - Conjunto de estados """
        
    """
    O método A(s) define e trata o espectro de ações no estado s
    """
    
    @abstractmethod
    def A(self, s):
        """ A - Ações possiveis no estado"""
        
    """
    O método T(s, a, sn) define e trata as probabilidades de transição de estados
    """
        
    @abstractmethod
    def T(self, s, a, sn):
        """ T - probabilidade de transição """
        
    @abstractmethod
    def R(self, s, a, sn):
        """ R - recompensa esperada na transicao"""
        
    @abstractmethod
    def suc(self, s, a):
        """ suc """
        