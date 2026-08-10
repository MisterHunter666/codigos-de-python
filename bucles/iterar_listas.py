

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
# Para comenzar tenemos justamente el primer bucle, el primer tipo de bucle que es FOR,
# Que es el más famoso de todos los bucles, el bucle FOR
# Y FOR es un bucle que nos permite iterar, crear una iteración
# Así que, vamos a arrancar a trabajar con FOR
# Antes de comenzar a iterar listas y usar el bucle FOR, de hecho, podemos arrancar ya mismo, entendamos bien a fondo el concepto de FOR
# Mejor dicho, el funcionamiento de FOR
# En Python, los bucles son: FOR, IN
# En otros lenguajes, tenemos el FOR que tiene tres condiciones
# O sea, i=0, mientras que i<".", i++, o i--
# Esa famosa forma de hacer bucles
# Python lo simplifica completamente
# Y Python usa: FOR, IN
# ¿Qué es un FOR, IN?
# Bien
# El "FOR IN" es un bucle que justamente lo que hace es crear una variable que en cada vuelta va a ser igual a ese pedacito de variable que estamos igualando
# Ok, vamos a pensarnos mejor
# Vamos ahora a verlo...