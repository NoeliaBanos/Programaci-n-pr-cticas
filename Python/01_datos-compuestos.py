print('Listas de datos y tuplas')
# esta lista se puede modificar
lista= ['Noelia Baños', 'Soy Noelia',True, 1.75]
# esta lista no se puede modificar
tupla = ('Noelia Baños', 'Soy Noelia',True, 1.75)
# así miramos los arrays en python
lista[3] = 1.80
#esta línea no se puede modificar porque es una tupla
#tupla[3] = 1.99
#print(lista[1])
print(lista[0])
print(tupla[1])
print(lista[3])
print(tupla[3])

print('-----------------')
print('Conjuntos y funcionamiento')
# creando un conjunto 'set' - similar a las listas
conjunto = {'Noelia Baños', 'Soy Noelia',True, 1.75}
# no se puede acceder a los elementos por índice
print(conjunto)

print('-----------------')
print('Diccionario')
# creando diccionario (dict), que es como un objeto en javascript
diccionario= {
    'nombre': 'Noelia Baños',
    'canal': 'Soy Noelia',
    'altura': 1.76
}
print(diccionario['nombre'])