package agente;

import ambiente.*;

public class Accao {

    private Comando comando;

    public Comando getComando() {
        return comando;
    }

    public Accao(Comando comando) {
        this.comando = comando;
    }
}