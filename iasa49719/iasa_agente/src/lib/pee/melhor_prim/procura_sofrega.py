from pee.melhor_prim.aval.avaliador_sof import AvaliadorSof
from .procura_informada import ProcuraInformada

#prioridade é so heuritsica

class ProcuraSofrega(ProcuraInformada):
    def __init__(self):
        super().__init__(AvaliadorSof())