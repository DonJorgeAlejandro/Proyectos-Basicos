# Simulador de dados JORGE SILVA

import random  
res = input("Quiere iniciar el lanzamiento de dados?: s/n ")   
while (res == 's'):
    dado1 = int((random.random()*10)%6+1)
    dado2 = int((random.random()*10)%6+1)
    print("El dado uno cae en: ", dado1) 
    print("El dado dos cae en: ", dado2)
    print("La suma de los dados lanzados es: ", (dado1 + dado2))
    res = input("Quiere iniciar el lanzamiento de dados?: s/n ")
    
    if (res == 'n'):
        print("Gracias por participar!")
        break