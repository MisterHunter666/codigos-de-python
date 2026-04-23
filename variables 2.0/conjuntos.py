#creando un conjunto con set()
conjunto = set(["Dato 1"])

#Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato 1", "dato 2"])
conjunto2 = {conjunto1,"dato 3"}
print(conjunto2)

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