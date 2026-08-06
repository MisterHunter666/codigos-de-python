#creando diccionarios con dict()
diccionario = dict(nombre="matias",apellido="bolonese")

#las listas no pueden ser claves y usamos fronzenset para meter conjuntos
diccionario = {frozenset(["matias","bolonese"]):"jajas"}

#creando diccionarios con fromkeys() valor por defecto: none
diccionario = dict.fromkeys("ABCDE","Algun valor fijo")

#creando diccionarios con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre","apellido"],"No se")


print(diccionario)

# Los diccionarios, como ya sabemos, se pueden crear como un json en javascript o con la función "dict"
# creando diccionarios con dict()
# y acá ponemos:
# diccionario = dict()
# La diferencia es que acá lo que nos va a pedir es un conjunto de "clave = valor"
# O sea, la estructura para crear un diccionario así es poner, por ejemplo:
# diccionario = dict(nombre="matias",apellido="bolonese")
# Entonces, de esta forma, creamos un diccionario
# Y si venimos acá y le damos: 
# print(diccionario)
# Esto, cuando se ejecuta, nos va a tirar el diccionario
# Acá, si nos fijamos, tenemos:
# {'nombre': 'matias', 'apellido': 'bolonese'}
# ¿Por qué?
# Porque efectivamente es como si creáramos variables dentro del diccionario ( dict() )
# Bueno, eso es el parámetro que recibe esta función ( dict() )
# Que efectivamente nos da por resultado la creación de un diccionario
# Es una forma diferente de crear un diccionario
# En vez de crearlo así:
# {
#   'nombre' : "matias",
#   'apellido' : "bolonese"
# }
# O sea, no hace falta que lo creemos de esta forma
# Lo podemos crear de esta forma:
# diccionario = dict(nombre="matias",apellido="bolonese")
# Podemos elegir la forma que nosotros prefiéramos
# No hay que olvidarse de que la forma en la que creamos datos vacíos es con esto:
# dict()
# No podemos crear diccionarios vacíos si usamos la forma de crearlo así:
# {}
# Si queremos crear diccionarios vacíos, los podemos usar con esta formula: dict()
# No podemos crear tuplas vacías a menos que usemos tuples(), la función
# No podemos crear listas vacías a menos que usemos list(), la función
# Entonces, es importante que entendamos esto
# En dict(), funciona igual
# Es decir, las listas no pueden ser claves porque son justamente iterables
# Acá vamos a ver, por ejemplo: 
# las listas no pueden ser claves 
# porque son mutables
# Si yo ahora acá, por ejemplo, creo un diccionario...
# diccionario = 
# Acá intento crear el diccionario con una lista, por ejemplo
# Si hacemos con una tupla, si nos fijamos, lo podemos hacer con una tupla
# diccionario = {(" ")}
# Por ejemplo:
# diccionario = {("matias","bolonese"):"jajas"}
# Actualizamos...
# {('matias', 'bolonese'): 'jajas'}
# Esto se muestra
# Las tuplas pueden ser claves
# Literalmente, estamos poniendo una tupla como clave
# Pero si hacemos con listas, es decir, reemplazamos el paréntesis ( () ) por el corchete ( [] ) que hace la lista 
# diccionario = {["matias","bolonese"]:"jajas"}
# Actualizamos...
# TypeError: unhashable type: 'list'
# Y ahora nos tira un error porque no es hashable 
# Lo que vimos antes, no funciona ni lo puede hacer
# Tampoco pueden ser, por ejemplo, los conjuntos
# Si queremos poner un conjunto...
# diccionario = {{"matias","bolonese"}:"jajas"}
# Actualizamos...
# TypeError: unhashable type: 'set'
# Tampoco me deja porque no es hashable
# Acá podríamos poner, por ejemplo, un frozenset()
# Si nosotros acá, por ejemplo, ponemos "frozenset()"...
# diccionario = {frozenset(["matias","bolonese"]):"jajas"}
# Acá pusimos paréntesis ( () )
# Acá lo hacemos como lista
# Si nosotros esto lo actualizamos...
# {frozenset({'bolonese', 'matias'}): 'jajas'}
# Ahora sí nos deja poner justamente el conjunto, frozenset()
# No hay que olvidarse de eso que es muy importante
# diccionario = {frozenset(["matias","bolonese"]):"jajas"}
# Ahí pusimos:
# las listas no pueden ser claves y usamos fronzenset() para meter conjuntos
# diccionario = {frozenset(["matias","bolonese"]):"jajas"}
# Ahí tenemos, perfecto
# Después, otra forma de crear diccionarios es con fromkeys()
# creando diccionarios con fromkeys()
# Esta es una función que nos permite crear un diccionario con todos los valores "none"
# O sea, sin valor, sin asignar
# ¿Cómo hacemos eso?
# Simple
# Ponemos:
# diccionario = fromkeys()
# Pero acá lo que hacemos es crear, por ejemplo, claves
# diccionario = fromkeys("nombre","apellido")
# Si ahora ejecutamos esto, nos va a decir que:
# NameError: name 'fromkeys' is not defined
# Está mal
# ¿Por qué esto tiene un error?
# Bien, el error es porque esto ( fromkeys() ) es un método de diccionarios
# Así que, tenemos que poner:
# dict.""""
# Que es el valor del diccionario
# dict es un tipo de dato
# diccionario = dict.fromkeys("nombre","apellido")
# Y acá lo creamos
# Ya actualizamos...
# Y corremos el programa...
# {'n': 'apellido', 'o': 'apellido', 'm': 'apellido', 'b': 'apellido', 'r': 'apellido', 'e': 'apellido'}
# Ahora, fijémosnos en qué nos creó
# Y el valor literalmente es "none" 
# Es:
# {'n': 'apellido', 'o': 'apellido', 'm': 'apellido', 'b': 'apellido', 'r': 'apellido', 'e': 'apellido'}
# ¿Por qué nos tira "nombre"?
# Es interesante esto
# Porque nos está haciendo que cada valor, que cada letra, "n,o,m,b,r,e", cada letra va a ser igual (=) al primero que nosotros pongamos acá
# ¿Cómo evitamos esto?
# Simple
# ¿Por qué funciona esto?
# Porque esto itera el primer elemento, es un iterable
# Entonces, tenemos que poner una lista... 
# diccionario = dict.fromkeys(["nombre","apellido"])
# Y ahora sí cerramos la lista
# Y cuando ejecutamos, nos creó...
# {'nombre': None, 'apellido': None}
# Y si seguimos agregando datos...
# diccionario = dict.fromkeys(["nombre","apellido","suscriptores"])
# Actualizamos...
# {'nombre': None, 'apellido': None, 'suscriptores': None}
# Esto nos crea básicamente todos los datos y todos los valores "none"
# Si nosotros acá, por ejemplo, decimos que nos muestre "diccionario["nombre"]"...
# print(diccionario["nombre"])
# Actualizamos...
# Y nos va a mostrar:
# None
# Y si ponemos "diccionario["apellido"]"
# Actualizamos...
# Y nos va a mostrar:
# None
# Y así con cualquier dato que le pidamos
# Esto es porque es una forma de crear diccionarios con todos valores sin definir
# Y es interesante la técnica esa en la que podemos crear un diccionario justamente con solamente pasarle una cadena de texto ( ["nombre","apellido","suscriptores"] ) que es lo que mostramos recién
# Si nosotros acá, por ejemplo, le pasamos una sola cadena de texto que diga: "ABCDE"
# diccionario = dict.fromkeys("ABCDE")
# print(diccionario)
# Actualizamos...
# Esto lo ejecuto...
# {'A': None, 'B': None, 'C': None, 'D': None, 'E': None}
# Y ahora me creó un diccionario con "A,B,C,D,E"
# Todos los valores con "none" pero "A,B,C,D,E"
# Incluso, si nosotros hacemos como hicimos antes y ponemos otro valor como, por ejemplo, "VALOR2"...
# diccionario = dict.fromkeys("ABCDE","VALOR2")
# Actualizamos...
# {'A': 'VALOR2', 'B': 'VALOR2', 'C': 'VALOR2', 'D': 'VALOR2', 'E': 'VALOR2'}
# Esto lo que hace es igualarnos "A,B,C,D,E" y siempre nos lo iguala a "VALOR2"
# Por defecto, viene así
# Entonces, si nosotros le pasamos un segundo valor...
# diccionario = dict.fromkeys("ABCDE","okasodkaods")
# Actualizamos...
# {'A': 'okasodkaods', 'B': 'okasodkaods', 'C': 'okasodkaods', 'D': 'okasodkaods', 'E': 'okasodkaods'}
# Lo que hace es igualar siempre a esto: "ABCDE"
# Entonces, el primer dato es un iterable, algo que podamos iterar
# Y el segundo dato es a lo que vamos a igualar fromkeys()
# Es interesante eso
# Entonces, en este caso, va a ser, por ejemplo, igual a: "Algun valor fijo"...
# diccionario = dict.fromkeys("ABCDE","Algun valor fijo")
# creamos diccionarios con fromkeys() con dos parametros
# creando diccionarios con fromkeys() con dos parametros
# Actualizamos...
# {'A': 'Algun valor fijo', 'B': 'Algun valor fijo', 'C': 'Algun valor fijo', 'D': 'Algun valor fijo', 'E': 'Algun valor fijo'}
# Y después podemos hacer lo mismo acá:
# Acá podemos pasar una lista, por ejemplo, incluso
# Podemos ponerle:
# diccionario = dict.fromkeys(["nombre","apellido"],"No se")
# Actualizamos...
# Y nos va a mostrar:
# {'nombre': 'No se', 'apellido': 'No se'}
# Hacemos estos últimos arreglos:
# creando diccionarios con fromkeys() valor por defecto: none
# diccionario = dict.fromkeys("ABCDE","Algun valor fijo")
# creando diccionarios con fromkeys() cambiando el valor por defecto a "no se"
# diccionario = dict.fromkeys(["nombre","apellido"],"No se")
# Actualizamos...
# Acá tenemos:
# {'nombre': 'No se', 'apellido': 'No se'}
# Y funciona igual, así es cómo funciona este apartado de diccionarios
# Ahora, ¿cómo podemos iterar justamente un conjunto por ejemplo?
# Porque sí, las listas, si nos acordamos, los diccionarios los podemos llamar así:
# print(diccionario["nombre"])
# Y llamamos al valor...
# Y nos muestra:
# No se
# Decimos, por ejemplo:
# print(tupla)
# "1" y nos muestra el primer dato
# Decimos:
# print(listas)
# "1" y nos muestra el primer dato
# Pero los conjuntos, ¿cómo podemos ver el valor de un conjunto?
# ¿Cómo podemos por ejemplo llamar al dos ("2")?
# ¿Cómo hacemos para llamar al dos ("2")?
# ¿O cómo hacemos para que nos muestre el siete ("7")?
# Solo el siete ("7")
# Para esto, tenemos que iterarlo, porque los conjuntos son iterables
# Pero, ¿qué es todo esto de iterar? ¿de qué estamos hablando?
# Bien
# Todo esto lo vamos a ver en el siguiente apartado que es el apartado de "bucles"
# Así que, vamos a ver qué son los bucles...