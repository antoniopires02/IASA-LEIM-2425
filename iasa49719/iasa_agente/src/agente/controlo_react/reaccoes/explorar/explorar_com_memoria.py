from ecr.comportamento import Comportamento
from sae.agente.avancar import Avancar

"""
Classe Explorar, que define um comportamento fixo simples para o agente se mover aleatoriamente no ambiente.

Esta classe:
- Baseia-se em respostas a estímulos para ativar o movimento.
- Implementa um comportamento de exploração, onde o agente escolhe direções aleatórias para se mover.
- Usa a função random.choice para selecionar aleatoriamente uma direção válida do conjunto de direções disponíveis.
- Ao ativar, cria uma resposta do tipo RespostaMover com a direção aleatória escolhida.
- Permite que o agente explore o ambiente de forma livre, sem objetivo direcional específico.
"""

class ExplorarComMemoria(Comportamento):
    def __init__(self, dim_max = 100):
        self.__memoria = []
        self.__dim_max = dim_max
    # memoria é uma lista
    # Quando se chega ao maximo da memoria elimina-se a memoria do inicio da lista
    # situação sabe posicao e direcao
    # se situação observada -> , caso contrario
       
     
    def activar(self, percepcao):
        # tuplo - situacao_atual posicao e direcao (vamos buscar à percepcao)
        situacao = (percepcao.posicao, percepcao.direccao)
        
        if situacao not in self.__memoria:
            if len(self.__memoria) >= self.__dim_max:
                self.__memoria.pop(0)
            self.__memoria.append(situacao)
            
        return Avancar()