'''
A classe No representa um nó na árvore de busca. 
Contém informações como o estado, o operador que levou a esse estado, o antecessor desse nó na árvore e outras informações relevantes para a procura, 
como custo acumulado e profundidade do nó na árvore. 
A classe é utilizada pelos algoritmos de procura para representar os estados e as transições entre eles. 
Cada nó é associado a um estado específico do problema, com informações sobre como esse estado foi alcançado.
Nó: estado que representa, nó antecessor e operador que levou a esse estado, profundidade do nó e custo do nó. Profundidade e custo são cumulativos.
'''

class No:
    
    nos_criados = 0
    nos_eliminados = 0
    max_nos_memoria = 0
    
    def __init__(self, estado, operador = None, antecessor = None, custo = 0):
        if not antecessor:
            self.__profundidade = 0
            self.__custo = 0
        else:
            self.__profundidade = antecessor.profundidade + 1
            self.__custo = custo
            
        self.__estado = estado
        self.__operador = operador
        self.__antecessor = antecessor
        
        self.__prioridade = None
        
        No.nos_criados += 1
        
        nos_memoria_momento = No.nos_criados - No.nos_eliminados 
        
        if nos_memoria_momento > No.max_nos_memoria:
            No.max_nos_memoria = nos_memoria_momento
        
    def __del__(self):
        No.nos_eliminados += 1
        
    @property
    def estado(self):
        return self.__estado
    
    @property
    def operador(self):
        return self.__operador
    
    @property
    def antecessor(self):
        return self.__antecessor

    """ 
    A profundidade e o custo são atributos read only.
    """
    @property
    def profundidade(self):
        return self.__profundidade
    
    @property
    def custo(self):
        return self.__custo
    
    #ReadWrite
    @property #Getter
    def prioridade(self):
        return self.__prioridade
    
    @prioridade.setter #Setter
    def prioridade(self, valor):
        self.__prioridade = valor
        
    def __lt__(self, outro_no):
        return self.__prioridade < outro_no.prioridade