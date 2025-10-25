from abc import ABC

from .solucao import Solucao
from .no import No
from .fronteira import Fronteira

'''
A classe MecanismoProcura implementa um algoritmo genérico de procura que utiliza uma fronteira para controlar os nós a serem explorados. 
Recebe uma fronteira no momento da inicialização e implementa a lógica de busca no método procurar(). 
Este método realiza a procura enquanto a fronteira não estiver vazia, expandindo nós sucessores e verificando se algum deles é um estado objetivo. 
O método _expandir() gera os nós sucessores a partir de um nó dado, aplicando os operadores do problema. 
O método _memorizar() é abstrato e deve ser implementado pelas subclasses para definir como os nós são armazenados ou processados durante a procura.
Existem diferentes métodos de procura, como a procura em profundidade, que explora primeiro os nós mais recentes, e a procura em largura, que explora primeiro os nós mais antigos. 
Cada método utiliza uma estratégia de controlo específica e uma estrutura de dados para a fronteira de exploração, como LIFO para procura em profundidade e FIFO para procura em largura.
Estado e uma situação do problema (configuração do puzzle num dado momento)
Operador corresponde a uma ação, transição de estado. (Ação possível que produz transformação de estado)
Estados sucessores
Espaço de estados - Conjunto de estados do problema e todas transições possíveis
Problema
• Estado inicial
• Operadores
• Objectivos (ou função objectivo: estado → {True, False})
Mecanismo de Raciocínio
• Exploração de opções possíveis para encontrar uma solução através de simulação prospectiva, tendo por base uma representação interna do problema
Raciocínio automático através de procura para problemas de planeamento
'''

class MecanismoProcura(ABC):
    def __init__(self, fronteira):
        self._fronteira = fronteira
        
    def _iniciar_memoria(self):
        self._fronteira.iniciar()
        
    def _memorizar(self, no):
        self._fronteira.inserir(no)
        
    """
    Cria-se um nó inicial e inicia-se uma fronteira LIFO com o nó. 
    Enquanto a fronteira não estiver vazia, remove-se o primeiro nó para verificar se seu estado é o objetivo. 
    Se for, retorna-se a solução correspondente. Caso contrário, expande-se o nó e insere-se cada nó sucessor na fronteira. 
    Se a fronteira esvaziar sem encontrar a solução, conclui-se que ela não existe.
    """
    def procurar(self, problema):
        self._iniciar_memoria()
        no = No(problema.estado_inicial)
        self._memorizar(no)
        while not self._fronteira.vazia:
            no = self._fronteira.remover()
            if problema.objectivo(no.estado):
                return Solucao(no)
            for no_sucessor in self._expandir(problema, no):
                self._fronteira.inserir(no_sucessor)
        return None
        
    """ 
    Inicia-se uma lista de sucessores vazia. 
    Obtém-se o estado do nó atual e aplica-se cada operador ao estado, gerando estados sucessores. 
    Para cada sucessor válido, calcula-se o custo total (custo acumulado mais custo da transição). 
    Gera-se o nó sucessor e adiciona-se à lista de sucessores. Por fim, retorna-se a lista de nós sucessores.
    """
    def _expandir(self, problema, no):
        sucessores = []
        estado = no.estado
        for operador in problema.operadores:
            estado_suc = operador.aplicar(estado)
            if estado_suc is not None:
                custo = no.custo + operador.custo(estado, estado_suc)
                no_sucessor = No(estado_suc, operador, no, custo)
                sucessores.append(no_sucessor)
        return sucessores
    
    @property
    def nos_processados(self):
        return No.nos_criados
    
    """ Quando incrementamos num de nos criados, calcular num de nos memoria, se esse numero no momento for maior que o num de nos em memoria retorna"""
    @property
    def nos_em_memoria(self):
        return max(No.max_nos_memoria, No.nos_criados - No.nos_eliminados)
    