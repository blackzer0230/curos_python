    ### STRING ###

my_string = "string"
my_other_string = "mi otro string"

print(len(my_string))
print(len(my_other_string))

# como hacerle un salto de linea a un string con el \n
my_new_line_string = "este es un string\ncon salto de linea"
print(my_new_line_string)

# para tabular y un string se usa el \t
my_tab_string = "\teste es un string con tabulaion"
print(my_tab_string)

# un escapado de lineas
my_scape_string = "\\t este sera un escapado \\n de lineas"
print(my_scape_string)


# Formateos de string 

#%
name, surname, age = "harry", "gonzalez", 20
print("mi nombres %s %s y tengo %d anios" %(name, surname, age))

# .format()
print("mi nombres {} {} y tengo {} anios".format(name, surname, age))

# f-string
print(f"mi nombres {name} {surname} y tengo {age} anios")



# desempaquetados de caracteres
lenguaje = "Python"

#misma cantidad de variables por la cantidad de caracteres de un string
a, b, c, d, e, f = lenguaje

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


# division 
lenguaje_slice = lenguaje[1:3]
print(lenguaje_slice)

lenguaje_slice = lenguaje[1:]
print(lenguaje_slice)

lenguaje_slice = lenguaje[:3]
print(lenguaje_slice)

lenguaje_slice = lenguaje[-2]
print(lenguaje_slice)

lenguaje_slice = lenguaje[0:6:2]
print(lenguaje_slice)

# reversa
reversed_lenguaje = lenguaje[::-1]
print(reversed_lenguaje)













