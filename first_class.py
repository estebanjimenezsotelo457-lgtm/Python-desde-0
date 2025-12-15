#Mensaje en la terminal, en este caso es "Hola mundo"...
#print ("Hola mundo")

# Varibles
#type_int = 5 # Tipo entero...
#type_float = 5.00 # Tipo decimal o real...
#type_strings = "Hola" # Tipo texto...
#type_bolean = #true o False 

# Operaciones 
#print ("Esto es una suma")
#numero_uno = 2
#numero_dos = 4
#resultado = numero_uno + numero_dos
#print(resultado)

# Cadena de caracteres (Strings)
#mensaje = "Hola"
#mensaje += " " # += Vas a sumar contenido a la varible sin borrar nada...
#mensaje += "Hernesto"
#print(mensaje) # Resultado "Hola Hernesto"...
               # Si pusieras = en vez de += se borraria el contenido de la variable

# Concatenacion (unir dos cadenas o mas "+")
#mensaje = "Hola"
#espacio = " "
#nombre = "Hernesto"
#print (mensaje + espacio + nombre) #Resultado "Hola Hernesto"

# Con numeros
#numero_uno = 5
#numero_dos = 5
#resultado = numero_uno + numero_dos
#resultado = str(resultado) # Se tiene que convertir el int a string porque si no da error...
#print ("El resultado de la suma es " + resultado) 
                                                 # Concatenar int con stringe no se puede...

# Busqueda (find) localizar dentro de una cadena, una sub cadena mas pequeña a un caracter
#mensaje = "Hola Hernesto"
#buscar_cadena = mensaje.find("Hernesto") # Busca por posicion que comienza desde cero y da resultado el nuemro de la poscion que esta el string
#print(buscar_cadena) # Resultado da el numero de poscion de string que en este caso es 5
            
# Extraccion (extraer porciones de la cadena)
#mensaje = "Hola Hernesto"
#extraer_subcadena = mensaje[1:8] # Comienza a recorrer caracter por caracter de 1 a 8 y lo extrae pero hasta la posicion numero 7 
#print (extraer_subcadena) # Resultado "ola Her"

# Comparacion == (para comparar dos cadenas de caracteres)
#mensaje_uno = "Hola"
#mensaje_dos = "Hola"
#print (mensaje_uno == mensaje_dos) # Los comprar a ver si son iguales o no y el resualtado puede ser True o False

# Palabras reservadas 
#and 
#del 
#for
#is 
#raise
#assert
#if 
#else
#elif
#from
#labda
#return
#break
#global
#not
#try
#class
#exept
#or
#while
#continue
#exec
#import
#yield
#def 
#finally
#in
#print

# Operadores aritmeticos 
# Suma +
# Resta -
# Multiplicacion *
# Exponente **
# Modulo %
# Division /
# Division entera // 

#print ("suma: ")
#numero_uno = 5
#numero_dos = 4
#nesultado = numero_uno + numero_dos
#resultado = str (resultado)
#print("El resultado de la suma es: " + resultado)

# ¿Como saber que tipo de dato es?
#numero = 5 
#print(numero , type(numero))


# Input (solicitar datos desde teclado osea al usuario)

# Tipo string...
#palabra = input("Introduce una palabra: ")

# Tipo int...
#num_int = int(input("Introduce un numero entero: "))

# int() es para el python sepa que viene una valor entero y se asigne como entero...

# Tipo float...

#num_float = float(input("Introduce un numero float: "))

# Tipo compelo 

#num_complex = complex(input("Introduce un numero complejo: "))

#print ("texto o string: ", palabra) 
#print ("entero o int: ", num_int)
#print ("decimal o float: ", num_float)
#print ("complejo o complex: ", num_complex)

# If (condiccion logica, si algo cumple o no)

# If condiccion logica :

# Ejemplo: 
#edad_carlos = 18
#if edad_carlos == 18:    
    #print ("Carlos tiene 18 años")
#else:
    #print ("Carlos no tiene 18 años")

# Aca vimos que si carlos tiene 18 años la condiccion se cumple y se termina con un mesaje
# Si no se cumple va al else que seria falso o negativo que se cumpla la condiccion y termina tambien con un mensaje

# round (para indicar cuantos decimales quiero que aparezcan)
#round (promedio, 2) aca estamos solicitando que de la variable promedio solo me de dos decimales

# If con opiciones multiples (elif)
# Aca podemos poner varias opciones o caminos
# ejemplo:

