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































