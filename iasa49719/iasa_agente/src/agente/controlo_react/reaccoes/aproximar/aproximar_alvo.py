from sae.ambiente.direccao import Direccao
from .aproximar_dir import AproximarDir
from ecr.prioridade import Prioridade

""" 
A classe implementa os comportamentos que permitem ao agente aproximar-se de um alvo numa das
quatro direções possíveis.

O gente aproxima-se do alvo com base na distância percebida entre o mesmo e o alvo, de acordo com prioridades. Isso é feito através
da seleção da ação mais prioritária entre os comportamentos constituintes do comportamento AproximarAlvo.
"""

class AproximarAlvo(Prioridade):
    def __init__(self):
        comportamentos = [AproximarDir(direccao) for direccao in Direccao]
        super().__init__(comportamentos)

'''
Alterei o construtor da classe retirando a função fornecida pelo editor python list visto já estar implícito.
Para melhor entendimento do código armazenei o antigo conteúdo do construtor numa variável "comportamentos".
'''