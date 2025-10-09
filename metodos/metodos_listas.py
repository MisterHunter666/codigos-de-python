# Los metodos de listas son métodos que vamos a poder aplicar a listas para operarlas.

#Creando una lista con list()
lista = list(["hola","matias",34,56,23,True])

#devuelve la cantidad de elementos de la lista.
cantidad_elementos = len(lista)

#agregando un elemento a la lista
lista.append("JAJAJAJA")

#agregando un elemento a la lista en un indice específico
lista.insert(2,"TOMA MAMA")

#agregamos varios elementos a la lista 
lista.extend([False,2030])

#eliminando un elemento de la lista (por su indice)
lista.pop(3) #-1 para elminar el último, -2 para eliminar el anteultimo, y así sucesivamente

print(lista)


# Vamos con el primero que es el list()

# LIST - crea una lista
# No es un método, es una función, como anteriormente vimos dir(). También, tenemos esta función de list(), que list() justamente crea una lista.

# Creando una lista con list()
#lista = list("hola","matias",34)

# Lo ejecutamos
#print(lista)
# Y nos devuelve un error
# En este caso, nos devuelve una excepción
# ¿Por qué nos devuelve una excepción?
# Bien, porque esto justamente toma como parámetro realmente una lista.
# lista = list(["hola","matias",34])
# Y de esa forma, ahora sí creamos una lista. 
# Podemos ver que cuando lo actualizamos y lo corremos, tenemos la lista creada.
# ['hola', 'matias', 34]
# Como no tiene sentido hacer esto para crear una lista, es raro.
# Como trabajamos, por ejemplo, con tuplas y demás. Bueno, podemos usarlo, pero no es lo más común. Pero nada, que sepan que con list() también podemos crear listas.
# Un buen uso, es para crear una lista vacía, es decir sin elementos.
 
# Bueno, ahora sí vamos a ver el primer método de las listas, que es len().

# LEN - cuenta la cantidad de elementos de una lista
# También len() estaba cuando trabajamos con los caracteres.
# En una cadena de texto, por ejemplo.
# cadena = "hola"
# resultado = cadena.len()
# Esto no funcionaba porque no era un método, era una función. Si ponemos len(cadena) y lo ejecutamos, vamos a buscar "resultado" y vamos a ejecutar a ver qué es lo que tiene adentro.

# resultado = len(cadena)

# print(resultado)

# Devuelve 4
# Bien, nos devolvía la cantidad de caracteres que tenía la cadena.
# ¿Pero qué pasa si ahora lo hacemos con la lista?
# Vamos a verlo
# resultado = len(lista)
# print(resultado)

# Devuelve 3

# Si hacemos esto con la lista, nos devuelve la cantidad de elementos de la lista.
# Por ejemplo, si se pone otros elementos...
# lista = list(["hola","matias",34,56,23,True])
# Ahora me va a devolver que la lista tiene seis(6) elementos.
# ["hola","matias",34,56,23,True]
#    |      |      |  |  |   |
#    v      v      v  v  v   v
#    1      2      3  4  5   6
#                            |
#                            v
# Esto es True, por lo que nos va devolver seis(6) elementos. 

# cantidad_elemento = len(lista)
# Entonces, de esta forma, decimos:
# Devuelve la cantidad de elementos de la lista.

# Después, tenemos otra más...

# APPEND - agrega un elemento a la lista
# Justamente lo que hace append() es agregar elementos a la lista. En este caso, vamos a decir:

# agregando un elemento a la lista

# (append(), insert y extend son diferentes formas de agregar elementos)

# agregando_con_append = lista.append("JAJAJAJA")
# Vamos a ver qué nos devuelve esto
# Primero, si agregamos ese elemento, la lista tiene otro elemento más
# print(lista)
# ["hola","matias",34,56,23,True, "JAJAJAJA"]
# No llamamos a esta variable, llamamos solo a la lista y ahora la lista fue modificada.
# Lo que hicimos acá no fue modificar a esta variable que estamos creando, sino que fue modificar directamente a la lista.
# Entonces de esta forma, a la misma lista le agregamos este elemento: "JAJAJAJA"
# Y lo mostramos acá. 
# print(lista)
# Así que funcionó.
# Vamos a ver qué nos tira la variable.
# print(agregando_con_append)
# Si actualizamos, esto nos devuelve: None.
# ¿Por qué? Porque no es un valor que nos importe.
# Así que vamos a borrar la variable y ahora sí, solamente trabajamos con la lista.
# De esta forma, agregamos justamente un valor a la lista. 

# Ahora también tenemos insert...

# INSERT - agrega un elemento a la lista en el indice especificado
# insert() también agrega un elemento a la lista

# agregando un elemento a la lista en un indice específico
# lista.insert(2,"TOMA MAMA")
# Vamos a ver qué nos muestra la lista ahora
# print(lista)
# insert() lo que hace justamente es agregar una lista.
# Si actualizamos y corremos el programa, ahí nos lo agregó.
# En el indice 2 nos agregó "TOMA MAMA"
# ["hola","matias","TOMA MAMA",34,56,23,True, "JAJAJAJA"]
# "hola" = 0 
# "matias" = 1
# "TOMA MAMA" = 2

