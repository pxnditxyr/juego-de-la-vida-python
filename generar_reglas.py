from generar_matriz import generar_matriz

def generar_regla_0 ( filas_matriz : int, columnas_matriz : int ):
    matriz = generar_matriz( filas_matriz, columnas_matriz )
    matriz[ 0 ][ columnas_matriz // 2 ] = 1
    return matriz

def generar_regla_24 ( filas_matriz : int, columnas_matriz : int ):
    matriz = generar_matriz( filas_matriz, columnas_matriz )

    for i in range( filas_matriz ):
        for j in range( columnas_matriz ):
            if i - j == -( columnas_matriz // 2 ):
                matriz[ i ][ j ] = 1
    return matriz
