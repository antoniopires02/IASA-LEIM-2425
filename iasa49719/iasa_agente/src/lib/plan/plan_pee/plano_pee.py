from plan.plano import Plano

"""
Esta classe representa um plano baseado numa solucao obtida por procura no espaco de estados, concebida para sistemas autonomos que necessitam de execucao eficiente das acoes planeadas. 
O construtor recebe uma solucao iteravel contendo os passos a seguir. 
O metodo obter_accao verifica se o estado atual corresponde ao proximo passo previsto e retorna a operacao correspondente para o agente executar. 
O metodo mostrar e utilizado para visualizacao, apresentando no simulador os vetores associados a cada acao ao longo do percurso. 
"""

class PlanoPEE(Plano):
    def __init__(self, solucao):
        self.__passos = [passo for passo in solucao]
        
    def obter_accao(self, estado):
        if self.__passos:
            passo = self.__passos.pop(0)
            if passo.estado == estado:
                return passo.operator
        
    def mostrar(self, vista):
        if self.__passos:
            for passo in self.__passos:
                vista.mostrar_vector(passo.estado.posicao, passo.operator.ang)
            
    @property
    def dimensao(self):
        return len(self.__passos)