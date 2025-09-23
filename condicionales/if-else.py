# if y else son los dos primeros condicionales que se ven
# Hay varios pero estos son los primeros dos, en realidad hay tres, pero primero se va a arrancar con estos dos.

#esta es la estructura de un condicional
#if 2 > 2: # si esto es True
   #accion # accion se ejecuta
           # este también se ejecuta
           
#if False # si esto es False
   #accion # accion no se ejecuta
          # este tampoco se ejecuta
          
# Los operadores de comparación devuelven datos booleanos (True o False).
# Si la condición es True, la acción se ejecuta.
# sino, la acción no se ejecuta.
# la acciones se ejecutan como bloques

edad = 19 # acá se crea una variable llamada "edad" se le pone un valor

if edad >= 18: # si la "edad" es mayor o 
               # igual a 18
    print("podes pasar") #se ejecuta este código
    print("forma parte del if") # forma parte del condicional
else: # sino
    print("no podes pasar") #se ejecuta este código  
    print("forma parte del else")  
    
print("no forma parte de ninguna condicion") #este código se va a ejecutar pase lo que pase porque está fuera de todas las condiciones             
                         
# el else se hace por fuera del bloque if porque Python es un lenguaje identado. 
#para salir de la condición, se tiene que ir abajo del bloque, ir en otro nivel abajo del tabulado.
# si el print se pone afuera del else, ya no forma parte de ninguna condición.
# Depende de la condición (if edad >= 18:) se va a ejecutar alguno de los dos códigos.
# Si no hay ningún else, ejecuta el primer código o sino ninguno.
# Pero si se quiere hacer algo en caso contrario, se pone un else, lo cual sirve para eso.

# Por ejemplo:

contraseña_almacenada = "BoloneseMaestro"
contraseña_escrita = '''BoloneseMaestro'''

if contraseña_almacenada == contraseña_escrita: 
    print("INICIANDO SESIÓN...") 
    
else:
    print("CONTRASEÑA EQUIVOCADA, INTENTE DE NUEVO") 
    
print("no forma parte de ninguna condicion")

# Se imprime "INICIANDO SESIÓN..." porque las contraseñas coinciden
# Se pasó la misma contraseña de la que estaba almacenada en la base de datos, por ejemplo.
# La contraseña la escribió el propio usuario, pero en un futuro lo ideal es conectarlo a una base de datos y extraer el dato que está alojado, porque se va a dar al usuario la opción de que se registre, que escriba sus datos, que esos datos se registren en la base de datos y después compararlo.
# "Me registró una contraseña que esta (BoloneseMaestro) que la sacamos de la base de datos, ¿lo que me está escribiendo (BoloneseMaestro) coincide con la contraseña que me registró?"
# si coincide, lo dejamos pasar, "INICIANDO SESIÓN...".
# Y ahí se creamos todo un proceso para iniciar sesión y efectivamente hacer que funcione 
# Y sino, si no coincide, le decimos "CONTRASEÑA EQUIVOCADA, INTENTE DE NUEVO".
# Python es un lenguaje sensitive, es decir, es sensible a mayúsculas y minúsculas
# La contraseña que se escribiendo tiene que ser exactamente igual a la que se registró.