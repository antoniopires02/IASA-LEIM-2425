#4 instancias de aproximar
#cada uma tem estimulo alvo e dispara respostamover nessa direccao
#prioridade inversamente prporcional a distancia

from sae.ambiente.direccao import Direccao
from .evitar_dir import EvitarDir
from ecr.hierarquia import Hierarquia

"""
O comportamento EvitarObst é um sub-objetivo do agente prospetor 
que é realizado com prioridade sob o Explorar, 
mas abaixo do AproximarAlvo na hierarquia.
"""

class EvitarObst(Hierarquia):
    def __init__(self):
        comportamentos = [EvitarDir(direccao) for direccao in Direccao]
        super().__init__(comportamentos)