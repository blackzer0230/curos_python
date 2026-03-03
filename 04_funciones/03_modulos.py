    ### MODULO ###
# un modulo es siemplemente un archivo .py que contiene codigo python y se puede utilizar en otros programas
    # TIPOS DE MODULOS 
    # modulo propio
    # modulo de la bibliotecas estandar
    # modulos de terceros 

# modulos propios!!!
# utilizaremos en archivo mi_modulo.py para sacar el codigo
import mi_module

print(mi_module.saludar("harry"))
print(mi_module.PI)

# poder importar funciones especificas
from mi_module import despedida, PI
print(despedida("sthefanny"))

# darle un alias a una modulo
import mi_module as mm
print(mm.despedida("sthefanny"))

# alias para funciones 
from mi_module import saludar as ss
print(ss("harry"))


# modulos de las bibliotecas estandar
import math
print(math.pow(2, 3))
print(math.pi)

import random
print(random.randint(1, 50))

import datetime
print(datetime.datetime.now())

import os 
os.system("fastfetch")


# modulos de terceros con pip 
# se instalan con pip install modulo


"""
❓ ¿Qué es esa carpeta __pycache__?

Cuando importas un módulo por primera vez,
Python compila el código a un formato intermedio (bytecode) para que la próxima vez que lo 
importes sea más rápido. Ese bytecode se guarda en la carpeta __pycache__.

¿Puedes borrarla?
Sí, sin problema. Python la volverá a crear si es necesario. 
Es segura y no debes subirla a GitHub (se ignora en .gitignore).
"""