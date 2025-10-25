from ecr.estimulo import Estimulo
from sae.ambiente.elemento import Elemento

"""
    Classe EstimuloObst: Representa um estímulo que detecta a presença de obstáculos em uma direção específica.

    Princípios de IA: Utiliza informações sensoriais para detectar obstáculos em uma direção específica.

    Princípios de agentes reativos com memória: Não mantém estado interno além da direção e intensidade do estímulo.

    Princípios de arquitetura de subsunção: Implementa um comportamento reativo, retornando a intensidade do estímulo com base na percepção atual.
"""

class EstimuloObst(Estimulo):
    def __init__(self, direccao, intensidade = 1.):
        self.__direccao = direccao
        self.__intensidade = intensidade
    
    def detectar(self, percepcao):
        intensidade = self.__intensidade if percepcao.contacto_obst(self.__direccao) else 0
        return intensidade