#Estos datos están compuestos por otros datos
# Los datos compuestos son datos que tienen adentro otros datos.
# Los datos compuestos son datos que adentro tienen datos simples u otros datos compuestos, pero que se pueden agrupar
# El primer tipo de dato es la lista

#creando una lista (se pueden modificar)
lista = ["Matias Bolonese","Golemm501",True,1.85]
#creando una tupla (no se pueden modificar)
tupla = ("Matias Bolonese","Golemm501",True,1.85)

#esto es válido
lista[3] = "Golemm503"

#esto no es válido
#tupla[3] = "Golemm503"

print(lista[3])

#conjunto o set
#creando un conjunto (set) (no se puede acceder a elementos por indice, no almacena datos duplicados)
#para crearlo, se usan llaves
conjunto = {"Matias Bolonese","Golemm501",True,1.85}

#print(conjunto[3]) -> no puede acceder al elemento

#creando un diccionario (dict) (es igual que un json en javascript) (la estructura es key : value y separamos con comas)
diccionario = {
    # clave   # valor
    'nombre' : "Matias Bolonese",
    'canal' : "Golemm501",
    'esta_emocionado' : True,
    'altura' : 1.84,
    'dato_duplicado' : "Golemm501"
}

# print(diccionario[key])
print(diccionario['nombre'])

# print() es una función que permite mostrar lo que contiene un valor.
# Si se pone print y adentro se le pasa algo, se va a mostrar en consola lo que se pasó.
# El tipo de dato es "list".
# Los datos compuestos sirven para agrupar datos

                      #indice   #elemento
                      #o
                      #posición
# "Matias Bolonese" = lista[0] (elemento 1)
# "Golemm501" = lista[1] (elemento 2)
# True = lista[2] (elemento 3)
# 1.85 = lista[3] (elemento 4)

# El número que está entre corchete es el elemento que se va a mostrar. 

# Una lista es un tipo de matriz.
# Hay otra matriz que es similar a lista que es el array, el arreglo, pero es otro tipo de matriz que hay que hacer otro tipo de cosas para trabajar con estas.
# Es muy utilizado en Python los arreglos, los array, pero para esto específicamente no, para esto necesitamos este tipo de matriz que son las listas.
# Una matriz es un conjunto de datos.
# Una lista, por ejemplo, es una matriz.
# Después hay otro tipo de dato compuesto que son las tuplas, que son iguales a las listas, solamente que en vez de usar corchetes, se usa paréntesis.
# La diferencia entre la lista y la tupla es que la tupla no se puede modificar.
# En un conjunto, las diferencias pueden ser que, por ejemplo, no tienen un orden fijo, es decir, son elementos desordenados y que pueden cambiar. O sea, pueden intercambiarse y va a estar todo bien.
# Los conjuntos son casi iguales que las listas, es decir, se pueden modificar solo que los elementos no, es como las tuplas en este caso.
# En los conjuntos, no se puede acceder por el indice, pero se puede mostrar como tal.
# Además, en los conjuntos, no permiten repetir valores.
# En los conjuntos, para acceder a los datos de un conjunto, se debe usar un bucle.
# Los conjuntos no tienen order, son desordenados, los elementos pueden variar de lugar.
# En los diccionarios, el usuario le asigna nombres propios a los elementos.
# En las listas, los índices se enumeran de forma automática.
# RECORDATORIO: LAS TUPLAS NO SE PUEDEN MODIFICAR
# En los diccionarios, no hay orden en los elementos.
# En los diccionarios, hay una clave y un valor.
# La estructura del diccionario es: (key, value).
# En los diccionarios, no se pone coma ni al principio ni al final, solo se utiliza para separar.