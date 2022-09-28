import random
from re import L


notaFinal = 0

preguntaArray = ['Cual es la capital de Cameroon? \n a): Douala \n b): Mingasa \n c): Madrid \n ','Cual de las siguientes tecnologias no se considera como lenguaje de programacion? \n a): Html \n b): Java \n c): Python \n','Cual es la nacionalidad del futbolista Granit Xhaka?  \n a): Suiza \n b): Inglatrra \n c): Japon \n']
randomNumber1 = random.randint(0,2)

pregunta = preguntaArray[randomNumber1]
input(preguntaArray[randomNumber1])
if(preguntaArray[randomNumber1] == 'a'):
    print('Respuesta correcta')
    notaFinal = notaFinal + 10
    preguntaArray.pop(randomNumber1)
else:
    print('Respuesta incorrecta')
    notaFinal = notaFinal - 5
    preguntaArray.pop(randomNumber1)


randomNumber2 = random.randint(0,1)  
input(preguntaArray[randomNumber2]) 
if(preguntaArray[randomNumber2] == 'a'):
    print('Respuesta correcta')
    notaFinal = notaFinal + 10
    preguntaArray.pop(randomNumber2)
else:
    print('Respuesta incorrecta')
    notaFinal = notaFinal - 5
    preguntaArray.pop(randomNumber2)
    

     
print('tu nota final es: ' + str(notaFinal))
     
