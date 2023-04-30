import sys
import pygame

from hallar_coordenadas import establecer_automata_en_matriz


def detectar_click ( evento, filas_matriz, columnas_matriz, ancho_pantalla, alto_pantalla, matriz ):
    if evento.type == pygame.MOUSEBUTTONDOWN:
        if evento.button == 1:
            establecer_automata_en_matriz( filas_matriz, columnas_matriz, ancho_pantalla, alto_pantalla, evento.pos, matriz )

def detectar_cerrado ( evento ):
    if evento.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


