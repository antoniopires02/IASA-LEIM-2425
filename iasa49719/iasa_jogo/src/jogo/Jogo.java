package jogo;

import jogo.ambiente.AmbienteJogo;
import jogo.ambiente.EventoJogo;
import jogo.personagem.Personagem;

//A classe Jogo é uma classe dotada de main de modo a executar o jogo.
//Implemantação do Modelo de interação.

public class Jogo {

    /*
     * Ao contrário da Arquitetura apresentada, os atributos da classe são
     * estáticos, não private.
     * Trata-se da inferência que ocorre, já que são variáveis posteriormente
     * inicializadas no main, um método static.
     */
    private static Personagem personagem;
    private static AmbienteJogo ambiente;

    public static void main(String[] args) {
        ambiente = new AmbienteJogo();
        personagem = new Personagem(ambiente);
        executar();
    }

    // Tal como na página 9 do módulo P1-iasa-proj este troço de código representa o
    // loop de execução do método executar.
    // O método é estático pois está definido no main.
    private static void executar() {
        /*
         * Só é gerado um novo Evento, após o ambiente ter evoluído, logo implementa-se
         * um ciclo do while.
         * Primeiro implementa o evoluir e depois verifica a condição.
         */
        do {
            ambiente.evoluir();
            personagem.executar();
        } while (ambiente.getEvento() != EventoJogo.TERMINAR);
    }

}
