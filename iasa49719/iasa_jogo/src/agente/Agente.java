package agente;

import ambiente.*;

/* 
Classe abstrata Agente
O Agente é um elemento do Modelo concetual (abstrato).
Agente é uma entidade computacional que interage com o computador através de sensores e atuadores. 
Opera para que a finalidade seja executada, formando percepções internas, e processando as percepções de forma a gerar ações a partir dos atuadores.
Primeiro o Agente interage com o ambiente e percepciona o ambiente, de seguida processa de acordo com o sistema. 
Posteriormente gera uma ação, e a ação sobre o processo atuar gera ações no ambiente.
*/

public abstract class Agente {

    private Ambiente ambiente;
    private Controlo controlo;

    public Agente(Ambiente ambiente, Controlo controlo) {
        this.ambiente = ambiente;
        this.controlo = controlo;
    }

    /*
     * A lógica associada ao método executar teve origem no diagrama de atividade.
     * É implementado o Modelo de Dinâmica com transferência de informação entre
     * atividades(Fluxo de objetos), referenciado no módulo 05-introd-eng-soft-3,
     * página 20.
     * Ocorre a perceção por parte do agente do ambiente, processa a informação, já no lado do Controlo, e
     * por fim atua (novamente no Agente).
     * Representa um passo de execução do Agente.
     */
    public void executar() {
        Percepcao percepcao = percepcionar();
        Accao accao = controlo.processar(percepcao);
        actuar(accao);
    }

    // O agente observa o ambiente e cria uma perceção de acordo com o evento atual.
    protected Percepcao percepcionar() {
        Evento evento = ambiente.observar();
        return new Percepcao(evento);
    }

    protected void actuar(Accao accao) {
        if (accao != null) {
            ambiente.executar(accao.getComando());
        }
    }
}