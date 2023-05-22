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

def generar_regla_11 ( filas_matriz : int, columnas_matriz : int ):
    matriz = generar_matriz( filas_matriz, columnas_matriz )
    mitad_matriz = ( columnas_matriz - 1 ) // 2 if columnas_matriz % 2 == 0 else columnas_matriz // 2
    pibote = mitad_matriz
    matriz[ 0 ][ mitad_matriz ] = 1
    for i in range( 1, filas_matriz ):
        for j in range( columnas_matriz ):
            if i % 2 == 0:
                if j >= pibote and j <= pibote + 1:
                    matriz[ i ][ j ] = 1
            else:
                if j < pibote or j > pibote + 1:
                    matriz[ i ][ j ] = 1
        pibote += 1
    return matriz

def generar_regla_15( filas_matriz : int, columnas_matriz : int  ):
    matriz = generar_matriz( filas_matriz, columnas_matriz )
    mitad_matriz = ( columnas_matriz - 1 )//2 if columnas_matriz%2 == 0 else columnas_matriz//2

    for i in range( filas_matriz ):
        for j in range( columnas_matriz ):
            if i % 2 != 0:
                if ( i + j ) != ( mitad_matriz + ( i * 2 ) ):
                    matriz[ i ][ j ] = 1
                
        if i % 2 == 0 and ( mitad_matriz + i ) < columnas_matriz:
            matriz[ i ][ mitad_matriz + i ] = 1
    return matriz

def generar_regla_9 ( filas_matriz : int, columnas_matriz : int ):
    matriz = generar_matriz( filas_matriz, columnas_matriz )
    mitad_matriz = ( columnas_matriz - 1 )//2 if columnas_matriz%2 == 0 else columnas_matriz//2
    matriz[ 0 ][ mitad_matriz ] = 1

    pibote_separacion = 1
    pibote_central = mitad_matriz

    for i in range( filas_matriz ):
        for j in range( columnas_matriz ):
            if i % 2 != 0:
                if j < pibote_central - pibote_separacion or j > pibote_central + pibote_separacion:
                    matriz[ i ][ j ] = 1
                if pibote_separacion == 3 and pibote_central - 2 < columnas_matriz:
                    matriz[ i ][ pibote_central - 2 ] = 1
            else:
                if i > 2:
                    if j == pibote_central + 2:
                        matriz[ i ][ j ] = 1
                    if j > pibote_central - 3 and j < pibote_central + 1:
                        matriz[ i ][ j ] = 1
                elif j == pibote_central + 1 and i > 0 and i < 3:
                    matriz[ i ][ j ] = 1
                    matriz[ i ][ j - 2 ] = 1

        if i % 2 != 0:
            if pibote_separacion < 3:
                pibote_separacion += 1
                pibote_central += 1
            else:
                pibote_central += 2
    return matriz
    
def generar_regla_25 ( filas_matriz : int, columnas_matriz : int ):
    matriz = generar_matriz( filas_matriz, columnas_matriz )
    mitad_matriz = ( columnas_matriz - 1 )//2 if columnas_matriz%2 == 0 else columnas_matriz//2
    matriz[ 0 ][ mitad_matriz ] = 1

    central = mitad_matriz
    cont = 1
    pibote=0

    for i in range( filas_matriz ):
        for j in range( columnas_matriz ):
            if i % 2 != 0:
                if j < (central + pibote - cont) or  j >=(central + pibote + cont):
                    matriz[i][j] = 1
            else:
                if j==central+pibote:
                    if i>3:
                        matriz[i][j-2]=1
                        matriz[i][j-1]=1
                        matriz[i][j-0]=1
                        matriz[i][j+2]=1
                    elif i>1:
                        matriz[i][j-1]=1
                        matriz[i][j+1]=1
        if i % 2 != 0:
            if i < 5 :
                cont+=1
            else:
                pibote+=1
                matriz[i][central + pibote -3]=1
                
    return matriz