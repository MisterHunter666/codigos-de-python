#creando un conjunto con set()
conjunto = set(["Dato 1"])

#Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato 1", "dato 2"])
conjunto2 = {conjunto1,"dato 3"}
print(conjunto2)

#Teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7} 

#Verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#Verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

#verificar si hay algún número en comun 

resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)

# Los conjuntos también los podemos crear con una función set() como ya vimos al principio
# creando un conjunto con set()
# conjunto = set( )
#                |
#                v
#            acá le pasamos
#              datos

# Lo que la función set() necesita como parámetro es un iterable, ya vamos a ver bien qué es un iterable y demás cosas que estamos a punto de llegar a eso
# A la función set() le vamos a pasar una lista, una lista que, por ejemplo, puede ser:
# conjunto = set(["Dato 1", "Dato 2"])
# Si le damos print("set")...
# Muestra "set" en la terminal, efectivamente
# Vamos a darle print(conjunto)
# Actualizamos...
# Y ahora se muestra:
# {'Dato 1', 'Dato 2'}
# Ya tenemos el conjunto funcionando
# Ahora, ¿qué pasa cuando queremos poner un elemento modificable en otro no modificable?
# Recuerden que los datos, por ejemplo, de sets no son modificables, o sea, no podemos decir que "set tal" va a ser igual a (=) otro dato porque no funciona
# ¿Cómo podemos hacer para poner datos que sí se pueden cambiar en datos que no se pueden cambiar?
# Si ahora, por ejemplo, a "conjunto" le pusiera otro dato, supongamos que adentro de la lista se pone una lista, se pone una lista dentro de otra lisa, ¿eso es posible?
# Vamos a poner una lista que sea dato en lista 1 y dato en lista 2
# conjunto = set(["Dato 1",["datoenlista1","datoenlista2"]])
# Actualizamos...
# Eso no se puede hacer porque dice que se le está pasando una lista y la lista es "unhashable"
# Básicamente, no se puede "hashar" dentro del set porque esos datos no se pueden modificar
# Y la lista es mutable, una lista puede mutar y acá solamente pueden ir datos que no se muten
# Entonces, deberíamos usar una tupla
# Si ahora se reemplaza esto por una tupla...
# conjunto = set(["Dato 1",("datoenlista1","datoenlista2")])
# Se actualiza...
# Y si se corre el programa...
# {'Dato 1', ('datoenlista1', 'datoenlista2')}
# Ahora sí se puede ejecutar porque las tuplas van adentro de otros datos
# O sea que tampoco funcionaría con un diccionario 
# Si esto se convierte en un diccionario...
# conjunto = set(["Dato 1",{"datoenlista1","datoenlista2"}])
# Tampoco se deja poner diccionarios porque dice que no se puede "hashar" el set
# ¿Pero cómo hacemos si se quiere meter un conjunto dentro de otro conjunto?
# Bueno, vamos a probar a ver qué pasa si se lo saca
# Vamos a poner...
# Metiendo un conjunto dentro de otro conjunto
# conjunto1 = {"dato 1", "dato 2"}
# conjunto2 = {conjunto1,"dato3"}
# ¿Esto funcionaría? ¿Este conjunto puede estar dentro de otro conjunto? ¿Pueden existir conjuntos anidados?
# Vamos a verlo...
# Ahora ponemos que se muestre "conjunto2"
# print(conjunto2)
# Actualizamos...
# No deja poner un conjunto dentro de otro conjunto
# ¿Cómo se tiene que hacer si se quisiera meter un conjunto dentro de otro conjunto?
# Bueno, hay que usar una función llamada "frozenset()", que es conjunto congelado
# conjunto1 = frozenset(["dato 1", "dato 2"])
# Esto también crea un conjunto, pero crea un conjunto inmutable y que puede estar congelado como para que sea "hashable" 
# Entonces, si ahora se actualiza y se corre el programa...
# print(conjunto2)...
# {'dato 3', frozenset({'dato 2', 'dato 1'})}
# Va a decir que ahora sí se pudo meter un conjunto dentro de otro conjunto
# Y, efectivamente, este conjunto se comporta como un conjunto normal, es literalmente un conjunto normal
# Vamos a verificarlo porque antes estaba "conjunto" y no sabemos si se estaba ejecutando bien
# creando un conjunto con set()
# conjunto = set(["Dato 1"])
# Metiendo un conjunto dentro de otro conjunto
# conjunto1 = {"dato 1", "dato 2"}
# conjunto2 = {conjunto1,"dato 3"}
# print(conjunto)
# Actualizamos...
# Y ahora muestra error
# Si se pone de esta forma, con el frozenset()...
# creando un conjunto con set()
# conjunto = set(["Dato 1"])
# Metiendo un conjunto dentro de otro conjunto
# conjunto1 = frozenset(["dato 1", "dato 2"])
# conjunto2 = {conjunto1,"dato 3"}
# print(conjunto2)
# {'dato 3', frozenset({'dato 2', 'dato 1'})}
# Ahí ya no tira más error
# Entonces, esta es la forma y la respuesta que nos viene a dar frozenset() que es para meter un conjunto dentro de otro conjunto
# Si queremos trabajar con un conjunto o si estamos trabajando con conjuntos, necesitamos entender lo siguiente:
# En teoría de conjuntos, tenemos por un lado lo que viene siendo un conjunto y por otro lado lo que viene siendo un subconjunto, que es como agarrar un par de datos del otro conjunto y crear un conjunto aparte 
# Es decir, si, por ejemplo, se tiene el conjunto "A", que tiene los datos que estamos viendo (2, 4, 6), y, además, se tiene el conjunto "B", que tiene los datos que estamos viendo (2, 4, 6, 8, 10), "A" es un subconjunto de "B" porque "A" tenemos solamente tres (3) datos que están en el conjunto "B", solamente que en "B" tenemos más conjuntos
# Entonces, "A" es un subconjunto de "B", porque "B" tiene todo "A" y más 
# Esta, justamente, es la teoría de conjuntos (casi)
# Un conjunto que incluye a otro y, además, tiene más datos, es un superconjunto de otro conjunto (en este caso, el conjunto "B") 
# Es decir, tenemos dos (2) perspectivas:
# La primer perspectiva es que "A" es un subconjunto de "B"
# Entonces, "A" es un subconjunto y "B" es un conjunto 
# Mientras que podemos tener la otra perspectiva que es ver a "B" como un superconjunto de "A" y "A" es un conjunto 
# Es depende del elemento que tomemos como referencia 
# Es decir, si decimos que "B" es un conjunto, "A" es un subconjunto de "B"
# Y si decimos que "A" es un conjunto, "B" es un superconjunto de "A"
# Esta es la teoría que se tiene que entender porque si queremos trabajar justamente con las siguientes funciones, tenemos que ver justamente esta teoría que es bastante interesante
# Así que, la vamos a llevar a la práctica
# Y vamos a venir acá poniendo:
# Teoria de conjuntos
# Vamos a crear devuelta el conjunto 1 y el conjunto 2
# Conjunto 1 va a ser igual a (=) un conjunto de numeros
# Vamos a poner: {1,3,5,7}
# conjunto1 = {1,3,5,7}
# Son numeros que son impares
# Y conjunto 2 vamos a poner: {1,3,7}
# Vamos a poner estos tres numeros
# ¿Cómo verificamos si un conjunto es un subconjunto de otro?
# Bien, decimos: 
# resultado es igual a... 
# resultado =
# En el resultado, se va a almacenar true o false porque estas funciones que vamos a usar ahora nos devuelven true o false, valores booleanos
# Decimos: ¿conjunto 2 es un subconjunto de conjunto 1?
# resultado = conjunto2.issubset(conjunto1)
# Este método ("issubset") nos devuelve ese dato 
# Es decir... 
# conjunto2.issubset
#     |        |   
#     v        v
# ¿conjunto 2 es un subconjunto?
# "issubset" significa "¿es un subconjunto de conjunto 1?" (en este caso)
# Vamos a ver qué nos responder, vamos a poner "print()"
# print(resultado)
# Y vamos a ejecutar esto y nos va a decir... 
# "True"  
# ¿Por qué?
# Porque es un subconjunto, porque en conjunto 1 podemos encontrar {1,3,7}
# Pero si ahora cambiamos los numeros y le decimos:
# ¿conjunto 1 es un subconjunto de 2?
# resultado = conjunto1.issubset(conjunto2)
# No
# Porque conjunto 1 tiene más cosas
# Entonces, no
# Devuelve "False"
# O sea, todo lo que está en 1 no está en 2 
# Pero al revés sí, es decir, todo lo que está en 2 está en 1
# Entonces, 2 es un subconjunto de 1
# Actualizamos
# resultado = conjunto2.issubset(conjunto1)
# Nos devuelve "True" 
# Entonces, acá vamos a poner:
# Verificando si es un subconjunto
# resultado = conjunto2.issubset(conjunto1)
# Otra forma de verificar si es un subconjunto o no es utilizando el menor o igual (<=)
# Acá ponemos:
# resultado es igual a (=) conjunto 2 menos o igual a (<=) conjunto 1
# resultado = conjunto2 <= conjunto1
# Esto funciona exactamente igual
# resultado = conjunto2.issubset(conjunto1)
# resultado = conjunto2 <= conjunto1
# El "issubset" o el menor o igual (<=) es lo mismo porque lo que comprueba es que estos numeros sean mayores o iguales a estos 
# Es sencillo, es una forma de verificarlo
# Vamos a verificarlo, vamos a comentar esta línea
# Vamos a ver si nos funciona 
# resultado = conjunto2 <= conjunto1
# Nos devuelve...
# "True"
# Efectivamente
# Porque es una forma de verificar
# Lo invierto nuevamente y ponemos...
# resultado = conjunto1 <= conjunto2
# Devuelve "False"
# Y se dirá: "No, porque es por la cantidad de datos"
# No, no es por la cantidad de datos porque si le damos, por ejemplo...
# conjunto1 = {1,3,-10,7}
# Si se le pusiera menos diez (-10), tecnicamente, la suma de todos estos es menos, no es por la suma
# Yo actualizo...
# "True"
# E igual sigue dando "True"
# Así que, no tiene nada que ver con que los numeros lo suman
# Es una forma de comparar si es un subconjunto o no es un subconjunto
# Así que, estas son dos formas validas de verificar si es un subconjunto
# resultado = conjunto2.issubset(conjunto1)
# resultado = conjunto2 <= conjunto1 
# Y después, tenemos la forma de verificar si es un superconjunto
# En este caso, se utliziza el método "issuperset"
# resultado = conjunto2.issuperset(conjunto1)
# Y ahora, se tiene verificarlo al revés (>=)
# resultado = conjunto2 >= conjunto1 
# Acá verificamos si es un superconjunto
# Hay que recordar que esto depende de las perspectivas
# Es lo mismo, acá simplemente lo invertimos
# Si tomamos a este
#     |
#     v
# conjunto2 >= conjunto1 
# La cabecita apunto para acá: <
# Si tomamos a este
#                | 
#                v
# conjunto2 <= conjunto1  
# La cabecita apunto para acá: >
# Entonces, tenemos que verificar la perspectivas
# No hay que olvidarse de eso
# La diferencia es que "issuperset" no lo usamos así
# conjunto2 <= conjunto1
# Sino que "issuperset" usamos así: 
# conjunto2 > conjunto1
# Es decir, si queremos verificar que no sea un subconjunto, lo ponemos al revés
# Para verificar que sea un subconjunto, es decir, para verificar que sea exactamente igual a esto: issubset(conjunto1)
# Es esta la función: 
# conjunto2 <= conjunto1
# Y en este caso, justamente, el que funciona es el signito al revés (>)
# Es decir, acá tiene que ser menor o igual que (<=)
# conjunto2 >= conjunto1
# Y acá tiene que ser mayor que
# conjunto2 > conjunto1 
# Es decir, todo lo contrario
# Si acá actualizamos y le pedimos que nos muestre el resultado, que nos va a mostrar 
# esto:
# resultado = conjunto2 > conjunto1
# No todos lo demás
# Solamente nos va a mostrar ese, siempre nos muestra el último que ponemos
# print(resultado)
# "False"
# Acá nos va a decir que es falso ("False") 
# resultado = conjunto2.issuperset(conjunto1)
# resultado = conjunto2 > conjunto1
# Porque conjunto 2 no es un superconjunto de conjunto 1
# Conjunto 1 es un superconjunto de conjunto 2
# resultado = conjunto1.issuperset(conjunto2)
# resultado = conjunto1 > conjunto2
# Entonces, ahí funciona, justamente esto que está acá 
# resultado = conjunto2.issuperset(conjunto1)
# resultado = conjunto2 > conjunto1
# es literalmente todo lo contrario a esto que está acá 
# resultado = conjunto2.issubset(conjunto1)
# resultado = conjunto2 <= conjunto1
# Es verificar lo contrario
# "issuperset" equivale a esto:
# conjunto1 > conjunto2 
# Es una interesante forma de verlo
# Bueno, ¿y si queremos verificar solamente si hay un numero en común?
# Lo verificamos de esta forma:
# verificar si hay algún número en comun 
# Para esto, usamos "isdisjoint"
# resultado = conjunto2.isdisjoint(conjunto1)
# Entonces, de esta forma decimos "¿hay algún resultado en común?"
# Actualizamos...
# print(resultado)
# "False"
# Y acá nos va a decir falso ("False")
# ¿Por qué?
# No es distinto, porque con que haya un resultado en común ya es igual
# Acá vamos a poner: 
# conjunto2 = {2,4,6,8}
# Hay que fijarse que no hay ningún elemento en común
# Ahora lo ejecutamos...
# print(resultado)
# "True" 
# Y me devuelve "True", porque son distintos
# resultado = conjunto2.isdisjoint(conjunto1)
#               |
#               v
#            Esto va a ser "True" solo
#            solo cuando los conjuntos que
#            se están comparando no tienen 
#            ningún número igual

# Si solamente hay un número, solo un número que sea igual, en este caso, es el "7"
# conjunto1 = {1,3,5,7}
# conjunto2 = {2,4,7,8}
# Actualizo...
# print(resultado)
# "False"
# Y me va a dar "False", porque ya hay un elemento que coincida 
# Cuando solo un elemento coincide, ya deja de ser igual
# Es decir, ya deja de ser completamente distinto
# resultado = conjunto2.isdisjoint(conjunto1)
#             |
#             v
# Y esto deja de ser "True"
# Así que, ahí acabamos de hacer una comparación y acabamos de ver efectivamente si esto funciona o no funciona
# Así que, vamos al apartado ahora de "diccionarios", que también tenemos bastante que aprender... 