# O sea, que antes del 34, el indice 2 va a ser el elemento que le pasamos
# Antes que era el indice 2 (34), ahora es el indice 3. Antes era 0, 1, 2 y ahora es 0, 1, 2, 3, ¿por qué? porque el indice 2 es este: "TOMA MAMA".
# Eso es lo que hace insert(). En append(), no lo podemos hacer. En insert decimos: "Quiero que en el indice 2 esté este elemento", y si ya existe un indice 2, correlo para atrás. Así es como funciona.

# Y después, tenemos la última que es extend()...

# EXTEND - agrega varios elementos a la lista
# extend() lo que hace es agregar varios. Con extend() no podemos agregar uno.
# agregamos varios elementos a la lista
# lista.extend(False,2030)
# Actualizamos
# print(lista)
# Esto me tira un error, ¿por qué? 
# Porque los elementos de la lista no los agregamos así. Los agregamos pasando una lista.
# Es decir, agregamos una lista a otra lista.
# Así que tenemos que pasarle justamente una lista.
# Una lista con elementos.
# lista.extend([False,2030])
# Ahora actualizamos.
# Y ahora sí, funciona.
# Porque tenemos que pasarle una lista. Y no se agrega una lista. La lista nos la divide y nos la agrega como elementos individuales, ¿ves?
# False,2023
# Acabamos de agregar estos dos elementos a la lista.
# Pero no le pasamos los elementos separados.
# Acá le pasamos elementos separados.
# Le podemos pasar un cinco(5) si queremos.
# Le podemos pasar un True si queremos.
# Le podemos usar lo que queramos.
# Pero acá no lo pasamos sueltos.
# Lo pasamos adentro de los corchetes.
# Porque esto significa que estamos pasando una lista

# Después, tenemos pop()...

# POP - elimina un elemento de una lista, pide indice y devuelve valor
# pop() al contrario de agregar, ya estamos eliminando 

# eliminando un elemento de la lista (por su indice)
# ¿Por qué? porque pop() nos pide el indice.
# Vamos a eliminar el elemento 0, por ejemplo.
# lista.pop(0)
# Entonces, si ahora vamos a actualizar la lista, lista ahora no tiene el elemento 0. El elemento 0 era "hola".
# print(lista)
# ['matias', 'TOMA MAMA', 34,56,23,'JAJAJAJA', False, 2030]
# ¿Ven? Antes estaba "hola". Pero ahora ya no tiene elemento 0. El elemento ahora pasa a ser "matias". Porque el que antes era el elemento 0 lo eliminó. 
# Si antes ponemos, por ejemplo, antes de que hagamos esto. Le digo: "mostrame en patalla len(lista)", es decir, si le pido que me muestre el tamaño de la lista y le pido que después me muestre el tamaño de la lista, van a ver esto que es bastante interesante.
# print (len(lista))

# lista.pop(0)

# print (len(lista))

# 10
# 9 
# Me muestra un 10 y un 9, ¿por qué? porque antes la lista tenía 10 elementos. 
# Lo muestro en pantalla.
# Y muestro en pantalla que la lista tiene 10 elementos. 
# Después sacamos un elemento (el elemento 0)
# Y cuando le volvemos a preguntar cuántos elementos tiene, nos dice: "ahora tiene 9". 
# Entonces, 10 elementos. Nos muestra el diez (10).
# Borramos el elemento. Mostramos de vuelta y ahora nos muestra que tiene 9 elementos. Así funciona pop().
# Justamente, nos elimina un elemento de la lista.
# Si pusiéramos, por ejemplo, el cuatro (4)...
# lista.pop(4)
# Nos eliminaría el elemento 4.
# El elemento 4 era 0("hola"), 1("matias"), 2(34), 3(56), 4(23). 
# Nos elimina el "23".
# Pero no, ¿por qué? porque el elemento 4 no es el 23. Es el 56. Porque el elemento 4 es 0("hola"), 1("matias"), 2("TOMA MAMA"), 3(34), y el cuarto, después del 34, venía el 56, que ahora desapareció. Porque agregamos el elemento "TOMA MAMA" (lista.insert(2, "TOMA MAMA"))
# Y además, agregamos el elemento "JAJAJAJA" (listen.append("JAJAJAJA"))
# Entonces, al agregar estos elementos, la lista cambió.
# Entonces, lo tenemos que tener en cuenta también.
# Incluso, una técnica para eliminar el último. 
# ¿El último elemento cuál es? 
# El último elemento es "2030"
# ¿Cómo hago para eliminar "2030"? 
# Bueno, lo que se hace es poner: -1. 
# lista.pop(-1)
# Entonces, si se pone -1, se elimina el último elemento de la lista.
# ['hola', 'matias', 'TOMA MAMA', 34, 56, 23, True, 'JAJAJAJA', False]
# Es una técnica interesante porque, de esta forma, le decimos: "el índice 0 es "hola". Bueno, 1 para atrás. Y 1 para atrás no existe, entonces vuelve a arrancar desde el último. 
# Si le decimos "-2", nos elimina el ante último
# Nos elimina el "False"
# Antes, el último era "2030". Lo eliminó.
# El ante último es "False". 
# ['hola', 'matias', 'TOMA MAMA', 34, 56, 23, True, 'JAJAJAJA', 2030]
# Y acá desapareció. No está más el False.
# Es una técnica que capaz pueda servir en un futuro.

# Después, tenemos remove()...
 
# REMOVE - remueve un elemento de una lista, pide valor
#  

# CLEAR - elimina todos los elementos de una lista

# SORT - ordena una lista de forma ascendente a descendente
# REVERSE - invierte los elementos de una lista 