# Los metodos de listas son métodos que vamos a poder aplicar a listas para operarlas.

#Creando una lista con list()
lista = list([34,56,23,True,False])

#devuelve la cantidad de elementos de la lista.
cantidad_elementos = len(lista)

#agregando un elemento a la lista
lista.append(65)

#agregando un elemento a la lista en un indice específico
lista.insert(2,"TOMA MAMA")

#agregamos varios elementos a la lista 
lista.extend([False,2030])

#eliminando un elemento de la lista (por su indice)
lista.pop(3) #-1 para elminar el último, -2 para eliminar el anteultimo, y así sucesivamente

#removiendo un elemento de la lista por su valor
lista.remove("TOMA MAMA")

#eliminando todos los elementos de la lista
# lista.clear()

#ordenando la lista de forma ascendente(si usamos el parametro reverse=True lo ordena en reversa)
lista.sort()

#invirtiendo los elementos de una lista
lista.reverse()

#verificando si un elemento se encuentra en la lista 
elemento_encontrado = lista.index(56)

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
# remove() también remueve.
# Solamente que remove() remueve un elemento de la lista por su valor.
# O sea, ahora vamos a remover un elemento por su valor.
# Es decir, al elemento lo buscamos con lista.remove()
# removiendo un elemento de la lista por su valor
# lista.remove("TOMA MAMA")
# Ahora tenemos que buscar cómo se llama el elemento. 
# Si lo encuentra, lo elimina.
# Entonces, si ahora lo buscamos, lo eliminó.
#['hola', 'matias', 34, 56, 23, True, 'JAJAJAJA', False, 2030]
# Antes "TOMA MAMA" estaba en la posición dos (2), ahora ya no está más en la lista.
# Si le pasamos un parámetro que no encuentra, no va a remover nada. Y no solamente eso, sino que nos lanza una excepción.
# lista.remove("TOMA 9D8AS9MAMA")
# Por eso es importante manejar esta excepción.
# Y en este caso, pasarle un parámetro que sabemos que tiene.
# lista.remove("TOMA MAMA")
# Entonces, ahora sí cómo encontró "TOMA MAMA", lo puede eliminar. 
# Y ya no tiene más "TOMA MAMA". 
# ['hola', 'matias', 34, 56, 23, True, 'JAJAJAJA', False, 2030]
# Si le pedimos que elimine el "56", elimina el "56".
# lista.remove(56)
# ['hola', 'matias', 'TOMA MAMA', 34, 23, True, 'JAJAJAJA', False, 2030]
# Eliminó el "56"
# Vamos a poner "TOMA MAMA", para que así como se agregó, se elimine. 
# lista.insert(2,"TOMA MAMA")
# lista.remove("TOMA MAMA")

# Y después, por último, tenemos el clear()

# CLEAR - elimina todos los elementos de una lista
# El clear() elimina todo. Es decir, elimina todos los elementos de la lista
# eliminando todos los elementos de la lista
# lista.clear()
# Así nomás, lista.clear() y los elimina todos.
# Por eso, lo vamos a dejar al final.
# Aunque sea algo que elimine, lo vamos a dejar al final porque no queremos que nos elimine la lista.
# De hecho, si fijamos cómo está esta lista y la mostramos ahora, nos va a decir que es una lista vacía.
# []
# Nos pasó una lista vacía.
# Porque todos los elementos fueron eliminados.
# Así como no queremos esto, vamos a, por ahora, comentarla.
# lista.clear()
# Como la comentamos, actualizamos y ya no se ejecuta más.
# ['hola', 'matias', 56, 23, True, 'JAJAJAJA', False, 2030]

# Vamos a ir con el siguiente...

