from .avaliador_heur import AvaliadorHeur

"""
Classe que implementa um avaliador do tipo A asterisco (A*), baseada na extensao da classe AvaliadorHeur. Esta classe 
define uma estrategia de avaliacao informada que combina o custo acumulado ate ao momento (g) com uma estimativa 
heuristica do custo restante ate ao objectivo (h), retornando a soma destes dois valores como prioridade. Este tipo 
de avaliacao permite guiar a procura de forma eficiente, mantendo a admissibilidade da heuristica, ou seja, garantindo 
que a estimativa nunca sobrestima o custo real. Ideal para encontrar solucoes optimas em contextos de planeamento 
inteligente.
"""

class AvaliadorAA(AvaliadorHeur):
    def prioridade(self, no):
        return no.custo + self._heuristica.h(no.estado)