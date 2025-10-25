from .avaliador import Avaliador


class AvaliadorCustoUnif(Avaliador):
    def prioridade(self, no):
        return no.custo