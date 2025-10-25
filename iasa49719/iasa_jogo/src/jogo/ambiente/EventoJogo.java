package jogo.ambiente;

import ambiente.Evento;

//EventoJogo é um enumerado onde estão presentes os eventos do jogo.

public enum EventoJogo implements Evento {
    SILENCIO, RUIDO, ANIMAL, FUGA, FOTOGRAFIA, TERMINAR;

    // Implementação do contrato definido na interface Evento.
    @Override
    public void mostrar() {
        System.out.printf("\n Evento: %s\n", this);
    }
}
