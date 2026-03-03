# 📘 Mis Apuntes de Python

¡Hola! Este repositorio contiene todos mis apuntes y ejemplos de código mientras aprendo Python. Aquí encontrarás desde conceptos básicos hasta temas más avanzados, todo explicado de forma sencilla y con ejemplos prácticos.

## 📋 Tabla de Contenidos

1. [Listas](#listas)
2. [Tuplas](#tuplas)
3. [Sets (Conjuntos)](#sets-conjuntos)
4. [Diccionarios](#diccionarios)
5. [Métodos de Strings](#métodos-de-strings)
6. [Bucles (for)](#bucles-for)
7. [Funciones](#funciones)
8. [Clases y POO](#clases-y-poo)
9. [Manejo de Excepciones](#manejo-de-excepciones)
10. [Módulos](#módulos)

---

## 📌 Listas

Las listas son colecciones **ordenadas**, **mutables** y pueden contener elementos de diferentes tipos.

```python
# Crear listas
mi_lista = [10, 24, 17, 40, 40, 7, 65]
mi_otra_lista = [20, 1.80, "choso", "gonlez"]

# Acceder a elementos
print(mi_otra_lista[0])   # 20
print(mi_otra_lista[-1])  # "gonlez"

# Métodos útiles
mi_lista.append(99)        # Añade al final
mi_lista.insert(1, 15)     # Inserta en posición 1
mi_lista.remove(40)        # Elimina el primer 40
elemento = mi_lista.pop()  # Elimina y devuelve el último
mi_lista.sort()            # Ordena la lista
mi_lista.reverse()         # Invierte el orden

# Slicing (rebanadas)
print(mi_lista[2:5])       # Elementos del índice 2 al 4