# nombre = "paula"
# if nombre == "laura":
#     print ("El nombre es: " + nombre)
# elif nombre == "paula":
#     print ("El nombre es: " + nombre)
# else:
#     print ("El nombre se desconoce ")

# Aca esta mirando condiccion por condiccion, el nombre de que esta en la variable es paula
# Mira la primera que es laura que no cumple la condiccion, despues pasa a la otra opcion que es paula
# Ahi ya encontro el nombre y se acaba con un mensaje
# Si no se cumpliera ninguna termina con el else diciendo que el nombre se desconoce


# Operadores relacionales 
# < menor que, si quiero puedo poner que 5 < 4 aunque no seria logico pero se puede
# > mayor que, 7 > 5 algo mas logico 
# == igual a, 5 == 5 donde algo sea igual si es igual da true si no false
# != diferente a, 4!=5 cuatro es diferente a cinco 
# <= menor o igual, 6 <= 6 si el 6 es menor o igual a 6
# >= mayor o igual, 9 >= 9 donde se 9 sea mayor o igual a 9

#1 ejercicio: 

# print ("Introduce los dos numeros a comparar: ")

# nro1 = int(input("Introduce el primer numero: "))
# nro2= int (input("Introduce el segundo numero: "))

# #if nro1 < nro2: 
#     # print(nro1 , "Es menor que", nro2)
# elif nro1 > nro2:
#     # print(nro1, "Es mayor que", nro2)
# elif nro1 == nro2:
#     print(nro1, "Es igual a", nro2)
# elif nro1 != nro2:
#     print(nro1 , "Es diferente a", nro2)
# else:
#     print("No introduciste los dos numeros") 
# Operadores logicos (and, or, not)

#num_uno = 5
#num_dos = 5 
#if num_uno == 5 and num_dos >= 5:
    #print (" Ambas partes se han cumplido")
#else:
    #print(" Una o ambas partes no se han cumplido")

# And es que quiero que las dos partes se cumplan ejemplo esta y esta parte

# num_uno = 5
# num_dos = 30

# if num_uno > 3 or num_dos == 30:
#     print (" Una o ambas partes de han cuplido")
# else: 
#     print (" Ninguna de las partes de cumplido")

# Or cuando quiero que una o otra parte se cumpla 

# numero = 10
# if not numero > 100:
#     print ("El numero no es mayor a 100")

# Le estamos diciendo a el programa si 10 no es mayor a 100 se ejecute el print

# num_uno = int(input(" Escribe un numero que sea igual a 5: "))

# if not num_uno == 5:
#     print (" El numero no es igual a 5, pero si se cumple la condicion")
# else:
#     print (" El numero es igual a 5, pero no se cumple la condicion")

# Basicamente es un if a la inversa, porque en primera instancia el numero no es igual a 5 pero cumple 
# Despues el numero puede ser igual a 5, pero no la cumple
# El el num_uno pase de ser true a ser false para cumplir la condiccion 

# Segundo ejercicio 

# nombre = input (" Hola, ingresa tu nombre aqui: ")
# clave = int(input(" ingresa tu numero de clave son del 1 a el 3: "))
# años = int(input(" Ingresa tu nuemro de años que haz estado trabajando: "))

# if clave == 1 and años == 1:
#     print (" Por el año que trabajaste recibes 6 dias de vacaciones")
# elif clave == 1 and años > 2 and años < 7:
#     print (" Por lo años que trabajaste recibes 14 dias de vacaciones")
# elif clave == 1 and años > 7:
#     print (" Por los años que trabajaste recibes 30 dias de vacaciones")
# elif clave == 2 and años == 1:
#     print("Por el año que trabajaste recibes 7 dias de vacaciones")
# elif clave == 2 and años > 2 and años < 7:
#     print (" Por lo años que trabajaste recibes 14 dias de vacaciones")
# elif clave == 2 and años > 7:
#     print (" Por los años que trabajaste recibes 22 dias de vacaciones")
# elif clave == 3 and años == 1:
#     print("Por el año que trabajaste recibes 10 dias de vacaciones")
# elif clave == 3 and años > 2 and años < 7:
#     print (" Por lo años que trabajaste recibes 20 dias de vacaciones")
# elif clave == 3 and años > 7:
#     print (" Por los años que trabajaste recibes 30 dias de vacaciones")
# else:
#     print (" La clave no existe")

# # Ejercicio 3 (Numero par o impar)

# numero = int(input(" Ingresa el numero: "))

