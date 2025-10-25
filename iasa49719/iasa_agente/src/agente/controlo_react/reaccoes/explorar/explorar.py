import random
from ecr.comportamento import Comportamento
from sae.agente.avancar import Avancar
from sae.agente.rodar import Rodar
from sae.ambiente.direccao import Direccao

"""
Classe Explorar, que define um comportamento fixo simples para o agente se mover aleatoriamente no ambiente.

Esta classe:
- Baseia-se em respostas a estímulos para ativar o movimento.
- Implementa um comportamento de exploração, onde o agente escolhe direções aleatórias para se mover.
- Usa a função random.choice para selecionar aleatoriamente uma direção válida do conjunto de direções disponíveis.
- Ao ativar, cria uma resposta do tipo RespostaMover com a direção aleatória escolhida.
- Permite que o agente explore o ambiente de forma livre, sem objetivo direcional específico.
"""

class Explorar(Comportamento):
    
    def __init__(self, probabilidade_rotacao = 0.7):
        self.__probabilidade_rotacao = probabilidade_rotacao
        self.__direccoes = list(Direccao)
        
    # percepcao apenas serve para cumprir o contrato de Comportamento, não tem utilidade nesta expecialização.
    def activar(self, percepcao):
        valor_aleatorio = random.random()
        direccao_aleatoria = random.choice(self.__direccoes)
        if valor_aleatorio < self.__probabilidade_rotacao:
            accao = Rodar(direccao_aleatoria)
        else:
            accao = Avancar()
        
        return accao