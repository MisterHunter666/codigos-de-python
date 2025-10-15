#pedirle un dato al usuario
nombre = input("che maestro, dame tu nombre: ")

#mostrando el dato
print(f'el nombre es: {nombre}')

# pedirle un dato al usuario
# ¿Por qué eso hacemos con input?
# Es una función que nos permite pedirle un dato al usuario.
# ¿cómo lo hacemos?
# nombre = input("che maestro, dame tu nombre:")
# Así que cuando actualizamos, ahora nos deja un espacio para que le demos click y escribamos.
# Se le puede poner "Matias" y ahora no pasó nada
# ¿Pero qué pasó?
# Ahora la variable "nombre" va a ser igual a "Matias"
# O sea, todo esto: "che maestro, dame tu nombre:" se va a convertir en "Matias"
# nombre = "Matias"
# ¿Cómo lo podemos corroborar?
# Ahora vamos a dejar un espacio porque otra cosa interesante es que cuando no dejamos espacios lo ponemos todo junto.
# Pero si dejamos un espacio, actualizamos y ahora nos deja un espacio y nos permite escribir espaciadamente.
# Así que es lo que vamos a hacer
# nombre = input("che maestro, dame tu nombre: ")
# Vamos a mostrar abajo print, 
# mostrando el dato
# print(nombre)
# Actualizamos y nos pide el nombre, en nuestro caso le ponemos "Matias" y abajo lo muestra:
# che maestro, dame tu nombre: Matias
# "Matias"
# Es más, podemos concatenarlo
# print(f'el nombre es: {nombre}')
# Actualizo y ahora dice:
# che maestro, dame tu nombre: Matias
# el nombre es: Matias
# Así es como le pedimos un dato al usuario
# Ahora, ¿qué pasa si le pedimos un número?
# Bien, vamos a pedirle un número
# le pasamos el número 11, por ejemplo
# che maestro, dame tu nombre: 11
# el nombre es: 11
# Bueno, esto aunque parezca no es un número
# El dato que nos va a devolver input siempre es un texto
# Siempre las funciones, cuando nosotros usamos funciones, usamos print, usamos input, todas las funciones que venimos utilizando nos van a devolver cosas.
# Así como estábamos usando métodos de cadenas, métodos de listas, cada método nos devolvía un dato
# Nos devolvían números, nos devolvían listas, nos devolvían textos.
# Input lo que nos devuelve siempre es un texto.