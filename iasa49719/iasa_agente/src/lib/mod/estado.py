from abc import ABC, abstractmethod

""" 
A classe Estado é fundamental para representar os estados do problema. 
É uma classe abstrata que define um comportamento padrão para todos 
os estados que serão utilizados nos algoritmos de procura. 
A implementação dos estados específicos deve herdar dessa classe e fornecer uma implementação para o método abstrato id_valor(), 
que é responsável por retornar uma identificação única para cada estado. 
Para além disso, sobrescreve os métodos __hash__() e __eq__() para garantir que os estados possam ser corretamente comparados e identificados.
"""

class Estado(ABC):
    def __hash__(self):
        return self.id_valor()
    
    # Se o other nao for instancia de estado, retorna None
    def __eq__(self, other):
        if isinstance(other, Estado):
            return self.__hash__() == other.__hash__()
    
    @abstractmethod
    def id_valor(self):
        """ID Valor"""