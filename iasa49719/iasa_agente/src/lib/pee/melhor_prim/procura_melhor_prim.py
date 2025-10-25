from pee.mec_proc.procura_grafo import ProcuraGrafo
from pee.melhor_prim.fronteira_prioridade import FronteiraPrioridade

"""
Classe que implementa o metodo de procura melhor-primeiro, em que os nos sao explorados com base na prioridade definida 
por um avaliador. Este avaliador combina informacoes como custo acumulado e heuristica para determinar a ordem de 
exploracao. A fronteira utilizada organiza os nos por ordem crescente de avaliacao, garantindo que o no com menor custo 
estimado e escolhido em cada iteracao. Esta abordagem permite uma procura mais eficiente em espacos grandes, evitando 
a exploracao desnecessaria de caminhos com custo elevado. A classe mantem o melhor no conhecido para cada estado, 
substituindo-o se uma nova alternativa com custo inferior for encontrada.
"""


class ProcuraMelhorPrim(ProcuraGrafo):
    def __init__(self, avaliador):
        super().__init__(FronteiraPrioridade(avaliador))
        self._avaliador = avaliador
        
    def _manter(self, no):
        #nó não está nos explorados 
        #ou o custo do nó é menor que o custo do nó já explorado
        return no.estado not in self._explorados or \
            no.custo < self._explorados[no.estado].custo