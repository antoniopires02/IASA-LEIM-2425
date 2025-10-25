from pee.mec_proc.mecanismo_procura import MecanismoProcura
from .fronteira_lifo import FronteiraLIFO

"""
Classe que implementa o mecanismo de procura em profundidade, derivada da classe base de mecanismos de procura.
Esta classe utiliza uma estrutura de fronteira do tipo LIFO (Last In First Out) para gerir os nós a explorar,
permitindo assim explorar o espaço de estados em profundidade até encontrar a solução do problema.
"""

class ProcuraProfundidade(MecanismoProcura):
    def __init__(self):
        self.__fronteira = FronteiraLIFO()
        super().__init__(self.__fronteira)
