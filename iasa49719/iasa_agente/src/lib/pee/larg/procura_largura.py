from .fronteira_fifo import FronteiraFIFO
from pee.mec_proc.mecanismo_procura import MecanismoProcura

"""
Classe que implementa a estrategia de pesquisa em largura, onde os nos sao explorados por niveis de profundidade de forma sequencial. 
Esta abordagem garante que os caminhos mais curtos em termos de numero de transicoes sao analisados primeiro, tornando-a adequada para encontrar solucoes otimas em ambientes com custos uniformes. 
Esta classe herda de ProcuraGrafo e utiliza uma fronteira do tipo FIFO para manter a ordem de insercao dos nos, garantindo que os mais antigos sao processados antes dos mais recentes. Este tipo de estrategia esta associado ao paradigma de busca nao informada em sistemas autonomos.
"""

class ProcuraLargura(MecanismoProcura):
    def __init__(self):
        super().__init__(FronteiraFIFO())