'''
1. Pida un número al usuario y determine si es par o impar.
'''
#numero = int(input('Ingrese un número y averigue si es par o impar: '))
#if (numero % 2 == 0):
#    print(f"{numero} es un número par")
#else:
#    print(f"{numero} es un número impar")
'''
2. Escriba una cadena if-elif-else que determine el estado de vida de una
persona.
• Si la persona tiene menos de 2 años, muestre un mensaje que diga que
es un bebe.
• Si tiene al menos 2 años, pero menos de 4, muestre que es un infante.
• Si tiene al menos 4, pero menos de 12, muestre que es un niño.
• Si tiene al menos 13, pero menos de 20, muestre que es un adolescente.
• Si tiene al menos 20 pero menos de 65, muestre que es un adulto.
• Si tiene 65 o más, muestre que es un anciano.
'''
#print("¿En qué estado de vida se encuentra?")
#edad_de_la_persona = int(input("Ingrese su edad: "))
#if (edad_de_la_persona<2):
#    print("Es un bebé")
#elif (edad_de_la_persona>1) and (edad_de_la_persona<4):
#    print("Es un infante")
#elif (edad_de_la_persona>3) and (edad_de_la_persona<12):
#    print("Es un niño")
#elif (edad_de_la_persona>12) and (edad_de_la_persona<20):
#    print(" Es un adolecente")
#elif (edad_de_la_persona>19) and (edad_de_la_persona<65):
#    print("Es un adulto")
#else:
#    print("Es un anciano")
'''
3. Infinito: Cree un ciclo que nunca termine y ejecútelo. Puede probarlo
haciendo que muestre algo en pantalla por cada pasada del ciclo. Para
finalizarlo, presione Ctrl-C o el comando para detener la ejecución
correspondiente a su editor
'''
# palabra = 'hola :D'
# while True:
#     print (palabra)
'''
4. Escriba un programa que contenga dos ciclos while anidados que
muestre los enteros del 1 al 100, diez números por línea, como se muestra
abajo,
1 2 3 4 5 6 7 8 9 10
11 12 13 14 15 16 17 18 19 20
21 22 23 24 25 26 27 28 29 30
.
.
91 92 93 94 95 96 97 98 99 100
'''
# n = 0
# for i in range (1,101):
#     n2 = n + i
#     print(n2)

'''
5. Resuelva el ejercicio anterior usando solo un ciclo while.
'''
'''
6. Escriba una función que muestre todos los números primos entre 1 y un
número n que es ingresado por parámetro.
'''

'''
7. Escriba una función que le pida al usuario ingresar condimentos para
un sándwich, hasta que el usuario ingrese ‘salir’. Cada vez que se ingrese
un condimento, muestre un mensaje avisando que ya se agregó el
condimento al sándwich.
Escriba versiones diferentes del programa de acuerdo a estos criterios:
• Use un test condicional en el ciclo while para detener la ejecución.
• Use un test condicional dentro del ciclo para decidir si continuar la
ejecución.
'''

'''
8.
A) Remera: Escriba una función hacer_remera() que tome como
parámetros un tamaño y el mensaje que debería ir impreso en la remera.
La función debe mostrar un mensaje describiendo el tamaño de la
remera y el mensaje impreso en ella. Llame la función una vez usando
argumentos por posición. Llámela una segunda vez usando argumentos
por clave.
B) Remeras Grandes: Modifique la funcion hacer_remera() para que el
tamaño por defecto sea ‘L’ y el mensaje, ‘Me gusta Python’. Haga un par
de remeras, la primera con los valores por defecto, y la segunda con
valores diferentes.
9. Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n
primeros numeros de la serie de Fibonacci. En esta serie, los primeros dos
números son 0 y 1, y cada sucesivo número es la suma de los dos números
inmediatamente anteriores (por ejemplo, 0,1,1,2,3,5, …).
10. (Opcional) Calculadora más inteligente: Modifique el ejercicio 9 del
primer practico para que la calculadora sea capaz de devolver el
resultado solamente de una operación especificada por el usuario. Por
ejemplo, si el usuario ingresa dos numeros x, y, y luego ingresa ‘1’, la
calculadora devuelve la suma entre los numeros x,y; si ingresa ‘2’,
devuelve la resta, etc.
11. (Opcional) Conversión imperial: Desarrollar un programa en Python
que pueda convertir gramos a libras, centímetros a pulgadas y kilómetros
a millas. El programa debe permitir la conversión en ambos sentidos.
1.60934 Km = 1 milla
0.393701 pulgadas = 1 cm
0.00220462 libras = 1 gramo
12. (Opcional) Cuando un año es bisiesto, el mes más corto del año,
febrero, tiene 29 días en vez de 28. Esto sucede casi cada 4 años.
Los tres criterios que permiten saber si un año es bisiesto en el calendario
gregoriano (el nuestro) son los siguientes:
• Si el año es divisible enteramente por 4, es bisiesto a menos que:
o El año sea divisible por 100, entonces NO es bisiesto, a menos
que:
▪ El año sea también divisible por 400. Entonces sí es un
año bisiesto.
Esto significa que en el calendario gregoriano los años 2000 y 2400 son
bisiestos, mientras que los años 1900, 2100, 2200 y 2300 no son bisiestos.
a) Escriba una función que tome un año y diga si es bisiesto o no.
b) Modifique su programa para que devuelva todos los años bisiestos entre el
año actual y el año pasado a la función como parámetro (este debe ser
posterior al año actual).
13. (Opcional) Si listamos todos los números naturales menores a 10 que
son múltiplos de 3 o 5, obtenemos 3,5,6 y 9. La suma de estos múltiplos es
23.
Encuentre la suma de todos los múltiplos de 3 o 5 menores a 1000.
'''