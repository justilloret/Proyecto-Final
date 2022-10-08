'''
1. Mensaje simple: Almacene un mensaje en una variable e imprímalo en pantalla. Después cambie el valor del
mensaje e imprímalo nuevamente.

'''
# mensaje1 = 'hola!'
# print(mensaje1)

# mensaje2 = 'cómo estas?'
# print(mensaje1,mensaje2)

'''
2. Almacene el nombre de una persona en una variable, imprima un mensaje para esa persona. Por ejemplo “Hola
Fede, ¿te gustaría aprender a programar?”

'''
# nombre = input('ingrese su nombre: ')
# print(f'hola {nombre}, bienvenido/a! :)')

'''
3. El número ocho: Escriba una suma, resta, multiplicación y división que resulten cada una en el número ocho.
Asegúrese de utilizar la función print() para ver los resultados en pantalla. Un ejemplo de línea es el siguiente:
print(5 + 3)
La salida debería mostrar el número ocho tantas veces como líneas haya escrito.

'''
# print( 4 + 4)
# print( 10 - 2)
# print(2*4)
# print(80//10)

'''
4. Cree cuatro variables llamadas mi_entero, mi_decimal, mi_string y mi_booleano. Asigne a cada variable un valor del
tipo que le corresponda. Luego muestre en pantalla el tipo de cada variable usando la función type() combinando
todo con la función print() :
type(mi_entero)
type(mi_booleano)
La salida final debería contener las siguientes líneas (no importa el orden):
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
'''
# mi_entero = 234
# mi_decimal = 0.5
# mi_string = 'hola!'
# mi_booleano = False

# print( type(mi_entero))
# print(type(mi_decimal)) 
# print(type(mi_string))
# print(type(mi_booleano))

'''
5. Escriba un programa que acepte un numero decimal como entrada y lo imprima sin lugares decimales.
'''
# numero_decimal = float(input('escribe un número decimal: '))
# print(numero_decimal//1)

'''
6. ¿Cuál es la salida de las siguientes expresiones?
1 != 2
Salida: True
True == 1
Salida: true
False != False
Salida: Flase
False > 0
Salida: False
1.0 < 1
Salida: False
“test” == “test”
Salida:True
1.0 >= 1
Salida:True
'''
# print( 1 != 2)
# print(True == 1)
# print(False != False)
# print(False > 0)
# print(1.0 < 1)
# print("test" == "test")
# print(1.0 >= 1)

'''
7. Escriba un programa que le pida al usuario que ingrese nombre y edad. Luego muestre un mensaje
donde le informe el año en que va a cumplir 100.
'''
# nombre= input('ingresa tu nombre: ')
# edad = int(input('ingresa tu edad: '))
# año_en_el_que_va_a_cumplir_100_el_usuario = (2022 - edad) + 100
# print(f'hola {nombre}!,sabias que tu cumpleaños numero 100 va a ser en {año_en_el_que_va_a_cumplir_100_el_usuario}?')

'''
8. Escriba un programa que permita convertir una temperatura en Celsius a la escala Farenheit. La
fórmula es:
Fahrenheit = 
'''
# temperatura_en_celsius = int(input('ingrese una temperatura en grados celsius: '))
# temperatura_en_fahrenheit = (9.0/5.0) * temperatura_en_celsius + 32
# print(f'{temperatura_en_celsius}° celsius equivalen a {temperatura_en_fahrenheit}° grados fahrenheit')

'''
9.  Calculadora simple: Cree un programa capaz de pedir dos números al usuario y devolver el resultado
de la suma, resta, multiplicación y división entre los mismos. Por ejemplo, si los números son 3 y 5, la calculadora
nos devolvería: 3+5; 3-5; 3*5 y 3/5. Pruebe también expandir su calculadora y agregar nuevas operaciones, tales
como la potenciación o la división entera.
'''
# numero1 = int(input('ingrese un numero: '))
# numero2 = int(input('ahora ingrese otro numero: '))
# suma = numero1 + numero2
# resta = numero1 - numero2
# multiplicacion = numero1 * numero2
# division = numero1 / numero2
# modulo = numero1 % numero2
# print(f'la suma entre {numero1} y {numero2} es de {suma} \nla resta entre {numero1} y {numero2} es de {resta} \nla multiplcacion entre {numero1} y {numero2} es de {multiplicacion} \nla división entre {numero1} y {numero2} es de {division}  \nel modulo de {numero1} y {numero2} es de {modulo}')