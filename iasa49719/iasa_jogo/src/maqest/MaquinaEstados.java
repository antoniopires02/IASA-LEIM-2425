package maqest;

import agente.Accao;
import ambiente.Evento;

public class MaquinaEstados {
    /*
     * Para evitar efeito teia e simplificar o sistema é criada uma máquina de
     * estados para uma maior eficiência e organização do código em si
     * É constituída por entradas , saídas e estados.
     * De acordo com o modelo teórico apresentado em aula os componentes são:
     * Modelo formal de computação
     * Lambda função de saída, em função do estado.
     * Delta transição de estado, com base no estado anterior.
     * Dados de entrada e dados de saída. Os valores são representados por símbolos,
     * formando alfabetos (de entrada e de saída).
     * Sigma representa o alfabeto de Entrada.
     * Z representa o alfabeto de Saída.
     * Letras maiúsculas representam conjuntos, minúsculas instâncias.
     * Conjuntos de estados Q, estados que estão na memória.
     * 
     * delta(q:Q, s:S): Q
     * lambda(q:Q, s:S): Z
     * 
     * Conjunto de Entrada - Eventos
     * Conjunto de Saída - Ações
     * Conjunto de Estados - Estados
     * 
     * Cada estado tem transições associadas e cada transição tem a indicação do
     * estado sucessor e guarda ação a executar.
     * Estado pode processar eventos e perante os eventos sao produzidas transições
     * que tem o estado sucessor e a ação.
     * No estado arranjar maneira de definir transicoes associadas a um estado
     */

    private Estado estado;

    public Estado getEstado() {
        return estado;
    }

    public MaquinaEstados(Estado estadoInicial) {
        this.estado = estadoInicial;
    }

    public Accao processar(Evento evento) {
        Transicao transicao = estado.processar(evento);
        if (transicao != null) {
            estado = transicao.getEstadoSucessor();
            return transicao.getAccao();
        } else {
            return null;
        }
    }
}