# SORT - ordena una lista de forma ascendente a descendente
# sort() es una función que ordena los elementos de forma ascendente.
# Si, por ejemplo, se le dice lista.sort(), vamos a ver qué muestra ahora
# lista.sort()
# Lo que pasa es que esto no funciona si la lista tiene cadenas de texto. 
# Entonces, lo que tenemos que hacer es borrar todas las cadenas de texto.
# Así que, vamos a borrar todas las cadenas de texto. 
# Borramos las cadenas de texto.
# lista = list([34, 56, 23, True])
# Y también, borramos el "JAJAJAJA" y vamos a crear un elemento que sea, por ejemplo, un "65".
# lista.append(65)
# Y el "False" también lo vamos a borrar y vamos a sacarlo.
# lista.extend([2030])
# Ahora si actualizamos, efectivamente, nos puede ordenar.
# Así que vamos a actualizar
# [True, 34, 56, 65, 2030]
# Ahora sí nos pudo ordenar.
# Aunque haya un "True", los True van primero, ¿por qué?, porque me agregó un "True". El "True" está al final. 
# [34, 56, 23, True]
# Yo agrego un "False"
# Vamos a ver qué pasa
# lista = list([34,56,23,True,False])
# También en esta parte
# lista.extend([False,2030])
# Vamos a ver qué pasa ahora si le agregamos dos "False"
# [False, False, True, 34, 56, 65, 2030]
# Los "False" vienen primero. Los "True" vienen segundos.
# Y después, vienen los números
# Del menor (34) al mayor (2030)
# A esto, también, le podemos dar una propiedad que es: reverse() = True
# lista.sort(reverse=True)
# Si le agregamos eso, lo que sucede es que se invierten.
# [2030, 65, 56, 34, True, False, False]
# O sea, ahora los ordenamos pero los ordenamos al revés. En inversa.
# Es como si agarráramos cada uno de los elementos y los invirtiéramos.
# Como que los diéramos vuelta automáticamente. 
# 1, 2, 3, 4, 5
# 5, 4, 3, 2, 1
# Entonces, así es como funciona esto, los da vuelta.
# Lo que antes era el elemento cinco (5), ahora es el elemento uno (1).
# Lo que antes era el elemento uno (1), ahora es el elemento cinco (5).
# Y así
# Vamos a poner ahora: "ordenando la lista (si usamos el parametro reverse=True lo ordena en reversa)"
# ordenando la lista (si usamos el parametro reverse=True lo ordena en reversa)
# lista.sort(reverse=True)
# Vamos a sacar el parametro "reverse=True"
# lista.sort()
# Ahora sí
# Vamos a poner ahora: "ordenando la lista de forma ascendente(si usamos el parametro reverse=True lo ordena en reversa)"
# lista.sort()
# ordenamos la lista de forma ascendente, es decir, hacia arriba. De menor a mayor.
# Si lo ponemos en reversa, es decir, ordenarlo en reversa, lo ordena de forma descendente. Desde el mayor al menor.

# Y por último, tenemos reverse() 

# REVERSE - invierte los elementos de una lista 
# Reverse() no hace lo mismo que sort() con el parametro "reverse" en True, sino que lo que hace es, justamente, "invierte los elementos", los invierte. O sea, si primero la ordenamos y después le damos en "reverse": "invirtiendo los elementos de una lista".
# lista.reverse()
# Si primero lo que hacemos es ordenar la lista, después eventualmente si va a ser el mismo resultado
# [2030, 65, 56, 34, True, False, False]
# Efectivamente, nos da el mismo resultado
# Si actualizamos, literalmente nos da el mismo resultado. Nos ordena de mayor a menor, ¿por qué? porque sort() lo que hace es ordenarla. 
# Si se le pusiera al sort() el parametro "reverse=True", haría lo mismo que reverse()
# lista.sort(reverse=True)
# Pero si se le sacara el sort(), reverse() lo que hace es la cadena que ya existe, simplemente, la cambia de lugar.
# [2030, False, 65, False, True, 56, 34]
# El elemento por defecto es así
# [34, 56, True, False, 65, False, 2030]
# Si le agregamos el reverse(), se invierte completamente
# [2030, False, 65, False, True, 56, 34]
# Entonces, el reverse() funciona para cualquier lista, revertirla. Solamente que el sort() lo que hace es primero la ordena y si le pasamos el parámetro "sort=True", también lo puede hacer al inversa.
# Solamente que el reverse() lo hace sin ordenarla.
# O sea, puede estar desordenada la lista porque, de todas formas, la revierte.
# El que antes era el primer número, ahora es el último. Lo que antes era el segundo número, ahora es el anteúltimo.
# Y lo que antes era el último número, ahora es el primero. Lo que antes era el anteúltimo, ahora es el segundo de la lista.
# [34, 56, True, False, 65, False, 2030]
# [2030, False, 65, False, True, 56, 34]
# Así funciona reverse()

