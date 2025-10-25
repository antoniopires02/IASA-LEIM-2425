from .comport_comp import ComportComp

""" 
Selecao de acao:
- acoes em paralelo
- se nao possivel, escolher 
(selecao de acao por prioridade) 
Associado a cada respota há um prioridade.

Criterio de prioridade:
A prioridade dos comportamentos internos é fixa.
Hierarquia de subsunção: topo da hierarquia substitui e suprime ação de menor prioridade.
Ordem é definida pela ordem de definição dos comportamentos.
"""
"""
    Tendo em conta as percepções recebidas pelos sensores do agente assim as reações por parte do mesmo.
    Para este efeito é necessária a seleção de ações.
    Porém sempre com base em prioridades. 
    Estas são definidas e assim respeitadas.
    A classe examina a lista de ações disponíveis
    e retorna a ação com a maior prioridade para ser executada pelo agente.
"""

class Prioridade(ComportComp):
    
    """ 
    Por forma a completar o método seleccionar_accao para efeito de retorno de ação com maior prioridade
    Itera sobre ações disponíveis, mantendo o controlo da acao com a maior prioridade encontrada.
    Após iteração retorna a ação.
    A função analisa a lista de ações fornecida e seleciona aquela com a
    maior prioridade.
    O argumento 'key' define qual o parâmetro da função max que deve ser aplicado,
    permitindo obter a ação de maior prioridade.
    """        
    
    def seleccionar_accao(self, accoes):
        
        """
        prioridade_actual = -float("inf")
        accao_maior_prioridade = None
        for accao in accoes:
            if accao.prioridade > prioridade_actual:
                accao_maior_prioridade = accao
                prioridade_actual = accao.prioridade
        return accao_maior_prioridade
        """
        if accoes:
            return max(accoes, key = lambda accao : accao.prioridade)
    