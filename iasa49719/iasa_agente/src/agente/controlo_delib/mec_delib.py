from sae import Elemento

"""
Classe Mecanismo Deliberado que representa o mecanismo responsável pelo controlo dos objetivos do agente.

Esta classe:
- Recebe o modelo do mundo para interagir com o ambiente e obter informações sobre estados e elementos.
- Tem uma função principal "deliberar" que devolve a lista de objetivos atuais do agente.
- Os objetivos, neste contexto, correspondem às posições no ambiente onde existem alvos (Elemento.ALVO).
- A lista de objetivos é ordenada pela distância ao estado atual do agente, para priorizar os alvos mais próximos.
"""

class MecDelib:
    def __init__(self, modelo_mundo):
        self.__modelo_mundo = modelo_mundo
        
    def deliberar(self):
        objectivos = self.__gerar_objectivos()
        if objectivos:
            return self.__seleccionar_objectivos(objectivos)
        
    def __gerar_objectivos(self):
        return [estado for estado in self.__modelo_mundo.obter_estados()
                if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO]
        
    def __seleccionar_objectivos(self, objectivos):
        if objectivos:
            objectivos.sort(key=self.__modelo_mundo.distancia)
        return objectivos