# Y ahí, más o menos, tenemos todos y cada uno de los elementos de la lista
# Así que, ya estuvimos viendo lo que vienen siendo los métodos de las listas
# De hecho, las tuplas, justamente, y los sets, que son los conjuntos, también tienen sus propios métodos, pero son bastante diferentes. 
# Es decir, si ahora, por ejemplo, mostráramos "dir(lista)"...
# print(dir(lista))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# nos va a mostrar todas las cosas que podemos hacer con una lista y las podemos ver.
# Mientras que si buscáramos los de una tupla...
# print(dir('dkasodksa'))
# esta es una tupla porque la creamos con paréntesis
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# nos dice que las cosas son diferentes
# Algunas cosas sí son similares, como el endswith(), como el isnumeric(), como el upper(), el join(), ¿pero por qué? porque funciona casi como un string.
# Vamos a agregar cualquier otro elemento más, así funciona como lista
# print(dir(('dkasodksa',5)))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
# Ahora sí funciona como una tupla
# Tenemos valores diferentes
# Tenemos casi pocas funciones
# Lo único que se puede hacer con las tuplas es contarlas, contar cuántos elementos tiene y usar la función index()
# La función index() también es para buscar un elemento
# Esas son las únicas dos cosas que podemos hacer.
# index() para buscar elementos y count()
# Así como index() nos buscaba, justamente, letras y nos devolvía la posición en la que estaba, nos devuelve también la posición en la que está el elemento que estamos buscando 
# busqueda_index = cadena1.index("H")
# Acá ya no funciona por caracteres, acá ya funciona por el elemento completo
# Si, por ejemplo, se pone...
# verificando si un elemento se encuentra en la lista 
# elemento_encontrado = lista.index(56)
# Si quero buscar, por ejemplo, el "56", que lo tenemos en la lista...
# actualizo...
# Y si le pido que me lo muestre, vamos a pedirle que me lo muestre...
# print(elemento_encontrado)
# lo que nos va a devolver es...
# devuelve "2"
# ¿por qué? porque la posición en la que se encuentra el "56" es el dos (2)
# [2030, 65, 56, 34, True, False, False]
#  |     |   |  
#  v     v   v     
#  0     1   2 
# La posición es el dos (2)
# Si le pedimos que encuentre, por ejemplo, el "34", o más fácil, le pedimos que encuentre el "True", le pasamos el "True"...
# elemento_encontrado = lista.index(True)
# vamos a hacer una predicción
# [2030, 65, 56, 34, True, False, False]
#  |     |   |   |   |
#  v     v   v   v   v
#  0     1   2   3   4
# Nos tiene que lanzar un cuatro (4)
# Actualizamos 
# y nos lanzó un cuatro (4)
# Así funciona
# Pero qué pasa si, por ejemplo, se le dice que busque el "5"
# elemento_encontrado = lista.index(5)
# ¿El "5" lo va a encontrar?
# ValueError: 5 is not in list
# No
# Hay un "56", pero no hay un "5"
# Por más que "56" tenga "5", esto busca elementos completos
# "5" no es "56"
# Esto, básicamente, agarra cada elemento y dice: "Esto qué me pasó, ¿es igual al elemento de la lista?"
# elemento_encontrado = lista.index(5)
# [34,56,23,True,False]
#  |  |  |                 
#  v  v  v                    
#  no no no      
#     |
#     v
#     sí tiene un "5", 
# pero no es igual a "56"    
# El index() lo que busca, justamente, en listas es: "si este elemento es igual a alguno de los de la lista" 
# Y "5" no es igual a ningún elemento
# "56" contiene "5", pero no es igual "5" a "56"
# Está bueno eso que se tenga en cuenta
# También, nos lanza errores
# Así que, vamos a darle "56" para que lo encuentre
# elemento_encontrado = lista.index(56)
# devuelve dos (2)
# Ahora sí, ahí lo encontró y nos devolvió el índice
# Así funcionan las tuplas
# lista = list([34,56,23,True,False])
# Si esto en vez de ser una lista, fuera una tupla, lo que podemos hacer con las tuplas es solamente buscar elementos y contarlos.
# Porque si intentáramos en una tupla, invertirla, revertirla o alterarla de cualquier forma, no podemos
# Porque, justamente, las tuplas y los conjuntos son inmutables.
# Podemos redeclararlos, pero no podemos cambiar ningún elemento
# No podemos cambiar el orden, por ejemplo, de ningún elemento de la tupla.
# Pero si vamos a, por ejemplo, lo que puede hacer un diccionario, por ejemplo, ponemos dir(), y ponemos un conjunto, que los hacemos con "set"
# print(dir(set))
# Y vamos a agregar, por ejemplo, un valor y otro valor
# # print(dir(set(["lasodksad","osdksodk"])))
#               |           |
#               v           v
#               valor 1     valor 2
# Entonces, actualizamos y tenemos el set creado
# ['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
# Lo que nos dice es esto que se puede hacer 
# Ahora sí, lo que podemos hacer es sacar elementos de los conjuntos, remover elementos de los conjuntos, pero no podemos agregar elementos.
# Es decir, no podemos usar el append(), no podemos usar el extend(). 
# Solamente podemos sacar elementos y remover elementos
# Ni siquiera podemos usar el index()
# Si de repente usamos con esto el index()...
# Vamos a sacar una lista
# elemento_encontrado_en_conjunto = set(["soadisaodi",54]).index(54) 
# A ver si encuentra el elemento "54"
# actualizamos...
# AttributeError: 'set' object has no attribute 'index'
# y nos tira una excepción
# porque no se puede usar index() en conjunto
# Si se quiere ver cuáles son todas las cosas que se puede hacer, hay que usar, simplemente, dir() y se ve como se vió recién
# En definitiva, es interesante que podamos ver esto y no, efectivamente no se puede usar el index() en sets.
# En las tuplas, solamente podemos buscar elementos y usar el index()
# Mientras que en los conjuntos podemos hacer todo lo que se vió antes, que es copiarlos, limpiarlos... 
# Es decir, si podemos eliminar todos los elementos de un conjunto, podemos copiarlos, podemos removerlos...
# Y si se quiere ir viendo qué hacen las diferentes funciones, se recomienda investigarlas.
# Pero no son más que las que se vieron hasta ahora.
# Lo que sí, después tenemos los métodos de diccionarios que también tienen sus cosas.
# O sea, tampoco podemos hacer tanto como con las listas, pero podemos hacer otras cosas interesantes.