from math import *
def funcion_fibonacci2():
    n = max(int(input('tecla un numero ')), 1)
    if n == 0: return 0
    elif n == 1: return 1
    else:
        a = (1 + sqrt(5))/2
        b = (1 - sqrt(5))/2
        for i in range(0, n-1):
            aux  = a + b   
            a = b
            b = aux
            
    print('El valor de '+ str(n) +' es: '+ str(b))