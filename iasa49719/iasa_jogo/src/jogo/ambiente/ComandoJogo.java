package jogo.ambiente;

import ambiente.Comando;

//ComandoJogo é um enumerado onde estão presentes os comandos do jogo.

public enum ComandoJogo implements Comando {
    PROCURAR, APROXIMAR, OBSERVAR, FOTOGRAFAR;

    // Implementação do contrato definido na interface Comando.
    @Override
    public void mostrar() {
        System.out.printf(" Comando: %s\n", this);
    }
}
