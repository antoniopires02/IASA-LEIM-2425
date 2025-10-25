from .procura_prof_lim import ProcuraProfLim


class ProcuraProfIter(ProcuraProfLim):
    def procurar(self, problema, inc_prof=1, limite_prof=100):
        for profundidade in range(0, limite_prof + 1, inc_prof):
            self._prof_max = profundidade
            solucao = super().procurar(problema)
            if solucao:
                return solucao