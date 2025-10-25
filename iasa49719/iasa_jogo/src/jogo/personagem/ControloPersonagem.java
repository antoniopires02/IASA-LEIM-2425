package jogo.personagem;

import agente.*;
import ambiente.Evento;
import jogo.ambiente.ComandoJogo;
import jogo.ambiente.EventoJogo;
import maqest.Estado;
import maqest.MaquinaEstados;

/*
 * A classe ControloPersonagem é dotada da capacidade inteligente do personagem do jogo, 
 * ou seja, é nela que estão presentes as transições possíveis que ocorrerão tendo em conta cada estado.
 * De acordo com a informação recebida pelos sensores(percepcao) / entrada, assim é tomada uma decisão (saída).
 * Daí a designação de modelo deliberativo.
 * Controlo - representa passo da execução a ser executado. 
 */

public class ControloPersonagem implements Controlo {

    private MaquinaEstados maqEst;

    public Estado getEstado() {
        return maqEst.getEstado();
    }

    /*
     * É no construtor que são definidos estados e ações que prosteriormente irão
     * ser utilizados nas transições, que posteriormente farão parte da máquinda de
     * Estados.
     * A lógica da implementação apoia-se no diagrama de transição de estado, pelo
     * que facilita a descrição e compreensão da dinâmica e comportamento do
     * sistema.
     */

    public ControloPersonagem() {
        Estado procura = new Estado("Procura");
        Estado inspeccao = new Estado("Inspecção");
        Estado observacao = new Estado("Observação");
        Estado registo = new Estado("Registo");

        Accao procurar = new Accao(ComandoJogo.PROCURAR);
        Accao aproximar = new Accao(ComandoJogo.APROXIMAR);
        Accao fotografar = new Accao(ComandoJogo.FOTOGRAFAR);
        Accao observar = new Accao(ComandoJogo.OBSERVAR);

        procura
                .transicao(EventoJogo.ANIMAL, observacao, aproximar)
                .transicao(EventoJogo.RUIDO, inspeccao, aproximar)
                .transicao(EventoJogo.SILENCIO, procura, procurar);

        inspeccao
                .transicao(EventoJogo.SILENCIO, procura)
                .transicao(EventoJogo.RUIDO, inspeccao, procurar)
                .transicao(EventoJogo.ANIMAL, observacao, aproximar);

        observacao
                .transicao(EventoJogo.FUGA, inspeccao)
                .transicao(EventoJogo.ANIMAL, registo, observar);

        registo
                .transicao(EventoJogo.FUGA, procura)
                .transicao(EventoJogo.FOTOGRAFIA, procura)
                .transicao(EventoJogo.ANIMAL, registo, fotografar);

        maqEst = new MaquinaEstados(procura);
    }

    /*
     * O método processar recebe uma percepcao por parte dos sensores do agente e
     * daí extrai o evento associado.
     * de seguida manifesta a acção de acordo com o evento percecionado.
     * Retorna a ação enquadrada.
     * 
     */

    public Accao processar(Percepcao percepcao) {
        Evento evento = percepcao.getEvento();
        Accao accao = maqEst.processar(evento);
        mostrar();
        return accao;
    }

    // Mostra o estado corrente recorrendo ao método que permite ler o próprio nome.
    private void mostrar() {
        System.out.printf(" Estado: %s\n", getEstado().getNome());
    }
}