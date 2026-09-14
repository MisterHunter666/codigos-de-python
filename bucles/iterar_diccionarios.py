diccionario = {
    "nombre": "matias",
    "apellido": "bolonese",
    "subs": 1000000   
}

#recorriendo diccionario para obtener las claves
for key in diccionario:
    key
    print(f"la clave es: {key}")
    
#recorriendo diccionario con items() para obtener las claves y los valores 
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es: {key} y el valor es: {value}")

# Para iterar un diccionario lo hacemos de la siguiente forma:
# Primero, creamos el diccionario
# diccionario = {
#     "nombre": "matias",
#     "apellido": "bolonese",
#     "subs": 1000000   
# }
# Acá tenemos el diccionario 
# Si lo mostramos en pantalla...
# print(diccionario)
# Ejecutamos...
# {'nombre': 'matias', 'apellido': 'bolonese', 'subs': 1000000}
# Nos muestra el diccionario
# Ahora, ¿cómo lo recorremos?
# Lo mismo
# for key in diccionario:
#     print(key)
# A ver qué es lo que nos muestra...
# nombre
# apellido
# subs
# Nos muestra "key"
# Porque el "key" es la clave
# Cuando ponemos "key" en diccionario lo que nos está mostrando es solamente la clave
# ¿Cómo hacemos para que nos muestre los valores?
# O, ¿cómo obtenemos algo?
# Lo mismo
# Estamos recorriendo el diccionario pero no nos muestra el valor
# Solamente nos muestra la clave
# for key in diccionario:
#     print(key)
# Y acá si ponemos "value" no nos va a cambiar nada
# for value in diccionario:
#     print(value)
# nombre
# apellido
# subs
# Es lo mismo
# Porque esto no cambia nada
# Nos muestra igual los "key"
# La forma es utilizando el ".items"
# for key in diccionario.items():
#     print(key)
# Antes utilizamos el ".items"
# Eso es para iterar el elemento
# Bueno, si vamos a "F5"... 
# ('nombre', 'matias')
# ('apellido', 'bolonese')
# ('subs', 1000000)
# ahora sí vamos a ver que estamos iterando el elemento y accedemos a los dos
# Esto nos devuelve una tupla con un par "clave-valor"
# Justamente a lo que decíamos antes
# Para esto ahora entendemos que estamos usando items
# Si por ejemplo ahora decimos "key"...
# for datos in diccionario.items():
#     key = datos[0]
#     value = datos[1]
#     print(f"la clave es: {key} y el valor es: {value}")
# Entonces, si corremos el código, tenemos esto:
# la clave es: nombre y el valor es: matias
# la clave es: apellido y el valor es: bolonese
# la clave es: subs y el valor es: 1000000
# De esta forma, estamos recorriendo un diccionario
# Entonces, ponemos:
# recorriendo diccionario con items() para obtener la clave y el valor 
# for datos in diccionario.items():
#     key = datos[0]
#     value = datos[1]
#     print(f"la clave es: {key} y el valor es: {value}")
# Y vamos a hacer exactamente lo mismo
# Pero al de arriba vamos a sacarle el "items()"
# print(f"la clave es: {key}")
# Y solamente va a ser igual a (=) "key"
# recorriendo diccionario para obtener la clave
# for key in diccionario:
#     key
#     print(f"la clave es: {key}")
# En el código de abajo, obtenemos las claves y los valores
# recorriendo diccionario con items() para obtener las claves y los valores 
# for datos in diccionario.items():
#     key = datos[0]
#     value = datos[1]
#     print(f"la clave es: {key} y el valor es: {value}")
# Mientras que solamente arriba obtenemos las claves
# Es decir, obtenemos solo las claves
# Y en el otro, obtenemos las claves y los valores
# Ahí tenemos dos diferentes formas de recorrer un diccionario
# Vamos a ver a continuación algo...
# Vamos a crear un archivo nuevo, que va a ser "mas_iteraciones.py"...