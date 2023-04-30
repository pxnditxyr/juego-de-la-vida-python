import pygame
from deteccion_eventos import detectar_cerrado, detectar_click
from dibujado import dibujar_automatas_de_matriz, dibujar_celdas
from generar_matriz import generar_matriz_aleatoria
from time import sleep

pygame.init()

FILAS_MATRIZ = 20
COLUMNAS_MATRIZ = 20

ANCHO_PANTALLA = 800
ALTO_PANTALLA = 800

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
    
    for i in range( filas_matriz ):
        for j in range( columnas_matriz ):
            cantidad_vecinos = contar_vecinos( matriz, i, j, filas_matriz, columnas_matriz )
            if matriz[ i ][ j ] == 1:
                # Si una celula viva tiene menos de 2 vecinos vivos muere por soledad
                # Si una celula viva tiene mas de 3 vecinos muere por sobrepoblacion
                if cantidad_vecinos < 2 or cantidad_vecinos > 3:
                    matriz[ i ][ j ] = 0
            else:
                # Si una celula muerta tiene 3 vecinos vivos revive
                if cantidad_vecinos == 3:
                    matriz[ i ][ j ] = 1



def main ():
    matriz = generar_matriz_aleatoria( FILAS_MATRIZ, COLUMNAS_MATRIZ )

    pantalla = pygame.display.set_mode( ( ANCHO_PANTALLA, ALTO_PANTALLA ) )
    pygame.display.set_caption( 'Juego de la vida' )

    actualizar_pantalla( pantalla, matriz )
    
    while 1:
        for evento in pygame.event.get():
            detectar_click( evento, FILAS_MATRIZ, COLUMNAS_MATRIZ, ANCHO_PANTALLA, ALTO_PANTALLA, matriz )
            detectar_cerrado( evento )

        actualizar_pantalla( pantalla, matriz )
        pygame.display.flip()
        aplicar_reglas( matriz )
        sleep( 0.2 )

if __name__ == '__main__':
    main()





