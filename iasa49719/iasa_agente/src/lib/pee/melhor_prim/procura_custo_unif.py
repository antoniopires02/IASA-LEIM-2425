from pee.melhor_prim.aval.avaliador_custo_unif import AvaliadorCustoUnif
from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim

# Função f é dada pelo custo do nó
# Procura custo uniforme.
class ProcuraCustoUnif(ProcuraMelhorPrim):
    def __init__(self):
        super().__init__(AvaliadorCustoUnif())