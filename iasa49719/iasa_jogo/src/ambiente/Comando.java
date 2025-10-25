package ambiente;

/*
Interface pública Comando
Interface com método correspondente a comandos que irão ser executados pela personagem.
Os métodos são definidos nesta classe e implementados numa classe aparte.
Possui um contrato funcional, independente de possíveis implementações.
O método mostrar permite visualizar comandos.

A interface tem relações de dependência com a interface Ambiente.
*/

public interface Comando {
    void mostrar();
}