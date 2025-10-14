# Vamos a ver el apartado de inputs y de diccionarios

# keys() -> devuelve las claves (también nos sirve para iterar)
# get() -> devuelve el valor de una clave
# clear() -> elimina todos los elementos
# pop() -> elimina un elemento
# items() -> para iterar el dict

# Estos cinco métodos son los que normalmente utilizamos cuando trabajamos con diccionarios

# creamos un diccionario
diccionario = {
    "nombre" : 'matias',
    "apellido" : 'bolonese',
    "subs" : 500
}

# Es un diccionario con tres(3) elementos 
# Un nombre, que es igual a "matias"
# Un apellido, que es igual a "bolonese"
# y la cantidad de suscriptores, que son quinientos(500)

#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un elemento con get() (si no encuentra nada el programa continúa) 
valor_de_kasdks = diccionario.get("kasdks")
print("hola papa, el programa continua")

# claves = diccionario.keys()

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("subs")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

# Si ahora mostramos esto en un print, vamos a ver qué es lo que nos muestra
print(diccionario_iterable)

# print(claves)
# dict_keys(['nombre', 'apellido', 'subs'])

# Esto nos devuelve dict.case, que son "nombre", "apellido" y "subs"

# ¿Para qué nos sirve keys también?
# Bien, también nos sirve para iterar

# Se pueden iterar tanto con items como con keys

# keys() es un método muy común y es, justamente, nos permite iterar en un futuro estos elementos para poder tener una tupla con todos los elementos, con todas las claves.

# Después tenemos get(), que get() es muy simple, acá le pasamos, por ejemplo, "nombre", un valor
# claves = diccionario.get("nombre")
# con get() le pasamos un valor
# devuelve "matias"
# Cuando lo accedemos, nos va a devolver el valor, "matias", "nombre" igual "matias"
# si se le pasa, por ejemplo, "apellido"...
# claves = diccionario.get("apellido")
# devuelve "bolonese"
# si se le pasa "subs"...
# claves = diccionario.get("subs")
# devuelve "500"

# Es como básicamente en una lista, hacer esto: [] y poner elemento [0], elemento [1], elemento [2]

# claves = diccionario[0].get("subs")
# claves = diccionario[1].get("subs")
# claves = diccionario[2].get("subs")

# De hecho, algo interesante acá es que nosotros podemos llamar a los elementos por números como si fuera una lista
# o sea que literalmente podemos hacer esto:

# diccionario = {
#     0 : 'matias',
#     1 : 'bolonese',
#     2 : 500
# }

# funciona, o sea si ahora de repente se pone esto, por ejemplo:
# claves = diccionario[0]
# Actualizo y me muestra "matias", porque esto:
#     0 : 'matias',
#     1 : 'bolonese',
#     2 : 500
# es como si fuera literalmente una lista, solamente que no es una lista porque no es un objeto tipo lista, o sea no se va a comportar como lista.
# Lo podemos llamar como lista, porque decimos "diccionario[0]" y parece tal cual una lista, nos muestra este elemento: "matias"
# Una lista es literalmente un diccionario, solamente que el índice ya viene por defecto y es auto incrementable, o sea se va incrementando por cada elemento que agregemos automáticamente.
# Pero en un diccionario también lo podemos hacer, podemos agregar los números como si fuera una lista, pero para eso creamos una lista y ya está.
# El diccionario tiene otros usos, tiene otra forma de trabajar justamente con clave o valor y por eso es un diccionario.
# si no haríamos listas, sí lo haríamos de esta forma:
# diccionario = {
#     "nombre" : 'matias',
#     "apellido" : 'bolonese',
#     "subs" : 500
# }
# por eso justamente es importante diferenciarlo
# Cada objeto, cada elemento que creemos tiene que ir acorde al tipo de dato que querramos trabajar y al contexto
# Entonces...
# diccionario = {
#     "nombre" : 'matias',
#     "apellido" : 'bolonese',
#     "subs" : 500
# }
# esto es lo correcto

# ¿Y para qué usamos get()?
# Si lo podemos hacer tranquilamente así:
# claves = diccionario["subs"]
# Bueno, lo que pasa es que si yo ahora, por ejemplo, hago esto:
# claves = diccionario("kasdks")
# y no me lo encuentra, esto me va a lanzar una excepción y es un KeyError.
# Pero si se le pasa get() y adentro se le pasa un nombre que no es, esto no me lanza una excepción, sino que me dice "None"
# claves = diccionario.get("kasdks")
# Es decir, mientras que uno me lanza una excepción el programa se para completamente y no continúa, el otro me dice: "si no lo encuentro, te voy a devolver "None", no te voy a dar un error"
# None nos indica que no tiene valor. Parecido al undefined en javascript
# Esa es la diferencia, entonces el programa continúa, si, por ejemplo se pone...
# print("hola papa")
# actualizo esto y me dice: 
# "hola papa"
# None
# Pero si, por ejemplo, se pone una cosa que no va a encontrar, el programa no continúa, se traba ahí y ahí finalizó, nos lanzó un error 
# claves = diccionario("oksdoskaoda")
# devuelve KeyError
# Entonces, esa es la diferencia, con una, el programa continúa, con otro no.
# Además get(), podemos ya trabajarlo y entender que es un getter(), que vamos a ver más adelante que es un getter().
# pero un getter() básicamente es un método que puede acceder a una propiedad particular de un objeto.
# pero ya vamos a ver bien lo que son los objetos.
# obteniendo un elemento con get() (si no encuentra nada, el programa continúa)  
# claves = diccionario.get("kasdks")

