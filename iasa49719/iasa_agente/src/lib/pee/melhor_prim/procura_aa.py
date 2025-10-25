from pee.melhor_prim.aval.avaliador_aa import AvaliadorAA
from .procura_informada import ProcuraInformada

"""
Classe que implementa o metodo de procura informada conhecido como procura AA. Esta abordagem baseia-se na avaliacao 
dos nos a expandir utilizando uma funcao heuristica combinada com o custo acumulado, promovendo a seleccao de caminhos 
promissores com base em conhecimento antecipado do dominio. A classe herda da estrutura generica de procura informada 
e especifica o uso do avaliador AA como estrategia de seleccao, que e fornecido no momento da inicializacao. 
"""
#prioridade é o custo do nó g + heuritistica

class ProcuraAA(ProcuraInformada):
    def __init__(self):
        super().__init__(AvaliadorAA())