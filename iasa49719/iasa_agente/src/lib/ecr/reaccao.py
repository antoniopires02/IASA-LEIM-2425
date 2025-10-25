#Convenção de imports dentro da biblioteca ecr.
from .comportamento import Comportamento

""" 
Sistema reativo - há um estímulo, produz-se uma resposta correspondente.
Associação estímulo resposta - Reação - unidade de associação de estímulos a respostas.
Modelo de reação: 1 unidade de estímulo (filtro - detector de estímulo na percepção) e 1 unidade de resposta(gera a resposta correspondente).
Percepção direcional - Elemento, distância e posição.
Percepção geral - Dá a posição x e y,
Modularizar - agrupar reações em comportamentos.
Comportamento composto - unidade modular que pode conter comportamentos.

Percepção vem do exterior, é processada pelo detetar do estímulo, vai gerar uma intensidade que alimenta o ativar de uma resposta e por fim é gerada uma ação.
"""

class Reaccao(Comportamento):
    
    def __init__(self, estimulo, resposta):
        self.__estimulo = estimulo
        self.__resposta = resposta
        
    def activar(self, percepcao):
        intensidade = self.__estimulo.detectar(percepcao)
        if intensidade > 0:
            # accao é uma variável explicativa, para efeitos de fácil leitura do código.
            accao = self.__resposta.activar(percepcao, intensidade)
            return accao
