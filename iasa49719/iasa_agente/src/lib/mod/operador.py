from abc import ABC, abstractmethod

'''
A classe Operador define as operações que podem ser aplicadas aos estados do problema. 
É uma classe abstrata que exige a implementação dos métodos aplicar() e custo(). 
O método aplicar() é responsável por aplicar o operador a um estado e gerar um novo estado sucessor, 
enquanto o método custo() calcula o custo associado à aplicação do operador de um estado para outro. 
Permitindo que os algoritmos de procura avaliem a qualidade das transições entre estados.
'''

class Operador(ABC):
    @abstractmethod
    def aplicar(self, estado):
        """Aplica a estado"""
    
    @abstractmethod
    def custo(self, estado_suc):
        """Custo"""