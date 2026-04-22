#creando tuplas con tuple()
tupla = tuple(["dato1", "dato2"])

#creando una tupla sin paréntesis de múltiples datos
tupla = "dato1","dato2"

#creando una tupla sin paréntesis de un solo dato
tupla = "dato",

print(tupla)

# En este archivo, vamos a crear tuplas
# Hay una forma de crear tuplas bastante interesante y es: tuple()
# creando tuplas con tuple()
# tupla = tuple()
# Es una función que nos permite crear una tupla 
# Adentro de la función tupla(), simplemente le ponemos los datos
# Por ejemplo
# tupla = tuple("dato1", "dato2") 
# Si ahora se muestra el dato...
# print(tupla)
# Pero tenemos que pasarle como parámetro una lista, o sea, recibe un solo parámetro que es una lista
# La lista que va a convertir en tupla
# tupla = tuple(["dato1", "dato2"])
# Entonces, ahora si se muestra print(tupla)
# print(tupla)
# se actualiza...
# y dice:
# ('dato1', 'dato2')
# También, existen formas de crear tuplas de una forma bastante particular
# Vamos a redifinir la tupla
# tupla = "dato1","dato2"
# En lugar de DESempaquetar, es como si empaquetaramos, (osea al revés)
# Así de sencillo se crea una tupla
# Si se le dice que muestre la tupla, teniendo comentado esto:
# tupla = tuple(["dato1", "dato2"])
# lo muestra igual con el print()
# ('dato1', 'dato2')
# Porque esta es una forma en la que también podemos crear tuplas sin los paréntesis 
# Si solamente ponemos los datos separados con coma (,), automáticamente, se crea la tupla
# tupla = "dato1","dato2"
# esto: tupla = "dato1","dato2"
# es lo mismo que poner esto: 
# tupla = ("dato1","dato2")
# Ahora la pregunta es: "¿Cómo hacemos para crear tuplas con un solo dato?"
# Si queremos crear un solo dato, la forma es poner el dato pero al final le ponemos una coma (,)
# tupla = "dato",
# ¿Por qué? 
# Porque si le ponemos esto: "dato" sin coma (,), es un string común y corriente
# Con la coma (,), ahora es una tupla
# Vamos a verificarlo
# Pero antes, vamos descomentar esto
# tupla = tuple(["dato1", "dato2"])
# ya que lo hacemos es redifinirlo, así que esto no afecta para nada a esto: tupla = "dato1","dato2"
# Vamos a crear una tupla así
# creando una tupla sin paréntesis de múltiples datos
# tupla = "dato1","dato2"
# creando una tupla sin paréntesis de un solo dato
# tupla = "dato",
# En la tupla sin paréntesis de múltiples datos, básicamente lo que hacemos es separar los datos con coma (,)
# Después de "dato2", no hace falta poner una coma (,)
# Entonces, no hace falta que se la agreguemos
# De hecho, si se quiere ver el tipo...
# print(type(tupla))
# Vamos a ver si efectivamente es una tupla
# Lo que muestra es esto:
# <class 'tuple'> 
# Sí, se comporta como tupla 
# Y si de repente la tupla se quiere crear solamente con un dato, ¿cómo hacemos?
# Así:
# tupla = "dato",
# Entonces, de esta forma creamos una tupla con tuple()
# tupla = tuple(["dato1", "dato2"])
# De esta forma, la creamos sin paréntesis 
# tupla = "dato1","dato2"
# Y de esta forma, la creamos con un solo dato
# tupla = "dato",
# Vamos a verificar a ver si se creó la tupla
# print(type(tupla))
# Muestra esto:
# <class 'tuple'>
# Se creó
# tupla = "dato",
# Esto también es una tupla, efectivamente. Funciona como tupla
# Y no, no es por esto:
# tupla = "dato1","dato2"
# Porque recordemos que acá la podemos redefinir
# O sea, ahora tupla es igual a (=) esto: "dato",
# no a esto: "dato1","dato2"
# De hecho, vamos a verificarlo...
# print(tupla)
# Muestra esto:
# ('dato',)
# Ahora es: tupla = "dato",
# Y ahí tenemos la tupla creada