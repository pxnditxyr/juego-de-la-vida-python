from random import randint

def generar_matriz ( num_filas, num_columnas ):
    matriz = []
    for _ in range( num_filas ):
        matriz.append( [ 0 ] * num_columnas ) 
    return matriz

def generar_matriz_aleatoria ( num_filas: int, num_columnas: int ) -> list[ list[ int ] ]:
    matriz = []
    for _ in range( num_filas ):
        fila = []
        for _ in range( num_columnas ):
            fila.append( randint( 0, 1 ) )
        matriz.append( fila )
    return matriz