# nos devuelve un objeto dict_item
# claves = diccionario.keys()
# dict_item es un tipo de objeto que se puede iterar
# obteniendo un elemento con get() (si no encuentra nada, el programa continúa)  
# valor_de_kasdks = diccionario.get("kasdks")
# ¿por qué "kasdks"? porque eso es lo que obtiene, está obteniendo el valor de esto: "kasdks"
# Las variables tienen que ser intuitivas, cuando nosotros creamos una variable, la variable tiene que ser efectivamente algo que describa lo que contiene adentro, entonces, ¿qué contiene adentro? el valor de "kasdks"
# y después imprimo con print: "hola papa, el programa continua".
# print("hola papa, el programa continua")
# actualizamos...
# hola papa, el programa continua
# dict_keys(['nombre', 'apellido', 'subs'])
# y ahí vemos que funciona.
# y tenemos lo que necesitamos obtener.

# Ahora, vamos a seguir con el siguiente método que es clear()
# clear() elimina todos los elementos del diccionario
# es decir, si se pone... 
# eliminando todo del diccionario
# diccionario.clear()
# y ahora vamos a ver el valor del diccionario
# verifiquemoslo, vamos a ver que hay adentro...
# print(diccionario)
# devuelve esto:
# hola papa, el programa continua
# {}
# adentro no tiene nada
# es un diccionario vacío
# eso es lo que hace clear()
# elimina todo del diccionario

# Después, tenemos otra función que es pop()
# con pop(), eliminamos un elemento del diccionario
# así como eliminamos pop(), eliminamos elementos de tuplas, de listas y demás, con pop() también podemos eliminar elementos del diccionario
# por ejemplo, si se pone...
# eliminando un elemento del diccionario
# diccionario.pop("nombre")
# corro el programa y me dice:
# hola papa, el programa continua
# {'apellido': 'bolonese', 'subs': 500}
# si ahora de repente se quiere sacar el apellido porque estar con el nombre parece suficiente, el apellido no hace falta, bueno, digo esto y ahora me devuelve el nombre:
# diccionario.pop("apellido")
# hola papa, el programa continua
# {'nombre': 'matias', 'subs': 500}
# y si ahora de repente se quiere sacar los subs, saco los subs
# diccionario.pop("subs")
# hola papa, el programa continua
# {'nombre': 'matias', 'apellido': 'bolonese'}
# y suponiendo que se quiera sacar más elementos, pongo la coma(,) y el elemento (" "):
# diccionario.pop("subs","nombre")
# actualizo...
# hola papa, el programa continua
# {'nombre': 'matias', 'apellido': 'bolonese'}
# y ahora saca "nombre" y "subs"

# Y por último, tenemos items()
# items() nos devuelve exactamente el diccionario
# o sea, si ahora, por ejemplo, se muestra el diccionario, me devuelve esto:
# {'nombre': 'matias', 'apellido': 'bolonese'}}
# si ahora, de repente, se dice:
# obteniendo un elemento dict_items iterable
# diccionario_iterable = diccionario.items()
# vamos a ver que es lo que devuelve en diccionario es esto:
# print(diccionario)
# hola papa, el programa continua
# {'nombre': 'matias', 'apellido': 'bolonese'}
# mientras que lo que devuelve en diccionario_iterable es otra cosa que es esto:
# print(diccionario_iterable)
# hola papa, el programa continua
# dict_items([('nombre', 'matias'), ('apellido', 'bolonese')])
# entonces, lo que devuelve "diccionario" es una cosa, y lo que devuelve "diccionario_iterable" es otra, ¿por qué? bueno, porque "diccionario" no se puede iterar
# básicamente, iterar es recorrer el elemento, ya se va a ver más adelante
# estamos recorriendo el elemento para poder acceder a cada uno de los elementos, en "diccionario" no se puede, mientras que en "diccionario_iterable" sí
# ya cuando se vea el tema "bucles" se va a ver
# así que, de hecho, lo próximo que vamos a ver después de los "inputs" y los ejercicios y todo lo que se haga, es los "bucles", o sea, "inputs", ejercicio y "bucles", y ahí vamos a volver a trabajar con esto, pero antes de ver eso, hay que entender bien cómo son los "inputs", cómo funcionan para que se cierre este ciclo y se comience con los primeros ejercicios prácticos que se van a hacer en lo que va del curso
# así que, hasta acá se deja este apartado de métodos de diccionarios, y ahora sí se continúa con los "inputs"(entrada de datos, "data inputs")...