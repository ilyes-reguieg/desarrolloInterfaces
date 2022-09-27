def funcion_fibonacci():
    n = max(int(input('tecla un numero ')), 1)
    if n == 0: return 0
    elif n == 1: return 1
    else:
        a = 0
        b = 1
        for i in range(0, n-1):
            aux  = a + b   
            a = b
            b = aux
            
    print('El valor de '+ str(n) +' es: '+ str(b))