#include <stdio.h>

#define JUGADORVSPC 1
#define JUGADORVSJUGADOR 2

int main() {
    int tipoJuego;

    printf("Seleccione el tipo de juego\n");
    printf("1.- Jugador vs PC\n");
    printf("2.- Jugador vs Jugador\n");
    scanf("%d", &tipoJuego);

    switch(tipoJuego) {
        case JUGADORVSPC:
            // jugador contra PC
            break;
        case JUGADORVSJUGADOR:
            // jugador contra jugador
            break;
        default:
            // opcion ingresada inválida
            break;
    }

    return 0;
}