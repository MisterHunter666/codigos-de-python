# Los metodos de cadena son funciones que se utilizan justamente aplicadas a lo que viene siendo un objeto.
# En Python, la mayoría de cosas se pueden considerar objetos.
# Por ejemplo, una variable, un texto, es un objeto.
# Una lista es un objeto.
# Entonces, cuando se habla de metodos, los metodos son funciones aplicadas a objetos.
# Una función es, por ejemplo, print().
# Las funciones tienen esta estructura: nombre de la función, le siguen los parentesis () y adentro a veces se le puede dar parametros, es como lo que va a recibir la función para convertir o hacer cosas con él.
# nombre_de_funcion(okoakdadk)
# Entonces, en este caso se tiene la función print(), que lo que hacer es mostrar en pantalla lo que se está pasando entre parentesis.
# Por ejemplo, print(Resultados)
# Después, está la funcion type(), que lo que hace justamente es devolver el valor que se le da. Por ejemplo, si se le da un 5 "type(5)", verifica qué tipo de numero es y lo devuelve. Si se le da un 15, dice qué número es. Cuando el valor es un número con coma (15.5), devuelve float. Cuando el valor es caracteres entre comillas ("string"), devuelve un string. Y cuando el valor es una mezcla entre caracteres y numeros, también devuelve un string.
# Entonces, type() lo que hace es verificar el dato que se le da y dice qué es lo que hace.
# Las funciones tienen esa finalidad: analizan pedazos de código que se les da para que devuelvan o que hagan cosas con ellos. 
# Entonces, las cadenas de texto tienen sus propios metodos, sus propias funciones. 
# Vamos a ver cuáles son las funciones que Python nos da por defecto para hacer con las cadenas, qué cosas podemos hacer con un texto, por ejemplo.

# Vamos a jugar un poco con lo que son las cadenas.

cadena1 = "Hola soy Matias" 
# cadena1 va a tener un texto

cadena2 = "Bienvenido maquinola"
# cadena2 va a tener otro texto

# Voy a jugar con estos dos textos.

# Para empezar, lo que vamos a hacer va a ser ver los diferentes metodos que hay.

# función
#  |
#  v
# DIR - devuelve la lista de atributos válidos del objeto pasado. Es uno que permite devolver todos los atributos de un objeto. Por ejemplo:
dir(cadena1)
# Al correrlo, no se devuelve nada porque dir() ejecuta algo y es un valor que deja suelto. Si se quiere mostrar en pantalla eso que se está haciendo, se tiene que envolverlo en un print(), ¿cómo se hace? Así: 
print (dir(cadena1))
# Lo que devuelve justamente son todas las cosas que se pueden hacer con esto. Se le puede dar: dir, endswith, encode, isdigit, lower, join, se le pueden remover prefijos. O sea, hay un monton de cosas que se pueden hacer con este objeto que se le pasa. Si, por ejemplo, se le pone un numero, pongo 4 o cualquier numero:
print (dir(4))
# Me da otro tipo de cosas. Son parecidas, pero son otro tipo de cosas, porque son datos diferentes. Con un numero, se puede hacer que se comporte de una forma, se puede operarlo de una forma diferente a los textos. De hecho, si, por ejemplo, se da y se crea una lista, a dir le paso una lista con cualquier cosa y actulizo:
print (dir(["soadasoi"]))
# Ahora, nos da otra cosa. Porque las listas tienen otros metodos propios, lo que se van a ver ahora, justamente, son los metodos y las propiedades, las cosas que podemos hacer con un texto. En este caso, cadena1. Así que, vamos a verificar y ver. Vamos a ir probando distintos metodos.
resultado = cadena1.lower()
# resultado va a ser igual a todo lo que hagamos.


#convierte a mayusculas
#mayusc = cadena1.upper()

#convierte a minusculas
#minusc = cadena1.lower()

#buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1.
busqueda_find = cadena1.find("M")

#buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepción
busqueda_index = cadena1.index("M")
#Queremos ver si en esta cadena de texto encontramos la cadena "Hola".
print (busqueda_index)
# Va a devolver 0.
# Porque devuelve la posición en la que encuentra lo que se le pida.

# dir dato, no dato.dir()
# dir(dato)

