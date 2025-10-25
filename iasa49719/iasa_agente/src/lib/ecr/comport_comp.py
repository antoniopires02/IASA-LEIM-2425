from abc import ABC, abstractmethod
from .comportamento import Comportamento

"""
Comportamento pode ser uma reação simples ou comportamento composto. 
Se for composto tem outros comportamentos dentro do mesmo e tem um mecanismo de seleção de ação.
A classe abstrata ComportComp herda Comportamento.
"""

class ComportComp(Comportamento):
    
    """ Comportamento composto quando ativado recebe percepao. Tem dentro varias comportamentos.
        A percepcao e encaminhada para os comportamentos internos.
        cada um deles vai gerar uma ação. 
        As ações são guardadas e depois aplicadas
    """
    
    def __init__(self, comportamentos):
        self.__comportamentos = comportamentos
        
    """ 
    O método activar implementa a lógica presente na página 13 do módulo 06-arq-react-1 das folhas de apoio.
    É recebida uma percepção do exterior de diversos comportamentos, de seguida é ativada no comportamento e depois selecionada.
    Serialização.
    """
    def activar(self, percepcao):
        accoes = []
        for comportamento in self.__comportamentos:
            accao = comportamento.activar(percepcao)
            if accao: # if is not None (None é uma marca, não um valor)
                accoes.append(accao)
        if accoes:
            return self.seleccionar_accao(accoes)
    
    @abstractmethod
    def seleccionar_accao(self, accoes):
        """Selecionar Ação"""