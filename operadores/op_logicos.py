# operadores lógicos: or and y not
# Hay más, pero por ahora vamos a ver estos tres que son los más comunes y sencillos.

#AND (&) es un operador que compara uno y otro.

Resultado = True & True #Devolver True
Resultado2 = False & True #Devolver Falso
Resultado3 = True & False # Devolver Falso
Resultado4 = False & False #Devolver Falso


#OR (|)

Resultado5 = True | True #Devolver True
Resultado6 = False | True #Devolver True
Resultado7 = True | False #Devolver True
Resultado8 = False | False #Devolver Falso

#NOT (not) es un operador de negación que invierte el valor.

Resultado9 = not True #Devolver Falso
Resultado10 = not False #Devolver True

print(Resultado)

# Resultados con el operador AND(&)

#En el primer caso(Resultado), se le pasa True & True. Si el primer valor es True y el segundo es True, va a devolver True.

# En el segundo caso(Resultado2), va a devolver Falso porque False & True, por más que una de las dos condiciones que se le pasa sea verdadera, igual en AND tienen que ser las dos verdaderas.

#En el tercer caso(Resultado3) pasa lo mismo que en el segundo, va a devolver False porque una de las conciones es False.

#En el cuarto caso(Resultado4), también va a devolver un False, por lo que se puede ver, para que el operador AND(&) devuelva Verdadero(True), las dos condiciones, o sea el valor a y el valor b que se le pasa, tienen que ser ambos verdaderos (True & True). Con que uno de los dos sea Falso (False), ya devuelve todo Falso.

# Resultados con el operador OR(|)

# En el quinto caso(Resultado5), devuelve True

# En el sexto caso(Resultado6), devuelve True

# En el séptimo caso(Resultado7), devuelve True

# En el octavo caso(Resultado8), devuelve False

# El operador OR va a devolver False solamente si las dos condiciones no se cumplen (False | False), o sea es como lo contrario de AND. 
# AND devuelve True si ambas condiciones se cumplen, sino no.
# OR devuelve False solamente si ninguna condición se cumple. Es como el otro extremo.
# OR es o una condición o la otra.
# Solamente va a devolver False cuando ambas condiciones son falsas.
#Ejemplo: (¿La primer condición que pasa es verdadera(True)? no ¿Y la otra? sí. Entonces se devuelve un True).
# Con que alguna de las dos condiciones se cumpla, ya devuelve todo verdadero (True).
# Ahora si las dos condiciones no se cumplen, ahí se devuelve falso (False). 

# Resultados con el operador NOT(not)

# En el noveno caso(Resultado9), devuelve False porque 

# En el décimo caso(Resultado10), devuelve True

# En el operador NOT, se le da un valor True, lo convierte en falso (False).
# Si se le da un valor False, lo convierte en verdadero (True).
# O sea si se le True, devuelve False.
# Y si se le False, devuelve True.

# not True: si no es verdadero, es falso.
# not False: si no es falso, es verdadero.

# Ejemplo de NOT:
# Si se le pasa un valor que sea 2 == 2, que es verdadero, devuelve falso (False) porque 2 sí es igual a 2, entonces se convierte en verdadero (True) y el "not" va a invertir el valor, o sea si se le pasa True, da False. Y si se le False, da True.  
# Ahora, ¿qué sucede si se le pasa 2 > 49?
# Eso es falso, pero si lo es y tiene un "not" adelante, not False es True. Así que, devuelve True. Porque "2 > 49" es falso y "not 2 > 49" devuelve lo contrario de lo que devuelve "2 > 49".

 