# ¿Qué es el desempaquetado de variables?
# Es una forma, una técnica que tenemos en Python, que tiene tantos lenguajes de pronunciación también, para básicamente asignarle valores a variables de una forma bastante particular
# ¿Cómo es eso?
# Vamos a crear por ejemplo una tupla
datos = ("Matias","F",1000000)
# "datos" va a ser igual (=) a una tupla que va a ser "Matias" 
# ¿Qué es el desempaquetamiento?
# Es una forma en la que podemos crear variables nuevas tomando los datos de, por ejemplo, una tupla
# ¿Cómo hacemos eso?
# Ponemos: nombre,apellido = datos
nombre,apellido,suscriptores = datos
# ¿A qué va a ser igual (=) nombre?
# Va a ser igual (=) al primer valor de la tupla
# datos = ("Matias","F")
#             |
#             v
#           nombre
# ¿A qué va ser igual (=) apellido?
# Va a ser igual (=) al segundo valor de la tupla
# Si incluso se le pusiese un millón (1000000):
# datos = ("Matias","F",1000000)
# Y en la parte del desempaquetado, se podría poner por ejemplo también: "suscriptores"
# nombre,apellido,suscriptores = datos
# Entonces, esto también funcionaría
# ¿Qué pasa si por ejemplo se le dice "print(nombre)"?
print(nombre)
# Me va a mostrar "Matias" 
# Si se le dice: "print(apellido)" 
print(apellido)
# Me va a mostrar "F"
# Y si se le dice: "print(suscriptores)"
print(suscriptores)
# Me va a mostrar "1000000"
# ¿Por qué? Porque esta es la forma en la que desencapsulamos variables 
# Tenemos que hacer de cuenta que cada valor que ponemos va a estar colocado en cada uno de los elementos de la tupla
# Entonces, es importante que entendamos que el desempaquetado funciona solamente si la cantidad de variables que ponemos es igual (=) a la cantidad de datos que tiene el array
# Si el array tiene tres (3) datos, creamos tres (3) variables
# Si el array tiene dos (2) datos, creamos dos (2) variables
# En este caso, así es como puede funcionar el desempaquetado
# mostrando resultados
# print(suscriptores)
# desempaquetado
# nombre,apellido,suscriptores = datos
# creando una tupla
# datos = ("Matias","F",1000000)
# Esto funciona con tuplas, con listas y demás
# Si por ejemplo se intenta crear una lista...
# creando los datos
# datos_en_tupla = ("Matias","F",1000000)
# datos_en_lista = ["Matias","F",1000000]
# creando el desempaquetado
# nombre,apellido,suscriptores = datos_en_tupla
# O sino se puede poner "datos_en_lista"...
# nombre,apellido,suscriptores = datos_en_lista
# Esto funciona porque el desempaquetamiento se puede dar tanto como para "lista" como para "tupla" y también como para conjuntos
# No me permite desempaquetar números, eso es un dato muy interesante
# Bien, acá tenemos estos datos ya creados y tenemos esto justamente que es el desempaquetamiento
# Acabamos de aprender a "desempaquetar"
# ¿Para qué nos sirve esto?
# Nos sirve para bastante y lo vamos a ver más adelante cuando veamos por ejemplo funciones
