# EJERCICIO 2

# a) Pedirle al usuario que diga cualquier texto real y:

# - calcular cuanto tardaría en decir esa frase

# - ¿Cuantas palabras dijo?

# b) si se tarda más de 1 minuto:

# - decirle:"para flaco tampoco te pedí un testamento".

# c) Matias habla un 30% más rápido:
#    ¿Cuanto tardaría él en decirlo?
         
#       1 segundo         ¿Cuantos segundos?
#          |                  |
# -----------------------------------------------
#          |                  |
#       2 palabras          x palabras

# El segundo ejercicio consiste en lo siguiente:
# Suponiendo que cada persona en promedio habla dos palabras por segundo, 
# a) Pedirle al usuario que diga cualquier texto real y calcular cuánto tardaría en decir esa frase y cuántas palabras fueron las que dijo
# b) Si se tarda más de un minuto, decirle: "Pará, flaco, tampoco te pido un testamento"
# y c) Cuánto tardaría Matias en decirlo, teniendo en cuenta que habla un 30% más rápido.

# Bueno, en estos ejercicios evidentemente estoy bastante presente, es decir, hablo de mí en tercera persona.
# Bueno, básicamente es porque se me ocurrió esa idea, ¿no?
# Aprovechando que yo hablo más rápido que los demás, podemos usar esta variable para jugar un poquito en el trayecto.
# Bien, vamos a hacer el segundo ejercicio
# Este es el último ejercicio de la primera parte

#le pedimos al usuario que nos diga una frase (o varias)
frase = input("Decime una frase y te calculo cuanto tardarias si tuvieras que decirla: ")

#creamos una lista con todos las palabras de la frase (se separan cada vez que haya un espacio en blanco)
palabras_separadas = frase.split(" ")

# usamos len() para ver la cantidad de elementos que hay en la lista
cantidad_de_palabras = len(palabras_separadas) 

#en caso de que tarde más de un minuto en decirlo, le decimos que pare un poco
if cantidad_de_palabras > 120:
    print("Pará flaco tampoco te pedí un testamento")
    
#Calculamos cuanto tardaria en decir las palabras y se lo decimos 
print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')
print(f'Matias lo diria en {cantidad_de_palabras * 100 // 2*1.3 / 100} segundos')

