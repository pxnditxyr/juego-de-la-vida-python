import pygame
from deteccion_eventos import detectar_cerrado, detectar_click, detectar_pausa
from dibujado import dibujar_automatas_de_matriz, dibujar_celdas
from generar_matriz import generar_matriz, generar_matriz_aleatoria
from time import sleep

import copy

from generar_reglas import generar_regla_0, generar_regla_11, generar_regla_24, generar_regla_25, generar_regla_34, generar_regla_1, generar_regla_15, generar_regla_9

pygame.init()

FILAS_MATRIZ = 16
COLUMNAS_MATRIZ = 25

ANCHO_PANTALLA = 1200
ALTO_PANTALLA = 600

COLOR_FONDO = ( 33, 33, 33 )
COLOR_DIVISIONES = ( 255, 132, 0 )
COLOR_AUTOMATA_CELULAR = ( 248, 255, 219 )

def actualizar_pantalla ( pantalla, matriz ):
    pantalla.fill( COLOR_FONDO )
    dibujar_celdas( FILAS_MATRIZ, COLUMNAS_MATRIZ, ANCHO_PANTALLA, ALTO_PANTALLA, pantalla, COLOR_DIVISIONES )
    dibujar_automatas_de_matriz( FILAS_MATRIZ, COLUMNAS_MATRIZ, ANCHO_PANTALLA, ALTO_PANTALLA, pantalla, matriz, COLOR_AUTOMATA_CELULAR )

def contar_vecinos ( matriz, indice_i, indice_j, filas_matriz, columnas_matriz ):
    cantidad_vecinos = 0

    j_izquierda = columnas_matriz - 1 if indice_j == 0 else indice_j - 1
    j_derecha = 0 if indice_j == ( columnas_matriz - 1  ) else indice_j + 1
    i_arriba = filas_matriz - 1 if indice_i == 0 else indice_i - 1
    i_abajo = 0 if indice_i == ( filas_matriz - 1 ) else indice_i + 1

    cantidad_vecinos += matriz[ i_arriba ][ j_izquierda ]
    cantidad_vecinos += matriz[ i_arriba ][ indice_j ]
    cantidad_vecinos += matriz[ i_arriba ][ j_derecha ]
    cantidad_vecinos += matriz[ indice_i ][ j_izquierda ]
    cantidad_vecinos += matriz[ indice_i ][ j_derecha ]
    cantidad_vecinos += matriz[ i_abajo ][ j_izquierda ]
    cantidad_vecinos += matriz[ i_abajo ][ indice_j ]
    cantidad_vecinos += matriz[ i_abajo ][ j_derecha ]

    return cantidad_vecinos

def aplicar_reglas ( matriz ):
    filas_matriz = len( matriz )
    columnas_matriz = len( matriz[ 0 ] )

    # Se quita la referencia
    # a = [ 0, 0, 0 ]
    # b = [ *a ]

    # No se quita la referencia por que hay una lista adentro
    # a = [ [ 0, 0, 0 ] ]
    # b = [ *a ]
    # b[0][0] = 1
    # a -> [ [ 1, 0, 0 ] ]
    # b -> [ [ 1, 0, 0 ] ]

    # Deep Copy, Si se quita la referencia
    # a = [ [ [[][[0]]], 0, 0 ]  ]
    # for i in range( len( a ) ):
    #    b[ 0 ] = [ *a[ 0 ] ]
    # [ 0, 0, 0 ] -> [ *a[ 0 ] ] -> [ 0, 0, 0, ] -> b[ 0 ]

    nueva_matriz = copy.deepcopy( matriz )
    for i in range( filas_matriz ):
        for j in range( columnas_matriz ):
            nueva_matriz[ i ][ j ] = matriz[ i ][ j ]

    for i in range( filas_matriz ):
        for j in range( columnas_matriz ):
            cantidad_vecinos = contar_vecinos( matriz, i, j, filas_matriz, columnas_matriz )
            if matriz[ i ][ j ] == 1:
                # Si una celula viva tiene menos de 2 vecinos vivos muere por soledad
                # Si una celula viva tiene mas de 3 vecinos muere por sobrepoblacion
                if cantidad_vecinos < 2 or cantidad_vecinos > 3:
                    nueva_matriz[ i ][ j ] = 0
            else:
                # Si una celula muerta tiene 3 vecinos vivos revive
                if cantidad_vecinos == 3:
                    nueva_matriz[ i ][ j ] = 1
    return nueva_matriz


def main ():
    matriz = generar_regla_25( FILAS_MATRIZ, COLUMNAS_MATRIZ )

    pantalla = pygame.display.set_mode( ( ANCHO_PANTALLA, ALTO_PANTALLA ) )
    pygame.display.set_caption( 'Juego de la vida' )

    actualizar_pantalla( pantalla, matriz )

    pause = True
    
    while 1:
        for evento in pygame.event.get():
            detectar_click( evento, FILAS_MATRIZ, COLUMNAS_MATRIZ, ANCHO_PANTALLA, ALTO_PANTALLA, matriz )
            detectar_cerrado( evento )
            pause = detectar_pausa( evento, pause )

        actualizar_pantalla( pantalla, matriz )
        pygame.display.flip()
        if not pause:
            matriz = aplicar_reglas( matriz )
        sleep( .5 )

if __name__ == '__main__':
    main()
