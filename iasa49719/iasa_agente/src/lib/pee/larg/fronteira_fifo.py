from pee.mec_proc.fronteira import Fronteira

"""
Classe que implementa uma fronteira com politica de insercao do tipo FIFO, ou seja, os nos sao processados pela ordem em que sao inseridos. 
Esta classe herda da interface Fronteira e redefine o metodo de insercao para garantir que os novos elementos sao colocados no inicio da lista, fazendo com que os elementos mais antigos sejam removidos primeiro. 
Este comportamento e tipico de estruturas de dados como filas, sendo util em algoritmos de pesquisa nao informada onde a ordem de exploracao deve ser mantida de forma justa.
"""

class FronteiraFIFO(Fronteira):
    def inserir(self, no):
        super()._nos.insert(0, no)
        
