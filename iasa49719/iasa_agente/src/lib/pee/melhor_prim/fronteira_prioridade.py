from pee.mec_proc.fronteira import Fronteira
import heapq

""" 
Organiza os nós na fronteira de acordo com o menor custo das transições.
"""

class FronteiraPrioridade(Fronteira):
    def __init__(self, avaliador):
        super().__init__()
        self.__avaliador = avaliador
        
    def inserir(self, no):
        no.prioridade = self.__avaliador.prioridade(no)
        heapq.heappush(self._nos, no)
    
    def remover(self):
        return heapq.heappop(self._nos)