import math
from agente.controlo_delib.modelo.estado_agente import EstadoAgente
from agente.controlo_delib.modelo.operador_mover import OperadorMover
from sae.ambiente.direccao import Direccao
from sae.ambiente.elemento import Elemento
from plan.modelo.modelo_plan import ModeloPlan

"""
Classe Modelo Mundo. Esta classe representa o ambiente onde o agente deliberativo está situado,
incluindo estados, elementos, posições e operadores disponíveis.

O construtor inicializa a maioria dos atributos como None ou vazios,
pois estes serão atualizados com a chamada ao método atualizar.

Esta classe representa o ambiente em que o agente deliberativo atua. O modelo mantém:
- O estado atual do agente (posição),
- Todos os estados possíveis com base na perceção,
- Elementos no ambiente (alvos, obstáculos),
- Operadores de movimento disponíveis (com base em direções possíveis),
- Um sinal de alteração (para indicar mudanças no mundo).

Métodos:
- obter_estado(): Retorna o estado atual do agente.
- obter_estados(): Retorna os estados reconhecidos no mundo.
- obter_operadores(): Retorna operadores de movimento válidos.
- obter_elemento(estado): Retorna o elemento presente numa determinada posição.
- distancia(estado): Calcula a distância entre o estado fornecido e o atual.
- actualizar(percepcao): Atualiza o modelo com base numa nova perceção.
- mostrar(vista): Mostra o estado atual do mundo visualmente.
- alterado: Indica se o mundo foi alterado desde a última atualização.
- __contains__: Permite verificar se um estado está contido nos estados conhecidos.
"""

class ModeloMundo(ModeloPlan):
    def __init__(self):
        self.__estado = None
        self.__estados = []
        self.__operadores = [OperadorMover(self, direccao) for direccao in Direccao]
        self.__elementos = {}
        self.__alterado = False
        
    def obter_estado(self):
        return self.__estado
        
    def obter_estados(self):
        return self.__estados
        
    def obter_operadores(self):
        return self.__operadores
        
    def obter_elemento(self, estado):
        return self.__elementos.get(estado.posicao)
        
    def distancia(self, estado):
        return math.dist(estado.posicao, self.__estado.posicao)
        
    def actualizar(self, percepcao):
        self.__estado = EstadoAgente(percepcao.posicao)
        self.__alterado = self.__elementos != percepcao.elementos
        if self.__alterado:
            self.__elementos = percepcao.elementos
            self.__estados = [EstadoAgente(posicao) for posicao in percepcao.posicoes]
        
    def mostrar(self, vista):
        for (posicao, elemento) in self.__elementos.items():
            if elemento in [Elemento.ALVO, Elemento.OBSTACULO]:
                vista.mostrar_elemento(posicao, elemento)
        vista.marcar_posicao(self.__estado.posicao)
        
    @property
    def alterado(self):
        return self.__alterado
    
    @property
    def elementos(self):
        return self.__elementos
    
    def __contains__(self, estado): #Implementação do operador in
        return estado in self.__estados