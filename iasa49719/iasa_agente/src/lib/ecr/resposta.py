class Resposta:
    
    def __init__(self, accao):
        self._accao = accao
        
    """ 
    Método activar retorna uma ação com base na intensidade que por sua vez é definida como prioridade.
    Percepções (agregados de estímulos) para tomada de decisão e daí surge uma resposta
    percepcao : observa a info do ambiente, pode ter muitos estimulos (pode ativar muitas respostas)
    """
    
    def activar(self, percepcao, intensidade=0):
        if percepcao is not None:
            self._accao.prioridade = intensidade
            return self._accao
