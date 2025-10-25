from ecr.resposta import Resposta
from sae.agente.rodar import Rodar

"""
Classe RespostaEvitar, que herda da classe RespostaMover.

Esta classe representa a resposta reativa do agente perante a presença de obstáculos. Quando é detetado um contacto com
um obstáculo na direção atual:
- A classe tenta encontrar uma direção livre (sem obstáculo).
- Essa nova direção é escolhida aleatoriamente a partir das disponíveis.
- Se nenhuma direção estiver livre, retorna None, ou seja, o agente não se move.
- Caso contrário, atualiza a ação com a nova direção e ativa a resposta normalmente.

Este comportamento permite ao agente evitar obstáculos dinamicamente, sem um plano deliberado.
"""


class RespostaEvitar(Resposta):
    # se na percepcao houver contacto, cria instancia de rodar numa nova direcao rodada de 90 graus, depois altera o atributo accao. No fim invoca o metodo ativar na superclasse.
    def activar(self, percepcao, intensidade):
        dir_actual = percepcao.direccao
        if percepcao.contacto_obst(dir_actual):
            nova_direccao = dir_actual.rodar()
            self._accao = Rodar(nova_direccao)
            return super().activar(percepcao, intensidade)
        