from .passo_solucao import PassoSolucao


"""
Classe que representa a solucao encontrada para um determinado problema de planeamento. 
Esta estrutura e responsavel por reconstruir o percurso desde o estado inicial ate ao estado final, percorrendo os antecessores do no terminal obtido durante a procura. 
Para isso, utiliza uma lista de passos, onde cada passo associa um estado a um operador, permitindo assim compreender a sequencia de accoes que conduziu a solucao. 
A classe e iteravel, facilitando a sua integracao em ciclos e visualizacoes. 
Adicionalmente, expoe propriedades para consultar o custo total e a profundidade da solucao, informacoes importantes na avaliacao da eficiencia do plano gerado.
"""

#Propriedades privadas o valor é calculado em execução 

class Solucao:
    def __init__(self, no_final):
        self.__no_final = no_final
        self.__passos = []
        no = no_final
        while no.antecessor:
            passo = PassoSolucao(no.antecessor.estado, no.operador)
            self.__passos.insert(0, passo)
            no = no.antecessor
            
        self.__dimensao = no_final.profundidade
        self.__custo = no_final.custo
        
        
    @property
    def dimensao(self):
        return self.__dimensao
    
    @property
    def custo(self):
        return self.__custo
    
    def __iter__(self):
        """
        for passo in solucao:
            print("Passo: ")
            print(passo.estado)
            print(passo.operador)
            
        solucao[1]
        """
        return iter(self.__passos)
    
    def __getitem__(self, index):
        return self.__passos[index]