#si es numerico, devolvemos true, sino devolvemos false
es_numerico = cadena1.isnumeric()
#devuelve false
#si es alfanumérico, devolvemos true, sino devolvemos false
es_alfanumerico = cadena1.isalpha()

#primera letra en mayuscula
#primer_letra_mayusc = cadena1.capitalize()
# print (primer_letra_mayusc)
# Al ejecutar este print, lo que muestra es "Hola soy matias".
# No solamente convierte la primera letra a mayuscula, sino lo que hace es primero hace como si fuera un lower(), convierte todo a minuscula, y después toma la primer letra y la convierte en mayuscula.
# Porque Matias estaba con mayuscula y usando el metodo capitalize() la dejó en minuscula (matias).
# Entonces, lo que hace es primero convierte todo en minuscula y después la primera letra la deja en mayuscula.
# Así es como funciona esta cadena.

print (es_alfanumerico)
#Acá se muestra el resultado.
# Si se ejecuta, se tiene lo mismo que dir(cadena1). Así que, lo que sucede en dir(cadena1), se va a almacenar en resultado.

# UPPER - convierte a mayuscula. Lo que hace es convertir todas mayusculas. Si se pone resultado = upper(cadena1), lo que hace esta cadena es convertir el dato a una mayuscula. Tira un error porque normalmente se suele trabajar de otra forma con los metodos. Los metodos en Python son "seguidos de", es decir, dir, por ejemplo, no era un metodo, era una función, es una función de python. Para que sea considerado un metodo, tiene que ser ejecutado de la siguiente forma y es:
# resultado = cadena1.upper()
# Ahora sí lo que hacemos es ejecutar un metodo de esta cadena. Entonces, si se ejecuta, va a devolver "HOLA SOY MATIAS", lo que hizo fue tomar este texto "Hola soy Matias" y convertirlo a mayuscula. De hecho, lo que se podría hacer directamente es esto: resultado = "Hola noas3o23i4SQODJK ".upper()
# Todo esto lo que va a hacer es, si se le dice que lo pase es lo mismo, pero lo pasó a mayuscula:
# HOLA NOAS3O23I4SQODJK
# Así es como funcionan los metodos.
# Los metodos son: el "dato" "." el "nombre_del_metodo" y los "(parentesis)".
# Esta es la estructura de la forma en la que funciona:
# resultado = DATO.METODO(OSAODKO)
# En caso de poner algún parametro, se tendrá que ponerlo. Vamos a ver cuándo usar parametros y cuándo no, pero ahí acabamos de hacer una función de esta forma:
# resultado = cadena1.upper()
# Estamos lo que tiene adentro de "cadena1" convirtiéndolo a mayusculas. Todo se convierte en mayuscula.

# LOWER - convierte a minuscula. Por ejemplo:
# resultado = cadena1.lower()
# Si se ejecuta, me va a convertir todo a minuscula. La H y la M estaba con mayuscula y ahora ya la convirtió a minuscula.
# Porque lower() convierte a minuscula.

# CAPITALIZE - primera en mayuscula. Es otro tipo de texto que es para convertir, no toda mayuscula ni toda minuscula, sino que convierte solamente la primer letra en mayuscula.

