from abc import ABC, abstractmethod
from .mecanismo_procura import MecanismoProcura

"""
A classe ProcuraGrafo implementa a procura em grafo, a qual faz parte do macanismo de procura.
Tem como objetivo verificar os nós já explorados. 
Para eliminar nós repetidos é necessário verificar se existem nós sucessores que já foram explorados.
Se tal acontecer, o nó com menor custo é mantido.
"""

class ProcuraGrafo(MecanismoProcura, ABC):
    def _iniciar_memoria(self):
        super()._iniciar_memoria()
        self._explorados = {}
    
    def _memorizar(self, no):
        if self._manter(no):
            super()._memorizar(no)
            self._explorados[no.estado] = no
            
    @abstractmethod
    def _manter(self, no):
        '''Manter Procura em Grafo'''