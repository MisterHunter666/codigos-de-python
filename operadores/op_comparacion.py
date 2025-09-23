# (valor) (operador) (valor)
#    a    (operador)    b

igual_que = 5 == 6 # no (False)

distinto_de = 5 != 6 # si (True)

mayor_que = 5 > 6 # no (False)

menor_que = 5 < 6 # si (True)

mayor_o_igual = 5 >= 6 # no (False)

menor_o_igual = 5 <= 6 # si (True)

# calculos combinados

a = 5
b = 10
c = 20
comparacion = a + b == c # 5(a) + 10(b) = 15, 15(a + b) == 20(c) ? no (False) 

# comparar usuarios

contraseña_almacenada = "BoloneseMaestro"
contraseña_escrita = '''BoloneseMaestro'''
# Los tipos de comillas no cambian la forma en la que se crean los strings, lo unico que importa es que sean strings ( cadenas de texto).
print(contraseña_almacenada == contraseña_escrita) # si (True)

# = es asignar
# == es comparar
# Los operadores de comparacion devuelven True (Verdadero) o False (Falso).
# Los operadores de comparacion sirven mucho para los condicionales.
# Los operadores de compacion agarran el primer valor y lo comparan con el segundo.

