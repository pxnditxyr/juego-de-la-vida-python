from math import floor


def hallar_coordenadas_centrales_pantalla ( tam_celda_eje_x, tam_celda_eje_y, i, j ):
    inicio_eje_x = tam_celda_eje_x * j
    inicio_eje_y = tam_celda_eje_y * i
    centro_eje_x = inicio_eje_x + ( tam_celda_eje_x / 2 )
    centro_eje_y = inicio_eje_y + ( tam_celda_eje_y / 2 )
    coordenadas_centro = ( centro_eje_x, centro_eje_y )
    return coordenadas_centro

def hallar_tam_celdas ( filas_matriz, columnas_matriz, ancho_pantalla, alto_pantalla ):
    tam_celda_eje_x = ancho_pantalla / columnas_matriz
    tam_celda_eje_y = alto_pantalla / filas_matriz
    return tam_celda_eje_x, tam_celda_eje_y

def hallar_radio ( tam_celda_eje_x: float, tam_celda_eje_y: float ) -> float:
    tam_menor = tam_celda_eje_x if tam_celda_eje_x < tam_celda_eje_y else tam_celda_eje_y
    radio = ( tam_menor - ( tam_menor * 0.15 ) ) / 2
    return radio

def establecer_automata_en_matriz ( filas_matriz, columnas_matriz, ancho_pantalla, alto_pantalla,  posicion, matriz ):
    tam_celda_eje_x, tam_celda_eje_y = hallar_tam_celdas( filas_matriz, columnas_matriz, ancho_pantalla, alto_pantalla )
    indice_j = floor( posicion[ 0 ] / tam_celda_eje_x )
    indice_i = floor( posicion[ 1 ] / tam_celda_eje_y )

    indice_i = indice_i if indice_i < filas_matriz else indice_i - 1
    indice_j = indice_j if indice_j < columnas_matriz else indice_j - 1

    matriz[ indice_i ][ indice_j ] = int( not matriz[ indice_i ][ indice_j ] )
