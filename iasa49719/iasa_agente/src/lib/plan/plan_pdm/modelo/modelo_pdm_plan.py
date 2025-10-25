from pdm.modelo.modelo_pdm import ModeloPDM
from plan.modelo.modelo_plan import ModeloPlan

"""
Esta classe combina funcionalidades de planeamento simbolico com modelacao de processos de decisao de Markov, sendo adequada para sistemas autonomos que requerem selecao de acoes com base em recompensas.
A classe herda das estruturas ModeloPlan e ModeloPDM, permitindo reutilizar metodos de obtencao de estados, operacoes e estado atual, enquanto introduz um modelo deterministico de transicoes baseado em accoes aplicadas sobre estados.
Durante a inicializacao, e definido um conjunto de transicoes validas, associando pares de estado e accao ao estado resultante da sua aplicacao. Tambem sao definidos os estados objetivo e o valor da recompensa maxima atribuida quando um desses estados e alcancado.
O metodo S retorna todos os estados disponiveis. A funcao A determina as acoes validas num dado estado, sendo vazia se esse estado for objetivo. 
A funcao T implementa a funcao de transicao deterministica do PDM, indicando se uma accao leva exatamente ao estado esperado. 
A funcao R calcula a recompensa com base no estado final, atribuindo rmax se este for um objetivo, ou penalizando com o custo da accao caso contrario. 
O metodo suc devolve o proximo estado possivel, se existir.
Este tipo de classe e usado em arquitecturas deliberativas onde e possivel planear e executar politicas otimizadas em ambientes previsiveis.
"""


class ModeloPDMPlan(ModeloPlan, ModeloPDM):
    def __init__(self, modelo_plan, objectivos, rmax=1000):
        self.__modelo_plan = modelo_plan
        self.__objectivos = objectivos
        self.__rmax = rmax
        self.__transicoes = {}
        for s in self.obter_estados():
            for a in self.obter_operadores():
                sn = a.aplicar(s)
                if sn in self.obter_estados():
                    self.__transicoes[(s, a)] = sn
    
    def obter_estado(self):
        return self.__modelo_plan.obter_estado()
    
    def obter_estados(self):
        return self.__modelo_plan.obter_estados()
        
    def obter_operadores(self):
        return self.__modelo_plan.obter_operadores()
        
    def S(self):
        return self.obter_estados()
    
    def A(self, s):
        return self.obter_operadores() if s not in self.__objectivos else []
    
    def T(self, s, a, sn):
        sn = self.__transicoes.get((s, a))
        return 1 if sn is not None else 0

    def R(self, s, a, sn):
        custo = a.custo(s, sn)
        if custo is not None:
            if sn in self.__objectivos:
                return self.__rmax - custo
            else:
                return custo  
        return None
    
    def suc(self, s, a):
        sn = self.__transicoes.get((s, a))
        return [sn] if sn is not None else []
        
    @property
    def rmax(self):
        return self.__rmax
    
    @property
    def objectivos(self):
        return self.__objectivos