from dataclasses import dataclass

from mod.estado import Estado
from mod.operador import Operador

"""
Classe de dados que representa um passo individual na sequencia de uma solucao encontrada durante o processo de planeamento. 
Cada instancia desta estrutura associa um determinado estado a um operador que levou a essa configuracao. 
Esta representacao e fundamental na reconstrucao do caminho seguido por um agente autonomo desde a origem ate ao objetivo. 
"""

@dataclass
class PassoSolucao:
    estado: Estado
    operador: Operador
