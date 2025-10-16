#pedirle un numero al usuario
numero = input("dame un numero, capitan: ")

#convierto el número a entero y lo multiplico por 2
#resultado_entero = int(numero) * 2

#convierto el número a flotante y lo multiplico por 2
resultado_flotante = float(numero) * 2

#mostrando el resultado
print(resultado_flotante)

# pedirle un numero al usuario
# numero = input("dame un numero, capitan: ")
# si de repente se dice:
# multiplicando el numero por 2
# resultado = numero*2
# Entonces, ahora vengo abajo y lo muestro...
# mostrando el resultado
# print(resultado)
# Esto es un programa super intuitivo, super perfecto y le damos F5...
# dame un numero, capitan: 6
# 66
# ¿Por qué?
# Porque dos veces 6 es 66
# Acá tenemos un ejemplo que lo explica mejor:
# "6" * 2 = "66"
# 6 * 2 = 12
# "6": esto es un texto
# Cuando agarramos texto y lo sumamos, simplemente se suman los caracteres. Se agarran y se suman.
# Acá tenemos un caracter: "6". Si lo multiplicamos (*) por dos (2), tenemos dos veces el caracter.
# Entonces, tenemos este resultado
# Ahora cuando un número (6) lo multiplicamos por dos (2), tenemos otra cosa
# "a" * 2: acá es como si multiplicáramos a dos veces (aa)
# Le estamos diciendo que haya dos veces este carácter (a)
# Se unen ya se tiene dos veces el carácter
# Ahora los números funcionan de forma diferente
# Cuando le decimos que los multiplique dos veces, no da 66, nos da 12.
# ¿Por qué? porque esto es un cálculo aritmético: 6 * 2
# Estamos trabajando aritméticamente con este dato: 6
# No de forma concatenándolos
# Esa es la diferencia
# Entonces tenemos una información que es: "me estás pasando un dato que es un texto"
# Entonces lo que tengo es un texto
# resultado = numero*2
# Estoy diciéndole que esto se multiplique (*) por dos (2)
# Y me da "66" porque estoy multiplicando el texto seis (6) por (*) dos (2)
# ¿Qué hay que hacer?
# Convertirlo al número
# ¿Cómo se convierte al número?
# Con la función int, como ya vimos antes.
# resultado = int(numero) * 2
# Cuando actualizo, ahora me dice: "dame un numero, capitan: "
# Le paso el 6
# dame un numero, capitan: 6
# 12
# Me devuelve "12"
# ¿Por qué? porque lo convertí al número.
# y este dato es un tipo int
# Lo convertí a entero
# Entonces ahora digo:
# convierto el número a entero y lo multiplico por dos (2)
# Esto es lo que hacemos

# Es más, también podemos copiarlo pero con otro tipo de dato

