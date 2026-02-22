    ### SET ###
# Un set es una colección desordenada, mutable y sin elementos duplicados. 
# Se utilizan cuando la unicidad de los elementos y las operaciones de conjuntos (unión, intersección, etc.)
# son importantes.

# Dos formas de crear un set vacío
mi_set = set()               # Correcto: set vacío
mi_otro_set = {}              # ¡Cuidado! Esto crea un DICCIONARIO vacío, no un set

print(type(mi_set))           # <class 'set'>
print(type(mi_otro_set))      # <class 'dict'>  (por eso es importante no confundir)

# Para crear un set con elementos, usamos llaves pero con al menos un elemento
mi_otro_set = {"choso", "gonlez", 20}
print(type(mi_otro_set))      # Ahora sí es <class 'set'>
print(len(mi_otro_set))       # 3
print(mi_otro_set)

# agregar un elemento
mi_otro_set.add("sthefanny")
print(mi_otro_set) # el orden puede varias 

# Intentar agregar un elemento que ya existe
mi_otro_set.add("choso")
print(mi_otro_set) # no se agregar porque ya existe el elemento 

# Manera de comprobar que existe
print("choso" in mi_otro_set)   # True
print("chosi" in mi_otro_set)   # False

# ELIMINAR 
mi_otro_set.remove("gonlez") # lo elimina, si no existe da error

mi_otro_set.discard("TeAmo") # lo elimina, si no existe no dara error

















