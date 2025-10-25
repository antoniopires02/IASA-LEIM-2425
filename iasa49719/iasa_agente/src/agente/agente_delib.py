from controlo_delib.controlo_delib import ControloDelib
from plan.plan_pee.planeador_pee import PlaneadorPEE
from sae.agente.agente import Agente
from sae.simulador import Simulador


class AgenteDelib(Agente):
    def __init__(self):
        super().__init__()
        planeador = PlaneadorPEE()
        self.__controlo = ControloDelib(planeador)

    def executar(self):
        percepcao = self._percepcionar()
        accao = self.__controlo.processar(percepcao)
        self.__controlo.mostrar(self.vista)
        self._actuar(accao)
        
# Activação do agente
if __name__ == "__main__":
    agente = AgenteDelib()
    simulador = Simulador(3, agente, vista_modelo = True)
    simulador.executar()
