from ..resposta.resposta_evitar import RespostaEvitar
from .estimulo_obst import EstimuloObst
from ecr.reaccao import Reaccao

"""
    Classe EvitarDir: Representa uma reação do agente para evitar obstáculos em uma direção específica.

    Princípios de IA: Utiliza informações sensoriais para detectar obstáculos em uma direção específica e agir de acordo.

    Princípios de agentes reativos com memória: Não mantém estado interno além da configuração inicial da reação.

    Princípios de arquitetura de subsunção: Implementa um comportamento reativo, onde a ação é disparada diretamente pela detecção do estímulo.
"""

class EvitarDir(Reaccao):
    def __init__(self, direccao):
        super().__init__(
            EstimuloObst(direccao), 
            RespostaEvitar(direccao)
        )