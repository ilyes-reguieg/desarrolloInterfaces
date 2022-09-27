pregunta1 = input('Cual es la capital de Cameroon? \n a): Madrid \n b): Mingasa \n c): Douala \n ')
notaFinal = 0

if(pregunta1 == 'c'):
    print('Respuesta correcta')
    notaFinal = notaFinal + 10
else:
    print('Respuesta incorrecta')
    notaFinal = notaFinal - 5

    
pregunta2 = input('Cual de las siguientes tecnologias no se considera como lenguaje de programacion? \n a): Html \n b): Java \n c): Python \n')
if(pregunta2 == 'a'):
    print('Respuesta correcta')
    notaFinal = notaFinal + 10
else:
    print('Respuesta incorrecta')
    notaFinal = notaFinal - 5
    
pregunta3 = input('Cual es la nacionalidad del futbolista Granit Xhaka?  \n a): Suiza \n b): Inglatrra \n c): Japon \n')
if(pregunta3 == 'a'):
    print('Respuesta correcta')
    notaFinal = notaFinal + 10
else:
    print('Respuesta incorrecta')
    notaFinal = notaFinal - 5
     
print('tu nota final es: ' + str(notaFinal))
     