# if numero % 2 == 0:
#     print (" El numero" , numero , "es par")
# else:
#     print (" El numero" , numero , "es impar")

# Ejercicio 4 (El numero mas grande de los 3)

# nro1 = int(input(" Ingresa el primer numero: "))
# nro2 = int(input(" Ingresa el segundo numero: "))
# nro3 = int (input(" Ingresa el tercer numero: "))

# if nro1 > nro2 and nro3:
#     print (" El " , nro1 , "es el mayor a" , nro2 ,"y" , nro3)
# elif nro2 > nro1 and nro3:
#     print( " El " , nro2 , "es el mayor a" , nro1 ,"y" , nro3)
# elif nro3 > nro1 and nro2:
#     print( " El " , nro3 , "es el mayor a" , nro1 ,"y" , nro2)
# else:
#     print(" No ingresaste ningun numero o no ingresaste los 3 numeros")

# Operadores de asignacion 

# El cual asigna el valor que se encuentra de el lado derecho a la variable del lado izquierdo
# Es decir, x = y asigna el valor de y a x 

# = 
# Esta asignacion es la que recibe el valor que le des a una variable, puede ser texto o numeros 
# ejemeplo: X = luz o M = 12

# += 
# por ejemplo tienes la varibale M = 12 y quieres añadirle otro numero, pues puedes hacerlo asi:
# M += 5, entonces la varible queda en 17 porque le añadiste otro valor y se sumaron 

# -= 
# Lo mismo que el de la suma pero con resta
# tienes la variable M = 12 y quieres restarle a esa variable entonces puedes hacerlo asi:
# M -= 5, entonces la variable queda en 8 porque le restaste el valor que es 5

# *= 

# Digamos que tienes la variable M = 12 y quieres multiplicarla por 2 entonces puedes hacerlo asi:
# M *= 2, entonces al iniciar tenias tu variable M = 12 y la multiplicaste x2 M *= 2 entonces el resultado es:
# M = 24 

# /= 

# Digamos que tienes la variable M = 12 y quieres dividirla por 2 entoces puedes hacerlo asi:
# M /= 2, entoces al iniciar tu variable valia 12 M = 12 al dividirla por 2 entonces quedaria asi:
# M = 6 

# // ( La division entera es que si yo quiero dividir algo que me pueda dar como resultado algo decimal
# solo me dara como resultado su parte entero osea digamos 3.3 me daria su parte entera que es 3)
# en su ejecucion es igual a la division normal solo le agrego //= y le doy el valor en el que quiero dividir

# % ( Modulo o resto)

# Digamos que tienes la variable M = 12 y quieres saber el residuo de la division y se guarde en tu variable M
# Entonces hacemos lo siguiente M %= 2, esto siganifica divide M = 12 entre 2 pero dame el residuo en la variable
# No el resultado de la division si no el residuo que seria 0 porque no sobra nada

# Juego de varibles 

# Esto seria los mismo que lo anterior pero con variable por ejemplo
# Sumemos dos variables M += J seria asi M = 12 + J = 3 seria M 15 = y J = 5
# M queria con 15 y J con 5, J le sumo pero queria con el mismo valor

# Ejercicio

# print (" Calculadora ")

# print("//////////////////////")
# print("/                    /")
# print("/  Menu de opciones  /")
# print("/                    /")
# print("/      1. suma       /")
# print("/      2. resta      /")
# print("/      3. div        /")
# print("/      4. multi       /")
# print("/                    /")
# print("//////////////////////")

# opcion = int(input(" Hola, elige la operacion que quieras: "))

# primer_numero = int(input(" Ingresa tu primer numero: "))
# segundo_numero = int(input(" Ingresa tu segundo numero: "))

# if opcion == 1:
#     primer_numero += segundo_numero
#     print (" El resultado de" , primer_numero , "+" , segundo_numero ,"es:" , primer_numero)
# elif opcion == 2:
#     primer_numero -= segundo_numero
#     print (" El resultado de" , primer_numero , "-" , segundo_numero ,"es:" , primer_numero)
# elif opcion == 3:
#     primer_numero /= segundo_numero
#     print(" El resultado de" , primer_numero , "/" , segundo_numero ,"es:" , primer_numero)
# elif opcion == 4:
#     primer_numero *= segundo_numero
#     print(" El resultado de" , primer_numero , "x" , segundo_numero ,"es:" , primer_numero)
# else:
#     print(" No ingresaste ningun numero o solo uno")














