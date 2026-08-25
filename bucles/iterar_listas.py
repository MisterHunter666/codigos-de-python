animales = ["gato","perro","loro","cocodrilo"]
numeros = [52,16,14,72]

#recorriendo la lista animales
for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')

#recorriendo la lista numeros y multiplicando cada valor por 10   
for numero in numeros:
    resultado = numero * 10
    print(resultado)


#iterando dos listas del mismo tamaño al mismo tiempo    
for numero,animal in zip(animales,numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")
    

for num in range(5,10):
    print(num)
    

# Un bucle es repetir de una forma controlada la ejecución de un código
# Bueno, para empezar tenemos que entender qué es lo que viene siendo iterar
# Porque los bucles son estas sentencias que nos permiten iterar un elemento
# ¿Todo se puede iterar?
# Bien, no
# No todos los elementos se pueden iterar, sino que solamente los elementos iterables
# Ahora, ¿qué es un elemento iterable?
# Bien, un elemento iterable es un elemento que tiene un iterador que define cómo se va a iterar
# No todos los elementos son iterables
# Pero, básicamente, un elemento puede ser iterable cuando tiene algo que defina cómo se va a iterar
# La primera iteración va a ser de acá "..." hasta acá, la segunda de acá "..." hasta acá, la tercera de acá "..." hasta acá
# Si no tiene nada que me diga cómo se va a iterar, es decir, cómo vamos a ir repitiendo el código y de qué forma vamos a ir recorriendo todo el elemento, porque iterar es eso, es recorrer un elemento
# Recorremos un elemento en pedacitos
# Esos pedacitos y la forma en la que se van a ir saltando esos pedacitos los define justamente un iterador
# Entonces, la pregunta es, ¿cuáles son los elementos iterables?
# Bien, por defecto, las listas, porque tienen varios elementos
# O sea, básicamente, una forma de iterar una lista es:
# Primero un elemento, después otro, después otro
# Lo mismo en las tuplas:
# Elemento 1, elemento 2, elemento 3, elemento 4
# Tienen elementos sobre los que iterar
# Es decir, bueno, la tupla completa es un dato
# Y si la tupla tiene cinco elementos, hacemos cinco iteraciones, una para cada elemento
# La tupla completa la podemos romper en cinco partes y vamos a iterar y repetir el código cinco veces, una para cada parte de ese código
# ¿Por qué?
# Porque es sencillo
# Las listas ya vienen definidas para iterarse de esa forma
# Las cadenas de texto también se pueden iterar, ya vamos a ver cómo, los diccionarios, los conjuntos...
# Así que, vamos a arrancar en todo este mundo y vamos a empezar
# Para comenzar tenemos justamente el primer bucle, el primer tipo de bucle que es for,
# Que es el más famoso de todos los bucles, el bucle for
# Y for es un bucle que nos permite iterar, crear una iteración
# Así que, vamos a arrancar a trabajar con for
# Antes de comenzar a iterar listas y usar el bucle for, de hecho, podemos arrancar ya mismo, entendamos bien a fondo el concepto de for
# Mejor dicho, el funcionamiento de for
# En Python, los bucles son: for, in
# En otros lenguajes, tenemos el for que tiene tres condiciones
# O sea, i=0, mientras que i<".", i++, o i--
# Esa famosa forma de hacer bucles
# Python lo simplifica completamente
# Y Python usa: for, in
# ¿Qué es un for, in?
# Bien
# El "for in" es un bucle que justamente lo que hace es crear una variable que en cada vuelta va a ser igual a ese pedacito de variable que estamos igualando
# Ok, vamos a pensarnos mejor
# Vamos ahora a verlo...
# Ok, supongamos que tenemos una lista "animales"
# Que va a ser igual a (=) "perro", "gato", "loro" y "cocodrilo"
# animales = ["perro","gato","loro","cocodrilo"]
#                |      |      |       |
#                v      v      v       v
#                0      1      2       3
# Una lista con cuatro (4, de 0 a 3) elementos
# Bastante simple hasta ahora
# Ahora, ¿cómo iteramos esta lista con for?
# Simple
# Primero decimos: 
# for animal in animales
# Ponemos los dos puntitos (:)...
# for animal in animales:
# Y ahora podemos ejecutar el código
# La pregunta es, ¿a qué va a ser igual "animal"?
# ¿Qué valor tiene "animal"?
# Fácil
# La primera vez que se ejecuta el código, "animal" va a ser igual (=) al primer elemento (0), es decir, "perro"
# De hecho, si usamos un "print(animal)" para mostrar qué es lo que tiene la variable "animal" adentro,
# nos va a decir "perro"
# perro
# Cuando termina de dar la vuelta al bloque, va a revisar si hay más elementos en esta lista
# Si hay más elementos, entonces se vuelve a ejecutar
# Pero ahora, "animal" es igual (=) al siguiente elemento,
# o sea, a "gato"
# O sea que en esta vuelta nos va a mostrar "gato"
# perro
# gato
# Termina de ejecutarse, vuelve a preguntarle si hay elementos
# y está el "loro"
# Entonces, en la siguiente vuelta, "animal" es igual a (=) "loro"
# perro
# gato
# loro
# Nuevamente, termina la ejecución y pregunta si hay otro animal
# Y sí, está el "cocodrilo"
# Entonces, ejecuta de vuelta y ahora "animal" es igual a (=) cocodrilo
# perro
# gato
# loro
# cocodrilo
# Ahora vuelve a preguntar y ya no hay más animales
# Entonces, el bucle termina de ejecutarse
# perro
# gato
# loro
# cocodrilo
# Y ahora sí, pasamos a la siguiente instrucción
# Entonces en definitiva, el programa funcionaría de la siguiente forma:
# Creamos la lista...
# animales = ["perro","gato","loro","cocodrilo"]
# Después, ejecuta el bucle tantas veces como animales tenga...
# for animal in animales:
# print(animal)
# perro
# gato
# loro
# cocodrilo
# Y cuando no tenga más, el programa continúa con su flujo natural
# Es bastante fácil
# Vamos a llevarlo ahora a la práctica, iterando una lista
# Que por eso creamos ese elemento para iterar listas
# Vamos a iterar de todo un poco
# Vamos a iterar cadenas de texto, vamos a iterar diccionarios... 
# Vamos a arrancar iterando listas
# Vamos a arrancar a escribir el código
# Para empezar es sencillo
# Vamos a crear una lista que se llama:
# lista = animales
# que era como lo teníamos
# Y vamos a crear un "gato", un "perro", un "loro" y un "cocodrilo"
# animales = ["perro","gato","loro","cocodrilo"]
# Bien
# ¿Cómo hacemos para recorrer esta lista?
# Bien, ponemos:
# for animal in animales:
#     print(animal)
# Cuando ejecutamos "print(animal)", muestra:
# gato
# perro
# loro
# cocodrilo
# Bien, de hecho podemos decir en el print esto:
# print(f'Ahora la variable animal es igual a: {animal}')
# Si ejecutamos, dice:
# Ahora la variable animal es igual a: gato
# Ahora la variable animal es igual a: perro
# Ahora la variable animal es igual a: loro
# Ahora la variable animal es igual a: cocodrilo
# Es facil, porque "animal" se va a ejecutar tantas veces como variables haya
# Si ahora le agregamos una nueva variable, por ejemplo, "pez"...
# animales = ["perro","gato","loro","cocodrilo","pez"]
# Ejecutamos...
# Ahora la variable animal es igual a: gato
# Ahora la variable animal es igual a: perro
# Ahora la variable animal es igual a: loro
# Ahora la variable animal es igual a: cocodrilo
# Ahora la variable animal es igual a: pez
# Abajo se va a agregar "pez"
# Y si "pez" lo ponemos al principio... 
# Vamos a ponerlo adelante de "gato" y ponemos una coma (",")
# animales = ["pez","gato","perro","loro","cocodrilo"]
# Ejecutamos
# Ahora la variable animal es igual a: pez
# Ahora la variable animal es igual a: gato
# Ahora la variable animal es igual a: perro
# Ahora la variable animal es igual a: loro
# Ahora la variable animal es igual a: cocodrilo
# Ahí está, se va a ejecutar primero "pez"
# Así es cómo funciona el bucle for, es fácil
# "animal" es una variable que se va a crear solamente para ser utilizada acá adentro
#                                |
#                                v
# print(f'Ahora la variable animal es igual a: {animal}')
# Es decir, adentro de este bloque de código, 
# Por eso está bueno, porque de esta forma podemos recorrerlo
# Es decir, si nosotros, por ejemplo, queremos ir haciendo cosas como...
# Vamos a crear otra lista que sea "numeros" es igual a (=), es decir, vamos a crear una lista de números
# animal = [10,62,12,72]
# Y si queremos, por ejemplo, mostrar todos los números y a esos números multiplicarlos por (*) dos (2), por ejemplo
# Bueno...
# for animal in animales:
#     resultado = animal* 2
# En este caso, vamos a cambiar el arreglo que vamos a poner
# Es más, vamos a hacer una cosa, vamos a dejarlo así:
# print(f'Ahora la variable animal es igual a: {animal}')
# Así como estaba
# Y vamos a poner: 
# recorriendo la lista animales
# for animal in animales:
#    print(f'Ahora la variable animal es igual a: {animal}')
# Y ahora vamos a venir acá abajo y poner...
# for numero in numeros:
# Y acá decimos...
# Vamos a agregar estos numeros que habiamos agregado antes
# Vamos a agregar cualquier otro numero ahora
# numeros = [52,16,14,72]
# Y acá lo que voy a hacer va a ser:
# resultado = numero * 10
# por ejemplo, lo multiplicamos por (*) diez (10)
# Y ahora vamos a decir:
# print(resultado)
# Entonces si actualizamos este bucle, nos va a dar:
# 520
# 160
# 140
# 720
# Que efectivamente son estos valores (52,16,14,72) multiplicados por (*) diez (10)
# 52 * 10 = 520
# 16 * 10 = 160
# 14 * 10 = 140
# 72 * 10 = 720
# Y de esta forma podemos hacer muchas cosas, porque supongamos que, por ejemplo, tenemos que una lista con ítems, tenemos ítems con objetos
# Tenemos un objeto y tenemos que mostrar "cuáles son todos los productos que tenés disponibles"
# Y tengo disponible papa, tengo disponible huevo...
# Entonces todos los productos disponibles los agregamos a una lista 
# Y ahí los mostramos
# Tenemos papa, tenemos huevo...
# Y así, es fácil, es realmente interesante la forma en la que podemos trabajar con elementos de esta forma
# Más adelante vamos a ver muchas formas igual de trabajar, pero esto es una forma interesante de recorrer listas
# En realidad es la forma de recorrer listas, no es una forma interesante
# Es la forma de hacerlo
# for numero in numeros:
#     resultado = numero * 10
#     print(resultado)
# Esto le vamos a agregar un comentario que sea:
# recorriendo la lista numeros y multiplicando cada valor por 10
# for numero in numeros:
#     resultado = numero * 10
#     print(resultado)
# Y ahí más o menos nos quedó este dato que está acá
# Bien, hasta acá está todo bien
# Ahora, la pregunta es, ¿cómo haríamos si quisiéramos iterar sobre dos (2) listas?
# ¿Cómo hacemos para hacer dos (2) iteraciones al mismo tiempo?
# Bueno, la forma es simple
# Si queremos iterar dos (2) listas, podemos poner un for adentro de otro for, que son for anidados
# O dos for juntos
# Pero la forma es utilizando una función particular que es "zip()"
# Vamos a hacer...
# Si quisiéramos iterar ambas listas juntas, ¿cómo haríamos?
# Bueno, primero las listas tienen que tener la misma cantidad de elementos
# En este caso, por ejemplo, tenemos "pez", "gato", "perro", "loro", "cocodrilo"
# Son cinco (5) elementos
# Vamos ahora al elemento "pez"
# animales = ["gato","perro","loro","cocodrilo"]
# Así nos queda la misma cantidad de elementos arriba y abajo
# Y ponemos:
# for numero,animal in zip()
#                         |
#                         v
# Y acá ponemos lista uno (1) y lista dos (2)
# En este caso sería "animales" y "numeros"
# for numero,animal in zip(animales,numeros)
# Acá ponemos dos puntos (:)
# for numero,animal in zip(animales,numeros):
# Y abajo, si nos fijamos, podemos poner: 
# print(f"recorriendo lista 1: {numero}")
#       ^                       |
#       |                       |
#    Acá ponemos la f           |
#                               v
#                       Y acá le agregamos el animal, en este caso es "numero"
# Y abajo ponemos "animal" y lista dos (2)
# print(f"recorriendo lista 2: {animal}")
# Si ejecutamos esto, acá si nos fijamos...
# Ahora la variable animal es igual a: gato
# Ahora la variable animal es igual a: perro
# Ahora la variable animal es igual a: loro
# Ahora la variable animal es igual a: cocodrilo
# 520
# 160
# 140
# 720
# recorriendo lista 1: gato 
# recorriendo lista 2: 52
# recorriendo lista 1: perro
# recorriendo lista 2: 16
# recorriendo lista 1: loro
# recorriendo lista 2: 14
# recorriendo lista 1: cocodrilo
# recorriendo lista 2: 72
# De esta forma interesante con la función zip(), podemos recorrer dos (2) listas al mismo tiempo
# Es muy interesante esto
# Lo de arriba vamos borrarlo rápidamente, o sea esto:
# recorriendo la lista animales
# for animal in animales:
#     print(f'Ahora la variable animal es igual a: {animal}')

# recorriendo la lista numeros y multiplicando cada valor por 10   
# for numero in numeros:
#     resultado = numero * 10
#     print(resultado)
# Actualizamos...
# Y si nos fijamos, solamente vamos a mostrar este código:
# for numero,animal in zip(animales,numeros):
#     print(f"recorriendo lista 1: {numero}")
#     print(f"recorriendo lista 2: {animal}")
# Básicamente, es un bucle en el que podemos acceder al valor de la vuelta del primer elemento en ambos casos
# Después la segunda vuelta va a ser igual al (=) segundo valor en ambos casos
# La tercera vuelta va a ser igual al (=) valor...
# Y esto la verdad que es excelente
# La verdad que es muy utilizado y es muy recomendable usarlo cuando queramos iterar dos (2) elementos de la misma lista 
# Podemos iterar dos (2) y tres (3)
# Acá también si tenemos otra lista, también con cuatro (4) elementos podemos poner alguna simplificación de la lista tres (3)...
# for numero,animal,lista3 in zip(animales,numeros,listacompleta):
# Y acá poner la lista tres (3), completa
# Y también funciona con más de dos (+2) listas
# Es interesante esto
# iterando dos (2) listas del mismo tamaño al mismo tiempo
# Entonces, iteramos dos (2) listas al mismo tiempo
# Es interesante esta función
# Lo único es que esto se itera al mismo tiempo
# Es decir, no es "primero todo uno, después todo otro"
# Es "uno, otro, uno, otro", "uno, otro, uno, otro", "lista uno, lista dos", "lista uno, lista dos"
# Es decir, "elemento uno, lista uno", "elemento uno, lista dos", "elemento dos, lista uno", "elemento dos, lista dos", "elemento tres, lista uno", "elemento tres, lista dos", "elemento cuatro, lista uno", "elemento cuatro, lista dos", y así...
# Bueno, después también lo que podemos hacer para iterar es iterar utilizando la función range()
# Es decir, si hacemos esto por ejemplo y usamos range():
# for num in range(5,10)
#  ^
#  |
#  |
# Acá podemos poner cualquier cosa, pero lo interesante siempre es poner nombres que coincidan con lo que estamos haciendo
# for num in range(5,10)
#                   ^
#                   |
# Acá si ponemos del cinco al diez (5,10), esto básicamente va a ejecutar números del cinco (5) al diez (10)
# Entonces si ponemos dos puntos (:)
# for num in range(5,10):
# Y digo:
# print(num)
# Lo que va a mostrar esto, básicamente, es lo que vamos a ver abajo de todas las demás...
# 5
# 6
# 7
# 8
# 9
# Si a range() le definimos dos (2) parámetros, el primer parámetro es en donde arranca
# Y el segundo en donde termina
# Por ejemplo:
# for num in range(10,20):
#                    ^
#                    |
# Acá pusimos veinte (20)
# Entonces, arranca en diez (10), termina en veinte (20)
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# ... hasta deicinueve (19)
# El veinte (20) nunca cuenta, es: 
# El primero está incluido y el último no
# Son diez (10) números
# O sea, vamos desde el diez (10) hasta el veinte (20)
# El veinte (20) no lo contamos, el diez (10) sí
# Y si no ponemos dos parámetros y solamente ponemos uno
# for num in range(20):
# Arranca de cero (0) hasta el número que le digamos
# Actualizamos...
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# Si le decimos que queremos hasta el cinco (5)...
# for num in range(5):
# Actualizamos...
# 0
# 1
# 2
# 3
# 4
# Va de cero (0) a cinco (5)
# Si no le pasamos ningún número adelante y solamente le pasamos un (1) número en vez de dos (2), el único parámetro significa "de cero (0) a el que le digamos"