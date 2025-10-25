from agente.controlo_react.controlo_react import ControloReact
from agente.controlo_react.reaccoes.explorar.explorar import Explorar
from agente.controlo_react.reaccoes.explorar.explorar_com_memoria import ExplorarComMemoria
from agente.controlo_react.reaccoes.recolher import Recolher
from sae import Agente

"""
A classe AgenteReact é uma especialização da classe Agente que implementa um agente reativo.
O agente reativo é controlado por um comportamento que é gerado com base nas associações entre estímulos (perceções) e respostas (ações).    
"""

class AgenteReact(Agente):
    # O agente é inicializado com o comportamento Explorar.
    
    def __init__(self):
        super().__init__()
        #comportamento = Explorar()
        comportamento = Recolher()
        #comportamento = ExplorarComMemoria()
        self.__controlo = ControloReact(comportamento)
     
        """
        Partições do Modelo Reativo 
        """
    def executar(self):
        percepcao = self._percepcionar()
        accao = self.__controlo.processar(percepcao)
        super()._actuar(accao)
        
        