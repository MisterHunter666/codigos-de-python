animales = ["pez","gato","perro","loro","cocodrilo"]

for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')

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
# Y queremos, por ejemplo, mostrar todos los números
# 