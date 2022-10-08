'''
FUNCIONES:
Argumentos por posición:  que los parametros sean respetados cuando escriba la función, ejemplo:
def función(valor,valor2):
    *escribo función*

función(1, 2)

argumentos por clave: no tienen que estaren orden, porque puedo darle un valor cuando escribo la función, ejemplo: 
función(valor=1, valor2=2)
'''


# def corroborar_email(mail):
#     esta_bien_escrito_o_no=mail.find("@")
#     if (esta_bien_escrito_o_no>=0):
#         print("tu email es valido!")
#     else:
#         print("tu email no es valido :(")

# email=input("Ingrese su email: ")
# corroborar_email(email)

'''
LISTAS:
'''

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
print(f"esta lista contiene los números: {lista_numeros}")

for i in range (5,23):
    print(f"las variantes que se encuentran entre las posiciones 5 y 22 son: {i}")
