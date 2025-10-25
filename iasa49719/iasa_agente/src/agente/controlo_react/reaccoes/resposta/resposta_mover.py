from ecr.resposta import Resposta
from sae.agente.accao import Accao

"""
Classe RespostaMover, que herda da classe Resposta.

Esta classe:
- Define uma resposta baseada em movimento, usada em comportamentos reativos do agente.
- Recebe uma direção como parâmetro no construtor.
- Cria uma instância da classe Accao com essa direção.
- Inicializa a superclasse Resposta com a ação criada, tornando possível a execução do movimento no ambiente.

    Classe RespostaMover: Representa uma resposta do agente para se mover em uma direção específica.

    Princípios de IA: Utiliza uma ação para representar o movimento do agente em uma direção.

    Princípios de agentes reativos com memória: Não mantém estado interno além da ação de movimento.

    Princípios de arquitetura de subsunção: Implementa um comportamento reativo, onde a ação é disparada diretamente pela detecção do estímulo.
"""

class RespostaMover(Resposta):
    def __init__(self, direccao):
        accao = Accao(direccao)
        super().__init__(accao)
        