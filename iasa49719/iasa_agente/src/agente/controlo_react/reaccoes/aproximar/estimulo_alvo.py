# se existir alvo naquela direccao retorna intensidade que é relação inversa da distancia, senao retorna zero.
# intensidae normalizada entre 0 e 1. Quando muito proximos do alvo muito alta, caso contrario caimento exponencial.
# gama é a base da função exponencial.

from ecr.estimulo import Estimulo
from sae.ambiente.elemento import Elemento

"""
    Classe EstimuloAlvo: Representa um estímulo para detectar a presença de um alvo em uma direção específica.

    Princípios de IA: Utiliza informações sensoriais para detectar a presença de um alvo em uma direção específica. 
    Utiliza uma função exponencial (com base gama) para modelar a intensidade do estímulo em relação à distância ao alvo.

    Princípios de agentes reativos com memória: Não mantém estado interno além da direção e do parâmetro gama.

    Princípios de arquitetura de subsunção: Implementa um comportamento reativo, retornando a intensidade do estímulo com base na percepção atual.

    Atributos:
        __direccao (Direccao): Direção em que o estímulo detecta a presença do alvo.
        __gama (float): Parâmetro que controla a intensidade exponencial do estímulo em relação à distância.

    Métodos:
        __init__: Construtor da classe.
        detectar: Detecta a presença de um alvo na percepção e retorna a intensidade do estímulo.
    """

class EstimuloAlvo(Estimulo):
    """
        Construtor da classe EstimuloAlvo.

        Args:
            direccao (Direccao): Direção em que o estímulo detecta a presença do alvo.
            gama (float): Parâmetro que controla a intensidade exponencial do estímulo em relação à distância. Padrão é 0.9.
        """
    def __init__(self, direccao, gama=0.9):
        self.__direccao = direccao
        self.__gama = gama
        
    def detectar(self, percepcao):
        """
        Detecta a intensidade do estímulo alvo na percepção.
        :param percepcao: Percepção do agente.
        :return: Intensidade do estímulo alvo.
        """
        elemento, distancia, _ = percepcao[self.__direccao]
        
        intensidade = self.__gama**distancia if elemento == Elemento.ALVO else 0
        
        return intensidade