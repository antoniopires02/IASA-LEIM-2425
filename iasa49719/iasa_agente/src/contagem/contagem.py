###
from modelo.heuristica_contagem import HeuristicaContagem
from modelo.problema_contagem import ProblemaContagem
from lib.pee.melhor_prim.procura_aa import ProcuraAA
from lib.pee.melhor_prim.procura_sofrega import ProcuraSofrega
from lib.pee.prof.procura_profundidade import ProcuraProfundidade
from lib.pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from lib.pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim
from lib.pee.prof.procura_prof_iter import ProcuraProfIter
from lib.pee.prof.procura_prof_lim import ProcuraProfLim
from lib.pee.larg.procura_largura import ProcuraLargura

VALOR_INICIAL = 0
VALOR_FINAL = 9
INCREMENTOS = [1, 2, -1]

problema = ProblemaContagem(VALOR_INICIAL, 
                            VALOR_FINAL, 
                            INCREMENTOS)

heuristica = HeuristicaContagem(VALOR_FINAL)

#mec_proc = ProcuraLargura() # Procura em Largura é completa e ótima. Produz a solução com o número mínimo de passos. O custo é determinado pelo incremento ao quadrado.
# Todos os nós processados ficam em memória.

#mec_proc = ProcuraProfundidade()

#mec_proc = ProcuraProfLim(5)

#mec_proc = ProcuraProfIter(50)

#mec_proc = ProcuraCustoUnif()

#mec_proc = ProcuraSofrega() 

mec_proc = ProcuraAA()

solucao = mec_proc.procurar(problema, heuristica)


if solucao:
    print(f"Dimensão: {solucao.dimensao}")
    print(f"Custo: {solucao.custo}")
    print("")
    print(f"Nós processados: {mec_proc.nos_processados}")
    print(f"Nós em memória: {mec_proc.nos_em_memoria}")
    print("")
    print(f"Estados repetidos: {mec_proc.estados_repetidos}")
    """
    print("Passos:")
    for passo in solucao:
        print(f"- Estado: {passo.estado.valor}")
        print(f"- Operador: {passo.operador.incremento}")
    """

"""
Apresentar no ecra o no numero de estados repetidos durante a procura.
Intervi na classe MecanismoProcura, na funcao _expandir, para contar o numero de estados repetidos.
Não consegui acabar no tempo estabelecido, mas a ideia era criar um atributo estados_repetidos na classe MecanismoProcura, para depois contar os estados repetidos.
"""