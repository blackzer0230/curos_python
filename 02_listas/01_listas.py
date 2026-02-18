    ### listas ###

# Una lista se puede hacer asi
my_list = list( )
# Esta tambien es otro lista
my_other_list = []

print(len(my_list))


my_list = [10, 24, 17, 40, 40, 7, 65]
print(my_list)
print(len(my_list))
print(type(my_list))


my_other_list = [20, 1.80, "choso", "gonlez"]
print(my_other_list)

# Como acceder a una lista 
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[2])
print(my_other_list[-1])
print(my_other_list[-3])
                        # una lista no es una tupla!!!!!


# retorno en numero si algo que repite en esa lista
print(my_other_list.count("choso"))
print(my_list.count(40))

# Desempaquetar una lista ?
age, height, alias, surname = my_other_list
print(surname)

# Se pueden sumar listas?
print(my_list + my_other_list)


# python es de tipado dinamico y se cambia mucho
my_list = "hola choso"
print(my_list)
print(type(my_list))



# como definir una constante en python? no se puede, pero se puede usar mayusculas para indicar que no se debe cambiar
# CONSTS_PI = 3.1416
# CONTS_NAME = "choso gonlez"


# agregar al final
my_other_list.append("lovesthe")
print(my_other_list)

# insertar en una posicion
my_other_list.insert(1, "azul")
print(my_other_list)

my_other_list[1] = "Rojo"
print(my_other_list)


# eliminar el primero que vea
my_other_list.remove("Rojo")
print(my_other_list)

# eliminar pero quedarse con ese valor
my_other_list.pop()
print(my_other_list)

del my_other_list[2]


my_new_list = my_other_list.copy()

my_other_list.clear()
print(my_other_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)


# numerooooooss
my_new_list.sort()
print(my_new_list)

# explicar revanadas










