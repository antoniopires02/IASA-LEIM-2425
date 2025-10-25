package agente;

import ambiente.*;

public class Percepcao {
    /*
     * Implementação da propriedade read only do diagrama UML, relativo ao atributo
     * evento. A propriedade implica a leitura, e não escrita.
     */
    private Evento evento;

    public Evento getEvento() {
        return evento;
    }

    public Percepcao(Evento evento) {
        this.evento = evento;
    }
}