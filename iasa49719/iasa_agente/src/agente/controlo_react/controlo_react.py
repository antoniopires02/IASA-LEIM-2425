from ecr.comportamento import Comportamento

"""
Controlo reativo do agente, que controla o agente segundo a arquitetura reativa.
O Comportamento do sistema é gerado com base nas associações entre estímulos (perceções) e respostas (ações).
A arquitetura reativa baseia-se num modelo simples de ação-reação, em que o agente perceciona um estímulo através da observação do ambiente ao seu redor. 
Dependendo da intensidade do estímulo, é gerada uma resposta correspondente, levando à execução de uma ação por parte do agente.
"""

class ControloReact():
    def __init__(self, comportamento):
        self.__comportamento = comportamento
    
    def processar(self, percepcao): # retorna uma ação
        return self.__comportamento.activar(percepcao)