# FIND - método encuentra la primera aparición del valor especificado, sino devuelve 1. Lo que hace es buscar un valor que se le pida. Por ejemplo: 
# Buscamos una cadena en otra cadena:
# busqueda_find = cadena1.find("Hola")
# Queremos ver si en esta cadena de texto encontramos la cadena "Hola".
# print (busqueda_find)
# Va a devolver 0.
# Porque devuelve la posición en la que encuentra lo que se le pida.
# Si se busca la letra "a", se encuentra en la posición 3 porque esto es como si fuera un objeto. No deja de ser un objeto, un arreglo o lo que queramos. Entonces, tiene posiciones. Una cadena de texto es un conjunto de caracteres. Esto es el uno(H), dos(o), tres(l), cuatro(a).
# Si la A está en el cuarto lugar, ¿por qué me devuelve el tres?
# Porque en las listas contamos de cero(0) a uno(1).
# En una matriz se cuenta de cero en adelante. No arrancamos a contar desde uno, arrancamos a contar desde cero.
# Entonces, este valor(H) no es uno, es cero. Si la "H" es cero(0), entonces "o" es uno(1). Si "o" es uno(1), entonces "l" es dos(2). Si "l" es dos(2), entonces "a" es tres(3). Entonces, tenemos cero(0, "H"), uno(1, "o"), dos(2, "l"), tres(3, "a").
# Es verdad, la posición en la que se encuentra la letra que le dijimos está en el tres(3, "a"), la tercera posición. Así que, efectivamente, nos funciona de esa forma.
# ¿En dónde encontramos una "s"? ¿en qué posición tenemos una "s"?
# En la posición cinco(5).
# cero(0, "H"), uno(1, "o"), dos(2, "l"), tres(3, "a"), cuatro(4, " "), cinco(5, "s"), efectivamente.
# ¿Y si encontramos una "m"?
# Devueve un -1, no existe.
# No hay forma de que sea -1.
# Lo que sucede es que devuelve -1 cuando no encuentra un valor.
# Porque Python es sensible a mayúsculas y minúsculas. Es justamente key sensitive.
# Entonces, se puso una M mayúscula.
# Si se hubiera puesto una m minúscula, hubiera dicho que estaba en la posición nueve(9).
# cero(0, "H"), uno(1, "o"), dos(2, "l"), tres(3, "a"), cuatro(4, " "), cinco(5, "s"), seis(6, "o"), siete(7, "y"), ocho(8, " "), nueve(9, "m").
# Los espacios también cuentan como números.
# " ": esto también es un espacio, esto sí existe. Existe y es un caracter más. Entonces, cuenta.

# cadena1 = "Hola soy Matias"
#            ||||||||||
#            vvvvvvvvvv
#            0123456789

# Está bien, cumple con la condición.

# Si se le dice la d minúscula, muestra -1.
# Pero entonces, ¿por qué muestra -1?
# Porque -1 es el valor que devuelve cuando no encuentra algo.
# Porque como no existe la posición -1, eso es lo que estaría devolviendo en caso de no encontrar nada.
# Si no encuentra nada, devuelve -1.
# Entonces, se pone: busca una cadena en otra cadena, si no hay coincidencias devuelve -1.

# Después, se tiene otra función que es igual.
# La diferencia es que es index().
 
# INDEX - método encuentra la primera aparición del valor especificado, sino devuelve una excepción.
# Busca una cadena en otra cadena.
# busqueda_index = cadena1.index("D")
# Si se le pasa la D, por ejemplo, la D mayúscula, se va a poner busqueda_index.
# print (busqueda_index)
# Esto va a devolver nueve(9), está bien.
# Funciona exactamente igual.
# Si se pasa la a, va a devolver tres(3), listo, está funcionando igual.
# Evidentemente está bien.
# Pero entonces, ¿para qué está hecha la función find() o index() si funcionan igual?
# Bueno, la diferencia es que en una, si no encuantra nada, devuelve -1 (find), pero en otra, si no encuentra nada, por ejemplo, vamos a ponerle un nueve(9).
# busqueda_index = cadena1.index("9")
# No hay ningún 9, así que debería devolver un error.
# Como por ejemplo acá, en la d minúscula.
# busqueda_index = cadena1.index("d").
# Nos tira un error, nos lanza una excepción.
# Más adelante, vamos a ver esto qué son las excepciones y cómo manejarlas, porque en un futuro tenemos que aprender a manejar las excepciones para que en caso de que nos lance un error en medio del programa, sepamos manejarlas y saber qué hacer con el programa para que no se trabe.
# Porque sino, si hay una excepción el programa se traba ahí y no avanza más. Y eso no puede suceder.
# Entonces tenemos que aprender a manejarlas.
# Bueno, en un futuro lo vamos a aprender a hacer.
# Pero justamente la diferencia entre find() e index() es que index(), en caso de no encontrar una coincidencia, nos tira una excepción. Entonces, vamos a agregarlo.
#buscamos una cadena en otra cadena, si no hay coincidencias, lanza una excepción
# busqueda_index = cadena1.index("M")
# Vamos a darle M y M mayúscula
# busqueda_find = cadena1.find("M")
# busqueda_index = cadena1.index("M")
# Entonces, si actualizamos y corremos el código, nos da nueve(9). Efectivamente, funciona.

