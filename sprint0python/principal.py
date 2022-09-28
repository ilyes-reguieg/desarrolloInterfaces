import time

from math import *
from fibonacci2 import *
from fibonacci import *

answer = input('que opcion quieres eligir tecla a si quieres ejecutar con fibo1  tecla b si quieres con fibo 2 ')

if(answer == 'b'):
    start_time = time.time()
    funcion_fibonacci2()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print('El tiempo de ejecución ha sido :' + str(elapsed_time) + ' s')
    
if(answer == 'a'):funcion_fibonacci()