# convierto el número a flotante y lo multiplico por 2
# resultado = float(numero) * 2
# pongo float, que es la otra función
# Con una función, convertimos a int con otra float
# Y float es un número con coma (.)
# Le voy a pasar un número
# Le voy a pasar, por ejemplo, un "4.5"
# dame un numero, capitan: 4.5
# 9.0
# Le paso un "4.5" y me dice "9.0"
# Pero, ¿por qué me muestra el punto cero (.0)?
# Si el resultado fue nueve (9)
# Cuando trabajamos con números flotantes (float), si tenemos "4.5" por (*) dos (2) y nos dan nueve (9), no es nueve (9), es nueve punto cero (9.0), o sea, es un número flotante (float).
# Por más que sea un número entero (integer), si lo convertimos a enteros con el número int.
# O sea, se podría hacer en todo caso esto y meter a la función int del resultado:
# resultado = int(float(numero) * 2)
# Entonces, el resultado de esto, que va a ser esto: "9.0", lo convierte entero (9).
# Si lo actualizamos y le damos "4.5"...
# dame un numero, capitan: 4.5
# 9
# Ahora sí se convierte entero
# Depende de lo que se quiera hacer, puede ser o no puede ser.
# Pero, ¿qué pasa si, por ejemplo, se tuviera el int?
# resultado = int(numero) * 2
# Y al int se le pasara otro dato
# Por ejemplo, se le pasa un número con coma (.)
# Bueno, actualizo y le paso un "4.5"...
# dame un numero, capitan: 4.5
# Lo que pasa es que se le está pasando a int un número flotante (float).
# E int convierte a enteros (integer)
# Entonces, cuando se sabe que se va a trabajar con números con coma (.)
# Si se va a trabajar con números con coma (.), se usa float.
# resultado = float(numero) * 2
# Y ahora sí esto funciona y se puede trabajar con números con coma (.)
# dame un numero, capitan: 16.23
# 32.46
# Por ejemplo, se le pasa "16.23" y lo multiplica por (*) dos (2) y devuelve "32.46", se tiene el resultado con coma (.)
# Y si después se dice: "yo se que el resultado me va a dar flotante (float) porque que son, por ejemplo, "0.5" "
# Después, se puede convertir a entero
# Pero si no y se lo necesita flotante, se lo deja en float
# Y así es cómo se trabaja con datos, con números
# Se pueden hacer hasta sumas (+), de esta forma
# Se agarra un número y se lo suma.
# Pero, ¿cómo se pueden sumar dos números?
# Bueno, primero se convierten los dos números a enteros
# 6 6, dos seis por ejemplo
# y se suman
# 6 + 6 = 12
# input lo que hace es pasar un dato
# Esto se va a utilizar mucho
# Porque "input" es una herramienta que permite pedirle datos al usuario de consola
# Es decir, para trabajar con otro tipo de datos usamos otras funciones
# Pero esta es la principal
# Lo que se hace es pedirle al usuario que dé información
# Y en programación, todo es eso
# Todo es pedir información
# Procesarla
# Y dar una respuesta
# Así es cómo funciona
# Entonces, ahora se está pidiendo esta información:
# numero = input("dame un numero, capitan: ")
# se da la información
# y se procesan respuestas
# En vez de darle al programa la información, como se viene haciendo siempre, ahora se le pide al usuario.
# Y esta justamente es la forma de trabajar con números en Python después de utilizar la función input().
# De hecho, vamos a poner "resultado_entero"
# resultado_entero = int(numero) * 2
# Y también, vamos a poner "resultado_flotante"
# resultado_flotante = float(numero) * 2 
# Ahora sí terminamos con y, por último, vamos a poner "resultado_flotante" porque sino después nos va a tirar un error... 
# print(resultado_flotante)

# Ahora vamos a ir con el apartado de ejercicios prácticos
# El apartado de ejercicios prácticos es un apartado que nos va a permitir crear cosas con lo que venimos aprendiendo
# O sea, todo lo que aprendimos hasta ahora, lo vamos a usar para crear cosas y crear proyectos
# Van a haber tres ejercicios prácticos
# Ejercicios prácticos 1
# Ejercicios prácticos 2
# Y ejercicios prácticos 3
# Estos tres ejercicios prácticos nos van a permitir reforzar todo lo que ya sabíamos y llevarlo a la práctica
# Para ver con qué problemas nos enfrentamos en la vida real cuando creamos cosas con los conocimientos que ya tenemos
# Después de ejercicios prácticos vamos a tener otras dos pruebas que son como unos ejercicios prácticos aparte que ahí vamos a investigar 
# Ahí vamos a aprender cosas nuevas y vamos a desarrollar con lo que ya sabemos y aprendiendo cosas nuevas
# Y después vamos a hacer un proyecto final
# Que es un proyecto para recopilar todo lo que aprendimos y nuevas cosas extra
# Pero para arrancar vamos con los tres ejercicios prácticos
# Que es: ejercicios prácticos 1, 2 y 3
# Ahora vamos con el "ejercicios prácticos 1"
# Que nos van a plantear diferentes problemas que tenemos que resolver
# Así que vamos a ver si lo podemos resolver
# Y cómo hacemos para enfrentarnos a los problemas que se nos van a plantear...  