from pee.mec_proc.fronteira import Fronteira

"""
Classe que estende a classe Fronteira para implementar uma estrutura LIFO (Last In First Out). Nesta implementação, os 
nós são adicionados no final da lista interna, o que significa que o último nó inserido será o primeiro a ser removido. 
Este tipo de fronteira é adequado para algoritmos de procura em profundidade, onde a exploração segue a profundidade do 
espaço de estados.
"""

class FronteiraLIFO(Fronteira):
    def __init__(self,):
        super().__init__()
        
    def inserir(self, no):
       self._nos.insert(len(self._nos) - 1, no) 