import pygame

from hallar_coordenadas import hallar_coordenadas_centrales_pantalla, hallar_radio, hallar_tam_celdas


def dibujar_celdas ( filas_matriz, columnas_matriz, ancho_pantalla, alto_pantalla, pantalla, color_divisiones ):
    tam_celda_eje_x, tam_celda_eje_y = hallar_tam_celdas( filas_matriz, columnas_matriz, ancho_pantalla, alto_pantalla )
    for i in range( 1, columnas_matriz ):
        pygame.draw.line( pantalla, color_divisiones, ( tam_celda_eje_x * i, 0 ), ( tam_celda_eje_x * i, alto_pantalla ), width=2 )
    for i in range( 1, filas_matriz ):
        pygame.draw.line( pantalla, color_divisiones, ( 0, tam_celda_eje_y * i ), ( ancho_pantalla, tam_celda_eje_y * i ), width=2 )

def dibujar_automatas_de_matriz ( filas_matriz: int, columnas_matriz: int, ancho_pantalla: float, alto_pantalla: float, pantalla, matriz, color_automata_celular ):
    tam_celda_eje_x, tam_celda_eje_y = hallar_tam_celdas( filas_matriz, columnas_matriz, ancho_pantalla, alto_pantalla )

    for i in range( filas_matriz ):
        for j in range( columnas_matriz ):
            if matriz[ i ][ j ] == 1:
                coordenadas_cetro = hallar_coordenadas_centrales_pantalla( tam_celda_eje_x, tam_celda_eje_y, i, j )
                radio = hallar_radio( tam_celda_eje_x, tam_celda_eje_y )
                pygame.draw.circle( pantalla, color_automata_celular, coordenadas_cetro, radio )
