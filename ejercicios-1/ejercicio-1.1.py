# Ejercicio 1

# a) Diferencia en porcentaje entre el curso actual y:

# - el más rapido de otros cursos
# - el más lento de otros cursos
# - el promedio de los cursos

# b) Porcentaje de material inservible que se reduce en:

# - el promedio de los cursos
# - el curso actual (este curso)

# Ver 10 horas de este curso a cuantas de otros cursos equivale?

#Promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
matias_curso = 1.5

#Duración de crudos
crudo_promedio = 5
crudo_matias = 3.5

#Diferencias de duracion

diferencia_con_min = 100 - (matias_curso / otros_cursos_min * 100)
diferencia_con_max = 100 - matias_curso * 1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - matias_curso / otros_cursos_promedio * 100

#Calculando el porcentaje de tiempo vacio removido
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10

#Mostrando las diferencias de duración (ejercicio A)
print(f'El curso de matias dura un: {diferencia_con_min}% menos que el más rápido')
print(f'El curso de matias dura un: {diferencia_con_max}% menos que el más lento')
print(f'El curso de matias dura un: {diferencia_con_promedio}% menos que el promedio')

#Mostrando la cantidad de espacios vacíos que se remueven (ejercicio B)
print(tiempo_vacio_promedio)

# El primer ejercicio consiste en lo siguiente:
# El timing para ver los conceptos vistos en Python en un curso de corrido es de 2.5 horas como mínimo, 7 horas como máximo y 4 horas en promedio.
# Este curso lo logró en una hora y media.
# a) ¿Cuánta diferencia en porcentajes hay entre el curso actual y el más rápido de los otros cursos, el más lento de otros cursos y el promedio de los cursos?
# b) Teniendo en cuenta que la cantidad de crudo en promedio de los demás cursos es de 5 horas y con edición lo convierten en 4 horas, y el crudo de este video fue de 3 horas y media y se redujo a 1 hora y media, ¿qué porcentaje de material inservible, material vacío en definitiva, se reduce del crudo en ambos casos?
# Y por último c)
# c) Ver 10 horas de este curso sería equivalente a ver cuántas horas de otros cursos?
# Y ver 10 horas de otros cursos equivalente a cuántas horas de este curso?
# Bien, este es el primer ejercicio que tenemos que resolver con los datos que tenemos a continuación
# Otro dato que no mencioné, que obviamente no es relevante para este ejercicio, pero que está bueno mencionar, es que este curso también está disponible en inglés
# Está bueno porque si tienen amigos que quieren aprender Python y hablan inglés o hablan otros idiomas, este no solamente es el mejor curso para gente que habla español, sino también para gente que habla en inglés.
# Ahora sí, vamos a comenzar con el primer ejercicio
# Bien, primero lo que tenemos que hacer siempre cuando arrancamos este tipo de programas es anotar los datos, así que vamos a anotar los datos que tenemos en cuenta.
# otros_ cursos_min =
# otros_cursos_max =
# otros_cursos_promedio = 
# Es decir, acá vamos a obtener un número que nos defina cuántas horas dura en cada caso
# Es decir, esta es la cantidad de horas que necesitan para ver esto que ya vimos a continuación
# Entonces, lo mínimo que se necesita en otros cursos es:

#Promedio de duracion
# otros_cursos_min = 2.5
# otros_cursos_max = 7
# otros_cursos_promedio = 4

# El mínimo es 2.5 horas
# El máximo es de 7 horas
# Y el promedio es de 4 horas
# Entonces, vamos a crear una anotación:

#Promedio de duracion
# otros_cursos_min = 2.5
# otros_cursos_max = 7
# otros_cursos_promedio = 4
# matias_curso = 1.5

# En otros cursos para ver todos estos conocimientos tardan 2.5 horas, como mínimo, como máximo 7 y en promedio 4.
# Nosotros logramos en 1.5
# Esos son los datos a través que tenemos de la duración
# Después, tenemos que sacar el promedio de crudos.
# Bien, lo que nos pide el ejercicio es básicamente mostrar la diferencia.
# Para eso vamos a crear un conjunto de variables que nos muestre las diferentes diferencias

