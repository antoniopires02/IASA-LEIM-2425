from .procura_profundidade import ProcuraProfundidade


class ProcuraProfLim(ProcuraProfundidade):
    def __init__(self, prof_max=10):
        self._prof_max = prof_max
        super().__init__()
       
    @property 
    def prof_max(self):
        return self._prof_max
        
    def _expandir(self, problema, no):
        return super()._expandir(problema, no)\
            if no.profundidade < self._prof_max else [] # Não rebentar com o código já feito
        