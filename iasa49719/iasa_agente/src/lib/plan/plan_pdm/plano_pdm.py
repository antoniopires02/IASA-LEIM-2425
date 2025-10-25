from plan.plano import Plano

"""
A classe PlanoPDM implementa o contrato Plano. 
É útil do ponto de vista do planeamento dos movimentos do agente.
Segue a lógica de Markov tendo em consideração a utilizade e a política.
Utilidade é a recompensa esperada de um estado, enquanto que a política é o conjunto de ações que o agente deve tomar para maximizar essa recompensa.

Esta classe representa um plano gerado com base em politica e utilidade calculadas a partir de um processo de decisao de Markov. 
A classe implementa a interface Plano e permite a selecao de accoes para um determinado estado com base numa politica previamente optimizada. 
A utilidade de cada estado tambem esta disponivel e pode ser utilizada para fins de visualizacao ou interpretacao do raciocinio do agente. 
Este tipo de plano e adequado para sistemas autonomos onde e possivel calcular antecipadamente a melhor accao a executar em cada estado, garantindo assim comportamento racional orientado para a maximizacao de recompensa esperada ao longo do tempo.
"""

class PlanoPDM(Plano):
    def __init__(self, utilidade, politica):
        self.__utilidade = utilidade
        self.__politica = politica
    
    def obter_accao(self, estado):
        if self.__politica:
            return self.__politica.get(estado)
        
    def mostrar(self, vista):
        if self.__politica:
            # Mostrar utilidade
            for estado, valor in self.__utilidade.items():
                vista.mostrar_valor_posicao(estado.posicao, valor)
                
            # Mostrar politica
            for estado, accao in self.__politica.items():
                vista.mostrar_vector(estado.posicao, accao.ang)
        
    @property
    def utilidade(self):
        return self.__utilidade
    
    @property
    def politica(self):
        return self.__politica