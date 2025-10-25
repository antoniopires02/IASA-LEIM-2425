from controlo_delib.mec_delib import MecDelib
from plan.plan_pee.planeador_pee import PlaneadorPEE
from sae.agente.transdutor import Transdutor
from sae.ambiente.ambiente import Ambiente
from sae.defamb import DEF_AMB

from controlo_delib.modelo.modelo_mundo import ModeloMundo
from controlo_delib.modelo.estado_agente import EstadoAgente

def obter_percepcao():
    num_amb = 4
    ambiente = Ambiente(DEF_AMB[num_amb])
    transdutor = Transdutor()
    transdutor.iniciar(ambiente)
    return transdutor.percepcionar() # Retornar uma perceção

def actualizar_modelo_mundo():
    """
    Teste de actualização do modelo do mundo
    
    >>> modelo_mundo = actualizar_modelo_mundo()
    >>> modelo_mundo.alterado
    True
    
    >>> estado = modelo_mundo.obter_estado()
    >>> estado.posicao
    (0, 0)
    
    >>> estados = modelo_mundo.obter_estados()
    >>> len(estados)
    671
    
    >>> operadores = modelo_mundo.obter_operadores()
    >>> len(operadores)
    4
    
    >>> estado = EstadoAgente((28, 9))
    >>> modelo_mundo.obter_elemento(estado)
    <Elemento.ALVO: 'A'>
    """
    percepcao = obter_percepcao()
    modelo_mundo = ModeloMundo()
    modelo_mundo.actualizar(percepcao)
    return modelo_mundo

def gerar_objectivos():
    """
    >>> objectivos = gerar_objectivos()
    >>> len(objectivos)
    3
    """
    modelo_mundo = actualizar_modelo_mundo()
    mec_delib = MecDelib(modelo_mundo)
    return mec_delib.deliberar()

def gerar_plano():
    """
    >>> plano = gerar_plano()
    >>> plano.dimensao
    37
    """
    planeador = PlaneadorPEE()
    modelo_mundo = actualizar_modelo_mundo()
    objectivos = gerar_objectivos()
    return planeador.planear(modelo_mundo, objectivos)
    

# Executar teste
if __name__ == "__main__":
    import doctest
    doctest.testmod() #Procura as intrucoes de teste do meu modulo e executa.