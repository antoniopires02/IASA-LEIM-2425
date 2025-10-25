from .procura_melhor_prim import ProcuraMelhorPrim

"""
Classe que representa uma extensao do metodo de procura melhor-primeiro, introduzindo a capacidade de integrar uma 
funcao heuristica no processo de seleccao de nos. A procura informada baseia-se em conhecimento adicional sobre 
o dominio do problema para orientar a exploracao de estados de forma mais eficiente, procurando reduzir o espaco 
de busca necessario ate atingir o objectivo.
"""

class ProcuraInformada(ProcuraMelhorPrim):
    def procurar(self, problema, heuristica):
        self._avaliador.heuristica = heuristica
        return super().procurar(problema)