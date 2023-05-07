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

def generar_regla_34(filas_matriz: int, columnas_matriz:int):
    matriz =generar_matriz(filas_matriz, columnas_matriz )

    for i in range( filas_matriz):
        for j in range( columnas_matriz):
            if i+j==columnas_matriz//2:
                matriz[i][j]=1
    return matriz

def generar_regla_1(filas_matriz: int, columnas_matriz:int):
    matriz =generar_matriz(filas_matriz, columnas_matriz )
    mitad_matriz = (columnas_matriz-1)//2 if columnas_matriz%2==0 else columnas_matriz//2
    for i in range( filas_matriz):
        for j in range( columnas_matriz):
            if i%2==0:
                matriz[i][mitad_matriz]=1  
            else:
                if mitad_matriz !=(j-1) and mitad_matriz !=(j+1) and mitad_matriz!=j:
                    matriz[i][j]=1     
    return matriz