from agente.controlo_react.reaccoes.aproximar.aproximar_alvo import AproximarAlvo
from agente.controlo_react.reaccoes.explorar.explorar import Explorar
from ecr.hierarquia import Hierarquia

"""
    Recolher alvos permite ao agente realizar comportamentos de acordo com o ambiente em
    que está e com a hierarquia definida para cada um deles. 
    Objetivos do agente prospector (ter sub-comportamento): 

	.recolher alvos
		Sub-Objetivos:
			.aproximar-alvo
			.evitar obstaculos
			.explorar

    Se existe um alvo, aproxima do alvo,
    Caso contrario vai evitar obstaculos,
    Para que possa explorar em zonas onde nao existem obstaculos
    Internamente, o comportamento Recolher é um comportamento composto.
    Hierarquia já extende ComportamentoComposto.
    O recolher vai usar instancias destas classes para as guardar nele próprio.
"""

class Recolher(Hierarquia):
    def __init__(self):
        comportamentos = [
            AproximarAlvo(),
            Explorar()
        ]
        super().__init__(comportamentos)