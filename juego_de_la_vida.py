import pygame
from generar_matriz import generar_matriz
from time import sleep


pygame.init()

FILAS_MATRIZ = 20
COLUMNAS_MATRIZ = 4

ANCHO_PANTALLA = 800
ALTO_PANTALLA = 800

COLOR_FONDO = ( 33, 33, 33 )
COLOR_DIVISIONES = ( 255, 132, 0 )
COLOR_AUTOMATA_CELULAR = ( 248, 255, 219 )

def hallar_coordenadas_centrales_pantalla ( tam_celda_eje_x, tam_celda_eje_y, i, j ):
    inicio_eje_x = tam_celda_eje_x * j
    inicio_eje_y = tam_celda_eje_y * i
    centro_eje_x = inicio_eje_x + ( tam_celda_eje_x / 2 )
    centro_eje_y = inicio_eje_y + ( tam_celda_eje_y / 2 )
    coordenadas_centro = ( centro_eje_x, centro_eje_y )
    return coordenadas_centro

def hallar_radio ():
    pass

def dibujar_celdas ( filas_matriz, columnas_matriz, ancho_pantalla, alto_pantalla, pantalla ):
    tam_celda_eje_x = ancho_pantalla / columnas_matriz
    tam_celda_eje_y = alto_pantalla / filas_matriz
    for i in range( 1, columnas_matriz ):
        pygame.draw.line( pantalla, COLOR_DIVISIONES, ( tam_celda_eje_x * i, 0 ), ( tam_celda_eje_x * i, alto_pantalla ), width=2 )
    for i in range( 1, filas_matriz ):
        pygame.draw.line( pantalla, COLOR_DIVISIONES, ( 0, tam_celda_eje_y * i ), ( ancho_pantalla, tam_celda_eje_y * i ), width=2 )

def dibujar_automatas_de_matriz ( filas_matriz, columnas_matriz, ancho_pantalla, alto_pantalla, pantalla, matriz ):
    tam_celda_eje_x = ancho_pantalla / columnas_matriz
    tam_celda_eje_y = alto_pantalla / filas_matriz

    for i in range( filas_matriz ):
        for j in range( columnas_matriz ):
            if matriz[ i ][ j ] == 1:
                coordenadas_cetro = hallar_coordenadas_centrales_pantalla( tam_celda_eje_x, tam_celda_eje_y, i, j )
                
                # pygame.draw.circle( pantalla, COLOR_AUTOMATA_CELULAR, coordenadas_cetro, 

    


def main ():
    matriz = generar_matriz( FILAS_MATRIZ, COLUMNAS_MATRIZ )
    pantalla = pygame.display.set_mode( ( ANCHO_PANTALLA, ALTO_PANTALLA ) )
    pygame.display.set_caption( 'Juego de la vida' )
    pantalla.fill( COLOR_FONDO )
    dibujar_celdas( FILAS_MATRIZ, COLUMNAS_MATRIZ, ANCHO_PANTALLA, ALTO_PANTALLA, pantalla )



    while 1:
        pygame.display.flip()
        sleep( 1 )

if __name__ == '__main__':
    main()





