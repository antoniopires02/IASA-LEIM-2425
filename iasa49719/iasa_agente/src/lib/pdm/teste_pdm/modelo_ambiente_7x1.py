from pdm.modelo.modelo_pdm import ModeloPDM
from pdm.pdm import PDM


class ModeloAmbiente7X1 (ModeloPDM):
    
    def __init__(self):
        self.__S = list([1, 2, 3, 4, 5, 6, 7])
        self.__A = list(['<-' , '->'])
        self.__T = {
            (1, '<-', 1): 0,
            (1, '->', 2): 0,
            (2, '<-', 1): 1,
            (2, '->', 3): 1,
            (3, '<-', 2): 1,
            (3, '->', 4): 1,
            (4, '<-', 3): 1,
            (4, '->', 5): 1,
            (5, '<-', 4): 1,
            (5, '->', 6): 1,
            (6, '<-', 5): 1,
            (6, '->', 7): 1,
            (7, '<-', 6): 0,
            (7, '->', 7): 0 
        }
        
        self.__R = {
            (1, '<-', 1): 0,
            (1, '->', 2): 0,
            (2, '<-', 1): -1,
            (2, '->', 3): 0,
            (3, '<-', 2): 0,
            (3, '->', 4): 0,
            (4, '<-', 3): 0,
            (4, '->', 5): 0,
            (5, '<-', 4): 0,
            (5, '->', 6): 0,
            (6, '<-', 5): 0,
            (6, '->', 7): 1,
            (7, '<-', 6): 0,
            (7, '->', 7): 0 
        }
        
        self.__transicoes = {(s, a): sn for (s, a, sn) in self.__T if s not in [1, 7]}
        
        """
        T(s, a, s'): [0, 1]
        s: S
        a: A 
        s' : S
        (s, a, s') = S X A(s) X S
        """
        
    
    def S(self):
        return self.__S
    
    
    def A(self, s):
        return self.__A
        
    
    def T(self, s, a, sn):
        return self.__T.get((s, a, sn), 0)
        
    
    def R(self, s, a, sn):
        return self.__R.get((s, a, sn), 0)
        
    """
    Política para o estado s dá ação
    A Utilidade do estado s dá o valor
    """
    def suc(self, s, a):
        # Gera o estado sucessor que resulta de realizar a ação a no estado s
        sn = self.__transicoes.get((s, a))
        return [sn] if sn else []


if __name__ == "main":
    modelo_pdm = ModeloAmbiente7X1()
    pdm = PDM(modelo_pdm, 0.5, 0.0)
    utilidade, politica = pdm.resolver()
    print(f"\nUtilidade: {utilidade}")
    print(f"\nPolítica: {politica}\n")