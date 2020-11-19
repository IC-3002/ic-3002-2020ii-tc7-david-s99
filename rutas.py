#Tarea corta 07 David 
res=[]
SIZE=0
matriz=[]
def encontrar_ruta(C):
    global res
    global SIZE
    global matriz
    SIZE=len()
    res=[[0]*SIZE for _ in range(SIZE)]
    r=len(C)
    c=len(C[0])
    
    
    return encontrar_ruta_aux(r,c,C)

def encontrar_ruta_aux(r,c,matriz):
    global res
    if (r==SIZE-1) and (c==SIZE-1):
        res[r][c] = 1;
        return True;
    if r>=0 and c>=0 and r<SIZE and c<SIZE and res[r][c] == 0 and matriz[r][c] == 0:
        res[r][c] = 1
        if encontrar_ruta_aux(r+1, c,matriz):
            return True
        if encontrar_ruta_aux(r, c+1,matriz):
            return True
        if encontrar_ruta_aux(r-1, c,matriz):
            return True
        if encontrar_ruta_aux(r, c-1,matriz):
            return True
        #backtracking
        res[r][c] = 0;
        return False;
    if encontrar_ruta_aux(0,0,matriz):
        print("Si hay solucion ")
        print("")
        for i in res:
            print (i)
    else:
        print("No hay solucion")
    return 0;



