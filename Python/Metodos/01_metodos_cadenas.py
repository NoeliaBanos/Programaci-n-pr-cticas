cadena1 = "hola soy Noelia"
cadena2 = "Bienvenidos a este programa"

#dir ejecuta algo que se ve envolviendolo con un print
#print(dir(cadena1))

# dir es una funcion
resultado = dir(cadena1)
print(resultado)

# para pasarlo a mayúscula
resultado = cadena1.upper()
print(resultado)

# lo pasa a minúscula
resultado = cadena1.lower()
print(resultado)

# primera letra en matúscula y el resto en minúscula
resultado = cadena1.capitalize()
print(resultado)

# buscamos una cadena en otra cadena sale -1 si no existe
resultado = cadena1.find('hola')
resultado = cadena1.find('N')
print(resultado)

#funciona parecido a find, pero si no existe sale un error
resultado = cadena1.index('N')
print(resultado)

# si es númerico devuelve true
cadena_numeric = '345'
resultado = cadena_numeric.isnumeric()
print(resultado)

# si es alfabético (de la a-z sin espacios) devuelve true si no, devuelve false
cadena_alfa = 'aaa'
resultado = cadena_alfa.isalpha()
print(resultado)

#buscamos una cadena en otra cadena y devuelve la cantidad de veces que coincide
coincidencias = cadena1.count('a')
print(coincidencias)

# contamos cuantos caracteres tiene la cadena
contar = len(cadena1)
print(contar)

#verificamos si una cadena empieza con otra cadena, devuelve true
empezar = cadena1.startswith('h')
print(empezar)

#verificamos si una cadena acaba con otra cadena, devuelve true
acabar = cadena1.endswith('a')
print(acabar)

#reemplaza una cadena dada por otra cadena
cadena_nueva = cadena1.replace('Noelia', 'Noe')
print(cadena_nueva)