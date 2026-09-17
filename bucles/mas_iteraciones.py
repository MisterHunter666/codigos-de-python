
frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]

#Evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == 'manzana':
        continue
    print(f'Me voy a comer una {fruta}')
    
#Evitar que el bucle siga ejecutandose
for fruta in frutas:
    print(f'Me voy a comer una {fruta}')
    if fruta == 'pera':
        break
print("bucle terminado")

# Vamos a crear una lista que va a tener por ejemplo frutas...
# frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
# Ahora si nosotros hacemos lo mismo...
# for fruta in frutas:
#     print(fruta)
# Recorro "fruta"...
# banana
# manzana
# ciruela
# pera
# naranja
# granada
# durazno
# Ya está, se nos recorre y se nos muestran todas las frutas  
# Pero supongamos que estas son las frutas que nosotros nos vamos a comer
# Entonces, agarramos y ponemos:
# print({fruta})
# La ponemos entre corchetes...
# Los corchetes los ponemos entre llaves {}
# print(f'{fruta}')
# Acá le ponemos una "f" y acá ponemos:
# print(f'Me voy a comer una {fruta}')
# Lo recorremos y nos muestra...
# Me voy a comer una banana
# Me voy a comer una manzana
# Me voy a comer una ciruela
# Me voy a comer una pera
# Me voy a comer una naranja
# Me voy a comer una granada
# Me voy a comer una durazno
# Todas las frutas se comen
# Pero supongamos que de repente nosotos digamos:
# "La granada a mí no me gusta"
# Y acá lo que tenemos que hacer es decir lo siguiente:
# if fruta == 'granada':
#     continue
# print(f'Me voy a comer una {fruta}')
# ¿Qué hace el "continue"?
# El continue dice: "El bucle va a terminar la vuelta y vamos a saltar"
# Todo lo que hace, porque vimos que el bucle da varias vueltas: "vuelta 1", "vuelta 2", "vuelta 3"
# Si tiene cinco (5) elementos da cinco (5) vueltas
# "Vuelta 1", "vuelta 2", "vuelta 3", "vuelta 4", "vuelta 5"
# Supongamos que en cada vuelta hay cinco (5) instrucciones
# Si la instrucción tres (3) es "continue"
# Y "continue" se ejecuta
# Todo lo demás no importa
# Se saltea a la siguiente vuelta
# Entonces nosotros actualizamos...
# Nos dice:
# Me voy a comer una banana
# Me voy a comer una manzana
# Me voy a comer una ciruela
# Me voy a comer una pera
# Me voy a comer una naranja
# Me voy a comer una durazno
# Se comen todas las frutas pero "granada" desapareció
# ¿Por qué?
# Porque cuando "fruta" vale "granada", no decimos "Me voy a comer una granada"
# Lo salteamos antes
# Y ahora sí pasa a la siguiente fruta que es "durazno"
# Y dice "Me voy a comer un durazno"
# if fruta == 'granada':
#     continue
# Si acá le decimos: "no me gusta la manzana"
# if fruta == 'manzana':
#     continue
# Ejecutamos...
# Me voy a comer una banana
# Me voy a comer una ciruela
# Me voy a comer una pera
# Me voy a comer una naranja
# Me voy a comer una granada
# Me voy a comer una durazno
# Y ahora se ejecuta
# Y se come todo menos la "manzana"
# ¿Por qué?
# Porque cuando la "fruta" es una "manzana" no se la come 
# Entonces, pasamos a la siguiente vuelta
# ¿Por qué?
# Porque acá se como la "fruta" 
# Pero no queremos que llegue a "manzana"
# Pero queremos que el bucle se siga ejecutando
# Entonces, pasamos (continue)
# Ahora supongamos que acá vamos a poner:
# Evitando que se coma una manzana con la sentencia continue
# Ahora imaginemos que de repente sabemos que cada vez que comemos una "pera" por ejemplo...
# Vamos a ejecutar el mismo código:
# for fruta in frutas:
#     if fruta == 'manzana':
#         continue
#     print(f'Me voy a comer una {fruta}')
# Ahí está
# Sabemos que cada vez que comemos una "pera"
# Cada vez que nuestro cuerpo reciba una "pera"
# Le duele la panza y no puede continuar
# Evitar que el bucle siga ejecutándose
# ¿Cómo hacemos para decir: " Bueno, ya está, nos comimos una "pera", nos va a hacer mal el estómago, no comamos más"?
# Bueno, le decimos:
# if fruta == 'pera':
# Y en vez de decirle "continue", le vamos a decir:
# break
# Que "break" es "termina el bucle acá"
# Si teníamos que dar siete (7) vueltas y estábamos en la vuelta cuatro (4), no importa, las otras tres (3) no las damos, el bucle termina acá
# Y podemos continuar con lo que venga por debajo
# Que viene acá que es:
# print("bucle terminado")
# Entonces, si ejecutamos esto...
# Me voy a comer una banana
# Me voy a comer una manzana
# Me voy a comer una ciruela
# bucle terminado
# Fijémonos en qué se come hasta una "ciruela"
# Y después la "pera" no se la come
# Vamos a hacerlo al revés
# Vamos a hacer que se coma primero la "pera"
# Se come la "pera" y después ejecutamos el condicional
# for fruta in frutas:
#     print(f'Me voy a comer una {fruta}')
#     if fruta == 'pera':
#         break
#     print("bucle terminado")
# Actualizamos...
# Me voy a comer una banana
# Me voy a comer una manzana
# Me voy a comer una ciruela
# Me voy a comer una pera
# bucle terminado
# Se come la "pera" y ya está, terminó
# Basta de comer porque se comió la "pera"
# Una vez que se comió la "pera", el bucle termina
# Si nosotros le sacáramos el "break", vamos a ver lo que pasa...
# for fruta in frutas:
#     print(f'Me voy a comer una {fruta}')
#     print("bucle terminado")
# Me voy a comer una banana
# Me voy a comer una manzana
# Me voy a comer una ciruela
# Me voy a comer una pera
# Me voy a comer una naranja
# Me voy a comer una granada
# Me voy a comer una durazno
# bucle terminado
# Sin el "break", se come todo
# Termina la "pera" y después se come una "naranja", una "granada" y un #durazno"
# Ahora con el "break"... 
# # for fruta in frutas:
#     print(f'Me voy a comer una {fruta}')
#     if fruta == 'pera':
#         break
#     print("bucle terminado")
# Actualizamos...
# Me voy a comer una banana
# Me voy a comer una manzana
# Me voy a comer una ciruela
# Me voy a comer una pera
# No llega a comerse nada más después de la "pera"
# Porque el "break" lo que hace es terminar todos los bucles 
# Después tenemos una forma interesante que es iterar cadenas de texto
# Vamos a iterar cadenas de texto
# Antes de hacer eso, otra cosa interesante es si acá ponemos:
# else:
# Y acá ponemos:
# print("terminado")
# Cuando el bucle hace un "break"...
# Con un "break", cuando el bucle termina en un "break", se saltea todo completo
# El "else" tampoco lo ejecuta
# Esa es la diferencia
# Que cuando encuentra un "break", no ejecuta nada más
# Cuando no lo encuentra, sí lo sigue ejecutando
# Y cuando termina el bucle, ejecuta el "else"
# Esa es la diferencia entre usar un "else" después de un "for" y poner las condiciones solas