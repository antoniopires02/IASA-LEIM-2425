from pee.melhor_prim.procura_aa import ProcuraAA
from plan.plan_pee.mod_prob.heur_dist import HeurDist
from plan.plan_pee.mod_prob.problema_plan import ProblemaPlan
from plan.plan_pee.plano_pee import PlanoPEE
from plan.planeador import Planeador

"""
Esta classe representa um planeador que utiliza um mecanismo de procura informada para a construcao de planos baseados em exploracao do espaco de estados.
Herda da interface Planeador, utiliza uma procura do tipo AA para encontrar um caminho desde o estado inicial ate a um estado objetivo definido. 
No processo de planeamento, verifica se existem objetivos, define o estado final e cria um problema de planeamento associado. 
Posteriormente, uma heuristica que calcula a distancia ate ao objetivo e usada para guiar a procura. 
Se a procura encontrar uma solucao, esta e encapsulada num plano especifico para o metodo PEE. 
"""


class PlaneadorPEE(Planeador):
    def __init__(self):
        self.__mec_pee = ProcuraAA()
    
    def planear(self, modelo_plan, objectivos):
        if objectivos:
            estado_final = objectivos[0]
            problema = ProblemaPlan(modelo_plan, estado_final)
            heuristica = HeurDist(estado_final)
        
            solucao = self.__mec_pee.procurar(problema, heuristica)
        
            if solucao:
                return PlanoPEE(solucao)