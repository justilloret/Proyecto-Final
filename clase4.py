'''
3. Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30) 
y el nombre del mes. Para simplificarlo vamos a suponer que febrero tiene 28 días. Usar diccionarios

'''

# diccionario = {
# 'enero': 31,
# 'febrero': 28,
# 'marzo': 31,
# 'abril':30,
# 'mayo':31,
# 'junio':30,
# 'julio':31,
# 'agosto':31,
# 'septiembre':30,
# 'octubre':31,
# 'noviembre':30,
# 'diciembre':31
# }

# pregunta=int(input('escribe un número de mes: '))
# meses = ('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
# meses.keys()
# for pregunta in meses:
#     print (f'el mes {pregunta} es {meses}')

notas = []

for i in range(7):
   nota=int(input('escribe tu nota: '))
   notas.append(nota)
print(f'tus notas son: {notas}')

notas_aprobadas = 0
notas_desaprobadas = 0

for j in range(len(notas)):
    if nota>=6 : 
        notas_aprobadas+=1
    else:
        notas_desaprobadas+=1
print(f'aprobaste {notas_aprobadas}  y desprobaste {notas_desaprobadas}')
