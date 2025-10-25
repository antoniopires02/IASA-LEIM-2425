package ambiente;

/*
 * A interface Ambiente representa a Abstração de um ambiente que servirá de
 * base para o Jogo desenvolvido.
 * Nela estão presentes métodos, que correspondem a ações de um interveniente no
 * jogo.
 * Faz parte do modelo estrutural de ambiente.
 * Possui contratos funcionais (interfaces) independentes de possíveis
 * implementações.
 * Considerando um ambiente que evolui ao longo do tempo, onde é possível
 * executar comandos e observar eventos.
 * 
 * A interface tem relações de dependência com as interfaces Evento e Comando.
 */

public interface Ambiente {
    void evoluir();

    Evento observar();

    void executar(Comando comando);
}