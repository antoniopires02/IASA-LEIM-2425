package maqest;

import agente.Accao;

public class Transicao {

    /*
     * Classe fulcral para implementação do sistema visto ser responsável pelo
     * processamento dos dados relativos ao estado sucessor e ação.
     */

    private Estado estadoSucessor;

    // Propriedade read only de estadoSucessor.
    public Estado getEstadoSucessor() {
        return estadoSucessor;
    }

    private Accao accao;

    // Propriedade read only de accao.
    public Accao getAccao() {
        return accao;
    }

    public Transicao(Estado estadoSucessor, Accao accao) {
        this.estadoSucessor = estadoSucessor;
        this.accao = accao;
    }
}
