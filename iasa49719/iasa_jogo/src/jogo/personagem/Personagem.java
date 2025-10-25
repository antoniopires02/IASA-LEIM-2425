package jogo.personagem;

import agente.Agente;
import jogo.ambiente.AmbienteJogo;

/* Personagem herda as características da classe Agente. 
 * 
*/
public class Personagem extends Agente {

    public Personagem(AmbienteJogo ambiente) {
        super(ambiente, new ControloPersonagem());
    }
}