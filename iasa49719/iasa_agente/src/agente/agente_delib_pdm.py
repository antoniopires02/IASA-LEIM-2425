from agente.controlo_delib.controlo_delib import ControloDelib
from plan.plan_pdm.planeador_pdm import PlaneadorPDM
from sae import Agente
from sae import Simulador


class AgenteDelibPDM(Agente):
    def __init__(self):
        super().__init__()
        planeador = PlaneadorPDM()
        self.__controlo = ControloDelib(planeador)

    def executar(self):
        percepcao = self._percepcionar()
        accao = self.__controlo.processar(percepcao)
        self.__controlo.mostrar(self.vista)
        self._actuar(accao)
        
# Executar Simulação
if __name__ == "__main__":
    agente = AgenteDelibPDM()
    simulador = Simulador(3, agente, vista_modelo=True)
    simulador.executar()