#diferencias de duracion
# Acá tenemos que sacar un promedio
# Primero lo que dura el curso de matias, matias_curso, dividido (/) lo que dura justamente los otros cursos, otros_cursos_min, y esto por (*) 100
# diferencia_con_min = matias_curso / otros_cursos_min * 100
# Bien, vamos a ver qué es lo que nos muestra esto
# print(diferencia_con_min)
# Nos muestra "60.0"
# Es decir, el curso de matias dura el 60 por ciento (%) de lo que duran los demás cursos
# Este "60.0" es un dato falso porque no nos representa nada real a menos que se haga así:
# diferencia_con_min = 100 - matias_curso / otros_cursos_min * 100
# ¿Por qué?
# Porque separa en módulos
# Primero se ejecuta 100 por un lado, después se ejecuta todo esto porque esto es como matemática en la vida real
# Primero se ejecutan las divisiones (/) y multiplicaciones (*) en este orden y después se resta (-)
# O sea, no es 100 menos (-) matias_curso y después el resultado de esto dividido (/) a lo otro
# No
# Esto se ejecuta de esta forma, es decir, se ejecuta así:
# diferencia_con_min = 100 - (matias_curso / otros_cursos_min * 100)
# Sin paréntesis funciona igual
# Se ejecuta primero todo esto: "(matias_curso / otros_cursos_min * 100)" y el resultado de todo eso le restamos (-) a cien (100)
# Es matemática básica, es decir, primero básicamente es matias_curso dividido (/) otros_cursos_min
# Eso justamente es lo que nos da al multiplicarlo (*) por cien (100), 60 por ciento (%)
# pero si lo restamos (-) a cien (100), nos va a decir la diferencia y la diferencia es del 40 por ciento (%), "40.0", o sea, esto es la diferencia de duración, es decir, el curso de matias dura cuarenta (40) por ciento (%) menos que el más rápido.
# Entonces, vamos a agregar un f, cerramos el string y vamos a decir "el curso de matias dura un: ", después dice el porcentaje, se agrega la barra de porcentaje (%) y "menos que el más rapido":
# print(f'El curso de matias dura un: {diferencia_con_min}% menos que el más rápido')
# O sea, el curso que más rápido lo explica es esto: "diferencia_con_min"
# Porque si un curso lo que menos tarda en explicar todo lo que explicamos es de dos horas y media (2.5) es porque es el más rápido, si otro tarda siete (7) es porque es más lento, entonces acá decimos que es el más rápido y lo que nos muestra en pantalla es lo siguiente:
# El curso de matias dura un: 40.0% menos que el más rápido
# O sea, logramos explicar un cuarente (40) por ciento (%) más rápido lo que el curso más rápido logró explicar
# Y así, podemos crear otras diferencias, es decir, así como es "diferencia_con_min" puede ser "diferencia_con_max" y "diferencia_con_promedio"
# diferencia_con_min = 100 - matias_curso / otros_cursos_min * 100
# diferencia_con_max = 100 - matias_curso / otros_cursos_max * 100
# diferencia_con_promedio = 100 - matias_curso / otros_cursos_promedio * 100
# Simplemente en uno ponemos "otros_cursos_max" y en otro "otros_cursos_promedio"
# Entonces, actualizamos y ahí nos va a decir
# print(f'El curso de matias dura un: {diferencia_con_min}% menos que el más rápido')
# print(f'El curso de matias dura un: {diferencia_con_max}% menos que el más lento')
# print(f'El curso de matias dura un: {diferencia_con_promedio}% menos que el promedio')
# Y también vamos a ir mostrando el resultado de cada operación aritmética
# Ahora actualizamos y nos dice:
# El curso de matias dura un: 40.0% menos que el más rápido
# El curso de matias dura un: 78.57142857142857% menos que el más lento
# El curso de matias dura un: 62.5% menos que el promedio
# Para reducir el número flotante de la "diferencia_con_max" (78.57142857142857), utilizamos la división doble (//), se usa de esta manera:
# diferencia_con_max = 100 - matias_curso // otros_cursos_max * 100
# Entonces, actualizamos y ahora nos dice:
# El curso de matias dura un: 100.0% menos que el más lento
# ¿Por qué? porque esto nos devuelven números que después terminan perjudicándonos a la hora de trabajar con decimales, ¿por qué?, porque no nos devuelven números flotantes
# Entonces, ¿qué es lo que se recomienda hacer?
# Primero, se multiplica (*) por mil (1000), esto para tener más números después del decimal y después en vez de multiplicarlo (*) por cien (100) simplemente lo dividimos (/) por diez (10), entonces de esa forma tenemos como una coma (.) en el decimal. 
# diferencia_con_max = 100 - matias_curso * 1000 // otros_cursos_max / 10
# Y si actualizamos ahora, dice:
# El curso de matias dura un: 78.6% menos que el más lento
# ¿Por qué? porque lo que se está haciendo es dándole tres ceros más (+000)
# O sea, la división, la doble (//), devuelve un número que es entero, o sea que si dice "0.7" se va a redondear para 0, si dice que es "1.2" se redondea para "2"
# En cambio, si se multiplica (*) por mil (1000) lo que antes era "1" ahora es "100", lo que antes era "1.4" ahora es "140"
# Entonces, cuando lo dividimos (/), no nos va a dar un número tan bajo y después ese número lo restamos (-) y esa forma es cómo una forma en la matemática para obtener esto.
# diferencia_con_max = 100 - matias_curso * 1000 // otros_cursos_max / 10
# Si sabemos que todo lo que está después de la coma (.) se borra, hagamos que lo que está después de la coma (.), pasar la coma (.) para que todo lo que está de la coma (.) se borre y después le volvemos a agregar la coma (.) 
# 20,6530602
# 20,6
# Y de esa forma como que ya tenemos el mismo número decimal, no en este caso en vez de moverla a dos (2) lugares la movemos una (1), si quisiéramos dos lugares lo haríamos de esta foma:
#  diferencia_con_max = 100 - matias_curso * 10000 // otros_cursos_max / 10
# Y de esa forma, ya tenemos la coma (.) movida a dos lugares
# En este caso, el nivel jerárquico del orden en el que se realiza la forma es lo mismo, pero no es lo mismo hacer esto:
# diferencia_con_max = 100 - matias_curso * 100 // otros_cursos_max / 10
# que esto:
# diferencia_con_max = 100 - matias_curso * 100 // otros_cursos_max
# Esto es matemático, pero como redondea para abajo cambia, no es una división común, entonces en este caso no se anulan números con números
# Y de esta forma, tenemos el ejercicio A hecho
# El A lo tenemos listo, es decir, ya estamos mostrando la diferencia con cada uno de los cursos
# El B nos pide que le mostremos cuál es el material de crudo que se remueve, o sea, cuál es el material que no sirve que en ambos casos sacamos 
# Y eso lo podemos obtener con los crudos, así que vamos a crear las variables de crudos:
# Duración de crudos
# crudo_promedio = 5
# crudo_matias = 3.5
# Cuando hablamos de crudo nos referimos al vídeo sin editar
# Por ejemplo, si se tiene un vídeo crudo de 5 horas, cuando se edita dura 4, más o menos, ¿por qué? porque es el crudo, es el material que sacamos cuando lo editamos, el crudo es el vídeo sin editar
# Ahora lo que tenemos que hacer es calcular la diferencia, porque sabemos que "matias_curso" hasta este momento duró "1.5" y hasta este momento se grabó "3.5" mientras que en los otros cursos "5" es lo que se grabó y quedó "4" hasta este momento
# Entonces, tenemos que hacer un cálculo de diferencias, así que vamos a hacerlo 
# De hecho, podemos copiar la misma fórmula, copiamos la de arriba, vamos abajo y ponemos:
# Calculando el porcentaje de tiempo vacio removido
# tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
# Y más o menos, si preguntamos cuánto es, cuánto nos da esto
# Primero vamos a agregar un comentario donde están los print():
# Mostrando las diferencias de duración (ejercicio A)
# print(f'El curso de matias dura un: {diferencia_con_min}% menos que el más rápido')
# print(f'El curso de matias dura un: {diferencia_con_max}% menos que el más lento')
# print(f'El curso de matias dura un: {diferencia_con_promedio}% menos que el promedio')
# Y después agregamos esto:
# Mostrando la cantidad de espacios vacíos que se remueven (ejercicio B)
# print(tiempo_vacio_promedio)
# ¿qué nos devuelve este print()?
# devuelve esto:
# 20.0
# O sea, nos devuelve un 20%