"""
Autor: Miguel_Murua
Fecha: 29/11/2023
"""
# Obtener la fecha y hora actuales en el sistema.

import datetime

ahora = datetime.datetime.now()
print(ahora)
print(type(ahora))
print(ahora.strftime('%d/%m/%y %H:%M:%S'))
