from .mec_delib import MecDelib
from agente.controlo_delib.modelo.modelo_mundo import ModeloMundo

"""
A classe ControloDelib define o mecanismo de controlo deliberativo. É dotado de memória na definição do comportamento do agente.
O controlo deliberativo é um mecanismo que permite ao agente tomar decisões com base em informações do ambiente e em objectivos definidos.
Classe Controlo Deliberativo que implementa um agente com controlo deliberativo, onde a memória e raciocínio são
centrais para a tomada de decisão.

O construtor inicializa:
- um planeador, que cria planos baseados no modelo do mundo e nos objetivos,
- o modelo do mundo que representa internamente o ambiente,
- um mecanismo deliberativo que define e atualiza os objetivos do agente,
- uma lista de objetivos e um plano corrente (o plano que o agente está a executar).

O método principal processar(percepcao) executa o ciclo do controlo deliberativo:
1. Assimila a perceção atual no modelo do mundo.
2. Decide se deve reconsiderar o plano atual (se não existir ou se o modelo foi alterado).
3. Se reconsiderar, chama o mecanismo deliberativo para atualizar objetivos.
4. Usa o planeador para gerar um novo plano com base nos objetivos.
5. Atualiza a visualização com o modelo, plano e objetivos.
6. Executa a próxima ação do plano (obtendo o operador e a ação correspondente ao estado atual).
Se não houver operador para o estado atual, o plano é descartado.

Além disso, existem métodos privados para:
- Assimilar perceções,
- Decidir reconsideração do plano,
- Deliberar objetivos,
- Planear um novo plano,
- Executar a próxima ação do plano,
- Mostrar a visualização atual.

Este controlo permite ao agente agir de forma deliberativa, baseando decisões e ações num modelo atualizado do ambiente
e numa sequência planejada de ações para alcançar objetivos.
"""

class ControloDelib:
    def __init__(self, planeador):
        self.__modelo_mundo = ModeloMundo()
        self.__mecanismo_delib = MecDelib(self.__modelo_mundo)
        self.__planeador = planeador
        self.__objetivos = None
        self.__plano = None
        
    def processar(self, percepcao):
        self.__assimilar(percepcao)
        if self.__reconsiderar():
            self.__deliberar()
            self.__planear()
        return self.__executar()
        
    def __assimilar(self, percepcao):
        self.__modelo_mundo.actualizar(percepcao)
    
    def __reconsiderar(self):
        return self.__modelo_mundo.alterado or not self.__plano 
        
    def __deliberar(self):
        # Delibera sobre a acao a executar
        self.__objetivos = self.__mecanismo_delib.deliberar()
    
    def __planear(self):
        # Planeia a acao a executar
        if self.__objetivos:
            self.__plano = self.__planeador.planear(self.__modelo_mundo, self.__objetivos)
        else:
            self.__plano = None
    
    def __executar(self):
        # Executa a acao planeada
        if self.__plano:
            estado = self.__modelo_mundo.obter_estado()
            operador = self.__plano.obter_accao(estado)
            if operador:
                return operador.accao
            else:
                self.__plano = None
    
    def mostrar(self, vista):
        # Mostra a acao planeada
        vista.limpar()
        self.__modelo_mundo.mostrar(vista)
        if self.__plano:
            self.__plano.mostrar(vista)
        if self.__objetivos:
           for objectivo in self.__objetivos:
               vista.marcar_posicao(objectivo.posicao)
    