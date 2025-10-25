from abc import ABC, abstractmethod

'''
A classe Problema encapsula o problema a ser resolvido. 
Possui um estado inicial e uma lista de operadores aplicáveis. 
A classe é abstrata e exige a implementação do método objetivo(), que verifica se um estado é um estado objetivo, 
ou seja, se é uma solução para o problema. Além disso, fornece métodos para acessar o estado inicial e a lista de operadores, 
garantindo assim o encapsulamento dos detalhes do problema e facilitando o uso por algoritmos de procura genéricos.
'''

class Problema(ABC):
    
    def __init__(self, estado_inicial, operadores):
        assert(len(operadores) >= 1), "Deve haver pelo menos um operador"
        self.__estado_inicial = estado_inicial
        self.__operadores = operadores
    
    @abstractmethod
    def objectivo(self, estado):
        """Objectivo"""
    
    @property
    def estado_inicial(self):
        return self.__estado_inicial
    
    # len(operadores) >= 1
    @property
    def operadores(self):
        return self.__operadores
    
    