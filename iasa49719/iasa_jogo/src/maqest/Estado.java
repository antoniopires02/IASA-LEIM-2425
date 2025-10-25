package maqest;

import java.util.HashMap;
import java.util.Map;

import agente.Accao;
import ambiente.Evento;

public class Estado {

    /*
     * A classe Estado representa o elemento da Máquina de Estados responsável por
     * cumprir ações em loop até que alguma condição altere o sistema.
     * Através desta classe é possível criar um Estado do agente com o respetivo
     * nome
     * que transita para um próximo estado.
     * É possível através de um HashMap que é utilizado como recurso para a sucessão
     * entre estados e determinadas ações do agente na transição.
     * Cada método transição define a função delta e a função lambda, sendo
     * "transicoes" o suporte de implementação das funções.
     */

    private String nome;

    // Propriedade read only do elemento nome.
    public String getNome() {
        return nome;
    }

    // Contentor com a chave do tipo Evento onde serão definidas 0 ou mais transições. 
    private Map<Evento, Transicao> transicoes;

    // Construtor da classe Estado onde é inicializado o atributo nome e instanciado o contentor de transições.
    public Estado(String nome) {
        this.nome = nome;
        transicoes = new HashMap<Evento, Transicao>();
    }

    public Transicao processar(Evento evento) {
        return transicoes.get(evento);
    }

    /*
     * Encadeamento de ativação.
     * O método transição mapeia uma transição ao evento definindo o estado sucessor
     * do estado atual tratado.
     * É uma transição composta visto ser resposta a um evento no ambiente.
     */
    public Estado transicao(Evento evento, Estado estadoSucessor) {
        transicoes.put(evento, new Transicao(estadoSucessor, null));
        return this;
    }

    public Estado transicao(Evento evento, Estado estadoSucessor, Accao accao) {
        transicoes.put(evento, new Transicao(estadoSucessor, accao));
        return this;
    }

}
