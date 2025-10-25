from agente.agente_delib import AgenteDelib
from agente.agente_react import AgenteReact
from sae import Simulador

#agente = AgenteReact()
agente = AgenteDelib()

simulador = Simulador(1, agente)
simulador.executar()


#Simulador(2, agente).executar()