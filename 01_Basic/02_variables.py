# la forma correcta de nombrar una variables es usando letras en minusculas y es guion bajo _

nombre = "Harry"
apellido = "Gonzalez"
edad = 20
nombre_completo = "Harry Gonzalez"


#imprimir variables
print(nombre)
print(apellido)
print(edad)
print(nombre_completo)


# concatenacion de variables en print
print(nombre, apellido, edad) 
print("mi nombre es:", nombre_completo)


# convertir valor 
#entero
anio = 2026
print(type(anio))

#string
anio_str = str(anio)
print(type(anio_str))

#float
anio_float = float(anio)
print(type(anio_float))

#booleano
anio_bool = bool(anio)
print(type(anio_bool))




# variables en una sola linea (Cuidado con abusar de esta sintaxis)
alias, age, country = "choso", 33, "venezuela"
print("soy", alias, "tengo", age, "anios con ese alias y soy de", country)




# entrada de datos por el usuario
nombre_usuario = input('ingrese su usuario de lol: ')
print('su usuario de lol es:', nombre_usuario)



# funciones del sistema
print(len(nombre)) # cantidad de caracteres
