"""
A classe MecUtil implementa o Mecanismo de Utilidade, que é responsável por calcular a utilidade.
A utilidade reflete o impacto acumulado da evolução da situação atual, traduzindo-se no que se conhece como recompensa. 
A partir da sequência de estados gerada ao longo da evolução, conseguimos determinar essas recompensas. 
No contexto de um determinado estado, as recompensas podem ser adquiridas ou perdidas conforme a ação do agente. 
O valor da recompensa é finito, podendo ser positivo ou negativo, dependendo se o agente recebe um benefício ou é penalizado.
"""

class MecUtil:
    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__gama = gama
        self.__delta_max = delta_max
        
    def utilidade(self):
        S, A = self.__modelo.S, self.__modelo.A
        
        U = {s: 0 for s in S()}
        
        while True:
            Uant = U.copy()
            delta = 0
            
            for s in S():
                U[s] = max([self.util_accao(s, a, Uant) for a in A(s)], default=0)
                delta = max(delta, abs(U[s] - Uant[s]))
                
            if delta < self.__delta_max:
                break
            
        return U
            
    
    def util_accao(self, s, a, U):
        T, R, suc = self.__modelo.T, self.__modelo.R, self.__modelo.suc
        return sum(T(s, a, sn) * (R(s, a, sn) + self.__gama * U[sn])
                   for sn in suc(s, a))
    
    @property
    def delta_max(self):
        return self.__delta_max
    
    @property
    def gama(self):
        return self.__gama
        