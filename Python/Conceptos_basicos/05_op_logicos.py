# AND = &
edad = 25
tiene_dni = True

if edad >= 18 & tiene_dni:
    print("Puede entrar al bar.")
else:
    print("No puede entrar.")
print('--------------------')
# OR = |
dia = "sábado"
es_feriado = False

if dia == "sábado" or dia == "domingo" or es_feriado:
    print("No hay clases.")
else:
    print("Hay clases.")

print('--------------------')
# NOT = not
lloviendo = False

if not lloviendo:
    print("Puedes salir sin paraguas.")
else:
    print("Lleva paraguas.")

print('--------------------')
edad = 17
permiso_padres = True

if edad >= 18 or (edad >= 16 and permiso_padres):
    print("Puedes ir al concierto.")
else:
    print("No puedes ir.")

print('--------------------')
tarea_hecha = False
nota = 9

if not tarea_hecha and nota < 10:
    print("Debes hacer la tarea para tener un 10.")