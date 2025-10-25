from abc import ABC, abstractmethod

"""
Interface que define a estrutura de um avaliador utilizado nos mecanismos de procura. O avaliador tem como funcao 
atribuir uma prioridade a cada no da fronteira, permitindo ordenar os nos de acordo com uma estrategia de avaliacao 
especifica. Esta abstracao permite que diferentes tipos de procura, como procura informada ou procura gulosa, possam 
definir os seus proprios criterios de selecao de nos, atraves da implementacao do metodo prioridade em subclasses 
concretas.
"""

class Avaliador(ABC):
    @abstractmethod
    def prioridade(self, no):
        '''Prioridade Avaliador'''
        