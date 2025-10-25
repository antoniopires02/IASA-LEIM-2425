from pdm.pdm import PDM
from plan.plan_pdm.modelo.modelo_pdm_plan import ModeloPDMPlan
from plan.plan_pdm.plano_pdm import PlanoPDM
from plan.planeador import Planeador

"""
A classe PlaneadorPDM implementa o contrato Planeador.
É utilizada para planear a trajetória do agente com recurso à lógica de Markov.
Esta classe representa um planeador baseado em processos de decisao de Markov, adequado para agentes autonomos que atuam em ambientes onde a previsibilidade e a estrutura das transicoes podem ser modeladas de forma simbolica. 
A classe implementa a interface Planeador, assumindo a responsabilidade de gerar planos com base num modelo do ambiente e numa lista de estados objetivo. 
O planeamento e realizado a partir de um modelo do dominio que e convertido para um modelo PDM, considerando recompensas associadas aos estados alvo. 
A partir deste modelo, e aplicado um algoritmo iterativo que calcula a utilidade esperada de cada estado, tendo em conta um fator de desconto e uma tolerancia para convergencia. 
O parametro gama regula a importancia de recompensas futuras, influenciando a profundidade do planeamento. O delta_max define o limite de variacao para determinar quando o algoritmo deve parar. 
O resultado do planeamento e um plano composto por uma politica otima e a utilidade estimada de cada estado, encapsulado num objecto PlanoPDM.
"""

class PlaneadorPDM(Planeador):
    """
    Na inicialização da classe PlaneadorPDM, são definidos dois atributos: gama e dela_max.
    O atributo gama é uma variável correspondente ao fator de desconto, pois estabelece uma relação proporcionalmente inversa entre o custo e a recompensa esperada.
    Quanto maior o gama, a probabilidade de o agente se mover é maior, obtendo uma recompensa maior.
    """
    def __init__(self, gama=0.85, delta_max=1):
        self.__gama = gama
        self.__delta_max = delta_max
        
    def planear(self, modelo_plan, objectivos):
        if objectivos:
            modelo_pdm = ModeloPDMPlan(modelo_plan, objectivos)
            pdm = PDM(modelo_pdm, self.__gama, self.__delta_max)
            utilidade, politica = pdm.resolver()
            return PlanoPDM(utilidade, politica)
        
    @property
    def gama(self):
        return self.__gama
    
    @property
    def delta_max(self):
        return self.__delta_max