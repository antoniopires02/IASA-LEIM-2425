from agente.controlo_react.reaccoes.aproximar.estimulo_alvo import EstimuloAlvo
from agente.controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from ecr.reaccao import Reaccao

"""
O aproximar direcional é uma reação que associa um estimulo alvo a uma resposta mover.
A classe AproximarDir Representa uma reação do agente para se aproximar de um alvo em uma direção específica.
Utiliza informações sensoriais para detectar a presença de um alvo em uma direção específica e tomar ação para se aproximar.
Princípios de agentes reativos com memória: Não mantém estado interno além da configuração inicial da reação.
Princípios de arquitetura de subsunção: Implementa um comportamento reativo, onde a ação é disparada diretamente pela detecção do estímulo.
Atributos: Nenhum atributo adicional além dos herdados da classe Reaccao.
"""

class AproximarDir(Reaccao):
    
    def __init__(self, direccao):
        super().__init__(
            EstimuloAlvo(direccao),
            RespostaMover(direccao)
        )