# Método y función no son lo mismo porque todos los métodos son funciones, pero no todas las funciones sos métodos justamente.
# Porque los métodos son funciones específicas de objetos.
# Si no es una función de un objeto, no es un método.  
# Ponemos dir dato, no ponemos dato.dir(), entonces no es un método, es una función
# dir(dato)
# Vamos a verlo más adelante bien.
# Cuando trabajemos con programación orientada a objetos, vamos a entenderlo bien. Porque vamos a poder crear objetos.
# Y cuando creamos un objeto a ese objeto, vamos a poder aplicarle funciones propias de ese objeto.
# Por ejemplo, un perro puede ladrar, pero no podemos decir que "ladrar" si no hay un perro. No podemos decir al programa "ladrar". Tiene que ser una función aplicada a un objeto. Entonces, ahí sí le podemos decir "ladrar". 
# Lo vamos a ver más adelante cuando vemos a programación orientada a objetos.
# Pero solo para saber que un método es una función aplicada a un objeto. Nada más.

# upper(), lower(), capitalize(): estos métodos justamente nos convierten el valor.

# find(), index(): estos métodos buscan un valor.

# isnumeric(), isalpha(): estos métodos consultan otra cosa. Es decir, nos devuelven también datos, pero justamente nos consultan si son numéricos o alfanuméricos.

# count(), len(): estos métodos hacen otra cosa que ya vamos a ver...

# endswith(), startswith(): estos métodos hacen otras cosas que vamos a ver junto con replace() y split().

# Así que, vamos a seguir con isnumeric() y isalpha().

# ISNUMERIC - si es numerico, devuelve true. Es una función que nos permite ver que si es numérico, devuelve true.
#si es numerico, devolvemos true, sino devolvemos false
# es_numerico = cadena1.isnumeric()
#devuelve false
# ¿Qué pasa si se le pone números?
# cadena1 = "534534534"
# busqueda_index = cadena1.index("5")
# es_numerico = cadena1.isnumeric()
# Nos devuelve true, ¿por qué? porque es valor numérico.
# Aunque sea un texto, esto: "534534534" es un texto, no es un valor numérico.
# Para que sea un valor numérico, tiene que ser esto: 534534534
# Pero lo que hace isnumeric() es verificar si es un número.
# Porque a ver, sí, está bien. Es un texto que tiene solo números. Bueno, entonces vamos a verificarlo. isnumeric(). Si es numérico, nos va a devolver true.
# Ahora vamos a comprobar si es alfanumérico.

# ISALPHA - si es alfa numérico, devuelve true.
# Si es alfanumérico, devolvemos true, sino devolvemos false
# es_alfanumerico = cadena1.isalpha()
# Solamente son válidos los caracteres desde la A a la Z.
# A, B, C, D, E, F, G, H, hasta la Z.
# Las letras del abecedario.
# El espacio (" ") no es alfanumérico.
# Entonces tenemos que sacarlo.
# Los espacios no son caracteres alfanuméricos, son caracteres especiales.
# Los caracteres especiales son, por ejemplo, el espacio(" "), el slash(\ y /), los puntos(.), las comas(,), etcétera.
# Entonces, solo si es alfanumérico, este método nos va a devolver true.

# COUNT - devuelve el número de ocurrencias de una subcadena en la cadena dada.
# LEN - cuenta los caracteres de una cadena.

# ENDSWITH - verifica si una cadena comienza con
# STARTSWITH - verifica si una cadena termina con

# REPLACE - reemplaza un valor por otro.
# SPLIT - separa por el parametro dado.

# Los metodos pueden retornar tipos de valores diferentes.
# Retornar un valor significa "devolvernos" porque cuando ejecutamos una función, es decir, nosotros ejecutamos una función y lo que ejecutamos, nos retorna algo. Es decir, por ejemplo, "minusc = cadena1.lower()" esta variable se convierte en de repente esto: "minusc = "hola soy matias"".
# Decir esto: "minusc = "hola soy matias"" y decir esto: "minusc = cadena1.lower()" es lo mismo porque esto: "minusc = cadena1.lower()" lo que nos va a retornar es esto: "minusc = "hola soy matias"".
# Entonces, retornar un valor es devolvernos un valor, la función, el total de la función, el total del código, es como que nos devuelve algo. Eso que nos devuelve es el resultado que nos da. Es como el resultado de la ejecución.
# Entonces, en este caso, vamos a dejarlo así: "minusc = cadena1.lower()".