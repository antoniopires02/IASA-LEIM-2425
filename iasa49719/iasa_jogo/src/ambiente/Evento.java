package ambiente;

/*
Interface pública Evento
Os métodos são definidos nesta classe e implementados numa classe aparte.
Possui um contrato funcional, independente de possíveis implementações.
O método mostrar permite visualizar eventos.

A interface tem relações de dependência com a interface Ambiente.
*/

public interface Evento {
    void mostrar();
}