# Primero, frase
# La frase va a ser igual (=) al "input("Decime una frase y te calculo cuanto tardarias si tuvieras que decirla: ")"
# Actualizamos y esto viene funcionando
# Abajo lo que vamos a hacer es usar la función "splits", que nos permitía separar las palabras
# Entonces, ahora vamos a poner
# cantidad_de_palabras va a ser igual (=) a "frase.split(" ")", ¿por qué? porque lo único que separa una palabra de otra palabra, es el espacio " ".
# Entonces, si dejamos un espacio acá: "Decime una", un espacio acá: "una frase" un espacio acá: "frase y" y vamos a calcular la cantidad de palabras que hay, ¿por qué? mirá: una palabra: "Decime", dos palabras: "Decime una", espacio " ", tres palabras: "Decime una frase", espacio " ", y así podemos entender la cantidad de palabras que tiene una frase. 
# Entonces, lo calculamos y acá ponemos que la cantidad de palabras es igual (=) a la "frase.split"
# Acá vamos a poner palabras totales, 
# palabras_separadas = frase.split(" ")
# Y abajo vamos a poner
# cantidad_de_palabras va a ser igual (=) a "len(palabras_separadas)"
# Y lo único que tenemos que hacer ahora es calcular cuánto tardó
# Y para eso, podemos hacer lo siguiente:
# print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')
# Entonces, actualizamos y aquí nos va a decir, nos va a pedir, a ver... 
# Decime una frase y te calculo cuanto tardarias si tuvieras que decirla: hola maestro como andas, que te contas de la vida rey
# okey, tenemos que actualizarlo, bien, no lo actualizamos. Ahora sí, bien, lo mismo
# Decime una frase y te calculo cuanto tardarias si tuvieras que decirla: hola maestro como andas que te contas de la vida mi rey
# Actualizamos y me dice
# Dijiste doce (12) palabras, y te tardarias seis (6.0) segundos en decirlo.
# Bastante bien
# La pregunta es, ¿cuánto me tardaría yo en decirlo?
# Bueno, vamos a ver
# print(f'Matias lo diria en {cantidad_de_palabras/2*1.3} segundos en decirlo')
# 1.3 es el 30%
# Y si actualizamos, ahí tenemos
# Decime una frase y te calculo cuanto tardarias si tuvieras que decirla: que haces maestro que contas
# Dijiste cinco (5) palabras, y te tardarias dos punto cinco (2.5) segundos en decirlo. 
# Matias lo diria en tres punto veinticinco (3.25) segundos en decirlo 
# Bien, Matias lo diría en segundos
# print(f'Matias lo diria en {cantidad_de_palabras/2*1.3} segundos')
# "en decirlo" está de más, se borra
# Matias lo diria en tres punto veinticinco (3.25) segundos
# Muy sencillo y ahí tenemos el programa
# Incluso, acá, si se quiere, se puede hacer lo de antes que es para redondear y generar un entero (int)
# print(f'Matias lo diria en {cantidad_de_palabras * 100 // 2*1.3 / 100} segundos')
# Por (*) cien (100), espacio (" "), división doble (//) por dos (2) y después lo multiplicamos (*) por uno punto tres (1.3) y después lo dividimos (/) por cien (100) devuelta 
# Ahora sí, si actualizamos tendríamos el programa bien con dos decimales
# Bien, ahora sí, ahora vamos a poner un "if"
# if cantidad_de_palabras > 120:
# if cantidad_de_palabras es mayor (>) a cientoveinte (120) 
# Vamos a decirle "print"
# print("Pará flaco tampoco te pedí un testamento")
# ¿Por qué? porque cientoveinte (120) palabras es un (1) minuto
# Si el tipo habla durante más de un (> 1) minuto, dijo cientoveinte (120) palabras
# Entonces, tenemos "cantidad_de_palabras", cientoveinte (120)
# Si dice más de cientoviente (> 120) palabras, le decimos esto: "Pará flaco tampoco te pedí un testamento"
# Entonces, ejecutamos el programa y vamos a verificar si funciona
# Bien, vamos a escribir sesenta (60) palabras
# Decime una frase y te calculo cuanto tardarias si tuvieras que decirla:  -- (Frase de 60 palabras) --
# Dijiste cientoveintiocho (128) palabras y te tardarias sesenta y cuatro (64) segundos en decirlo
# Matias lo diria en ochenta y tres punto dos (83.2) segundos
# Y abajo me dice: "Pará flaco tampoco te pedí un testamento"
# Quedó el programa, es funcional y vamos a explicar parte por parte cómo funciona
# De hecho, vamos a poner el "if" para que funcione

#le pedimos al usuario que nos diga una frase (o varias)
# frase = input("Decime una frase y te calculo cuanto tardarias si tuvieras que decirla: ")

#creamos una lista con todos las palabras de la frase (se separan cada vez que haya un espacio en blanco)
# palabras_separadas = frase.split(" ")

# usamos len() para ver la cantidad de elementos que hay en la lista
# cantidad_de_palabras = len(palabras_separadas) 

#en caso de que tarde más de un minuto en decirlo, le decimos que pare un poco
# if cantidad_de_palabras > 120:
#     print("Pará flaco tampoco te pedí un testamento")
    
#Calculamos cuanto tardaria en decir las palabras y se lo decimos 
# print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')
# print(f'Matias lo diria en {cantidad_de_palabras * 100 // 2*1.3 / 100} segundos')

# Ahí va, ahora sí tenemos el código completamente comentado, funcional y ya tenemos todo listo para poder decir que resolvimos el ejercicio 2
# Incluso, A y B juntos, o sea, ni siquiera tuvimos que separarlos porque más o menos lo pudimos hacer todo en uno solo
# Y ya tenemos listo el primer apartado de ejercicio de este curso de Python
# Ahora sí, ya podemos ir con la segunda parte del curso de Python, que es una sección básico intermedia, porque ya estamos avanzando un poquito más adelante y lo que vamos a ver ahora es medio básico intermedio.
# Es básico pasando intermedio, así que vamos a verlo... 