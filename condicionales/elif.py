# El else-if es otra condición extra

# Por ejemplo:

ingreso_mensual = 81000 # se crea una variable llamada "ingreso_mensual" con un valor de 8000
gasto_mensual = 80000 # se crea una variable llamada "gasto_mensual" con un valor de 2000

# if anidados y else if (elif en Python)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0: # if anidado
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("bien pa, estas bien")
    else:
        # el else se pone en el mismo nivel jerárquico que el if de gasto_mensual
        print("y pa, estas gastando una banda, hay que ver si te alcanza")
    
elif ingreso_mensual > 1000:
    print("estas bien en Latinoamérica")

elif ingreso_mensual > 500:
    print("estas bien en argentina")
    
elif ingreso_mensual > 200:
    print("estas bien en venezuela")
    
else:
    print("sos pobre")
    
# En Python, el else if se escribe "elif".

# Si la primer condición no se cumple, no vamos al else, vamos a darle una segunda condición.
# Si ingreso_mensual no es 10000, es 5000, no vamos a decirle "sos pobre", vamos a ver si tiene más de 1000.
# A 10000 no llega, vamos a ver si llega a 1000.
# Si llega a 1000, le decimos "estas bien en Latinoamérica".
# Y si no llega a 1000, ahí sí le decimos "sos pobre".
# En caso de que sea mayor a 10000, le decimos "estas bien en cualquier parte del mundo", y los demás print no se ejecutan, ninguna de las dos.
# En caso de que la primera condición (if ingreso_mensual > 10000:) no se cumpla, se pasa a la segunda condición (elif ingreso_mensual > 1000:).
# Y si la segunda condición se cumple, ejecuta el código (print("estas bien en Latinoamérica")) pero el código del else no (print("sos pobre")).
# Ahora, si la primera condición no se cumple y la segunda condición tampoco se cumple, recién ahí se ejecuta el código del else: "sos pobre".
# También se pueden poner varios elif.
# Esta forma de trabaja con condicionales es muy útil y lo vamos a ver en casos prácticos
# Conceptualmente, hay algo que se llama ifs anidados que es un if adentro de otro if, que también se hace mucho eso de meter un if adentro de otro if.
# Suponiendo que se tengan que cumplir dos condiciones al mismo tiempo, se puede usar un if anidado.
# Por ejemplo:
# si el ingreso_mensual es mayor a 10000, pero además los gastos son menores a 7000, le decimos "estas bien". Y sino le podemos decir otra cosa.
# Los elif no pueden ir después de un else, solamente pueden ir después de un if.


# if ingreso_mensual - gasto_mensual > 3000: 
#        print("ahora si estas bien")

# Si la diferencia entre lo que ingresa y lo que gasta es de 3000, le decimos "ahora si estas bien"

# Podemos hacer una condición que si el tipo gasta más de lo que ingresa, está en déficit. 

# if ingreso_mensual > 10000:
#    if ingreso_mensual - gasto_mensual < 0: 
#        print("estas en deficit")
#    elif ingreso_mensual - gasto_mensual > 3000:
#        print("bien pa, estas bien")
#    else:
#        print("y pa, estas gastando una banda, hay que ver si te alcanza")

# Si el ingreso_mensual - gasto_mensual es menor a 0, significa que está en deficit.
# Por ejemplo: Si gana 72000 y le restamos lo que gasta (80000), está en 8000 de pérdida.
# Entonces, le decimos "estas en deficit".
# Ahora bien, si se pasó de 72000 a 92000, va a decir "bien pa, estas bien".
# Y si ahora se gana 81000 y se gasta 80000, va a decir "y pa, estas gastando una banda, hay que ver si te alcanza".

# Este programa sirve como ejemplo para moverse con el if y else if.
# Es un ejemplo de else if e if anidado.