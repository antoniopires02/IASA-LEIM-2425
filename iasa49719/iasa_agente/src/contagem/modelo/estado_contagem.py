from lib.mod.estado import Estado

"""
Classe EstadoContagem

Esta classe herda da classe base Estado e representa os estados possíveis do problema "Contagem",
em que o estado é definido por um número inteiro. O valor do estado é armazenado como um atributo
privado e acessado através de uma propriedade. Embora o próprio número possa ser utilizado como 
identificador, é definido um método `id_valor()` que retorna o hash do valor, garantindo um ID único
e compatível com estruturas como dicionários ou conjuntos.
"""

class EstadoContagem(Estado):
    def __init__(self, valor):
        self.__valor = valor
    
    @property 
    def valor(self):
        return self.__valor

    def id_valor(self):
        return hash(self.__valor)
    