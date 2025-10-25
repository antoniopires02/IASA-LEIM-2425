package jogo.ambiente;

import ambiente.*;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/*
 * Classe AmbienteJogo implementa a Interface Ambiente do package ambiente.
 * Possui um construtor que será responsável pela criação do próprio ambiente virtual.
 * Na sequência da Aula1 foi implementada a classe AmbienteJogo que implementa a interface Ambiente.
 * Nela estão presentes os princípios de acoplamento e coesão, relacionando-se com enumerações Java
 * que irão representar eventos e comandos do jogo. 
 * Tal como o fornecido pela interface possui recursos para efeitos de input do user em runtime,
 * evolução do ambiente, execução do mesmo gerar eventos fornecidos e observar o evento em execução.
 */

public class AmbienteJogo implements Ambiente {

    // Atributo evento da classe
    private EventoJogo evento;

    // Segundo a lógica presente no UML implementa a propriedade read only do evento
    public EventoJogo getEvento() {
        return evento;
    }

    // Contentor de eventos
    private Map<String, EventoJogo> eventos;

    Scanner scanner = new Scanner(System.in);

    /*
     * Construtor da classe
     * no construtor é criado um HashMap com eventos representados por Strings.
     * correspondendo cada String a um evento.
     */
    public AmbienteJogo() {
        eventos = new HashMap<String, EventoJogo>();
        eventos.put("s", EventoJogo.SILENCIO);
        eventos.put("r", EventoJogo.RUIDO);
        eventos.put("a", EventoJogo.ANIMAL);
        eventos.put("f", EventoJogo.FUGA);
        eventos.put("o", EventoJogo.FOTOGRAFIA);
        eventos.put("t", EventoJogo.TERMINAR);

    }

    // Método da Interface Ambiente que implementa o contrato funcional
    @Override
    public void evoluir() {
        evento = gerarEvento();
    }

    // Método da Interface Ambiente que implementa o contrato funcional
    @Override
    public Evento observar() {
        if (evento != null) {
            evento.mostrar();
        }
        return evento;
    }

    // Método da Interface Ambiente que implementa o contrato funcional Comando.
    // Mostra no ecrã o nome do comando.
    @Override
    public void executar(Comando comando) {
        comando.mostrar();
    }

    // Método privado para gerar Eventos
    /*
     * Neste método foi utilizada programação declarativa para gerar o mesmo.
     * Em que é pedido ao user para escolher um evento e recebe utilizando o metodo
     * get de eventos.
     */
    private EventoJogo gerarEvento() {
        System.out.print("\n Evento? ");
        String codigoEvento = scanner.next();
        return eventos.get(codigoEvento);
    }

}