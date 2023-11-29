"""
Autor: Miguel_Murua
Fecha: 29/11/2023
"""
# Obtener la representacíon inversa de una cadena de caracteres.

cadena = 'Python'

for i in range(len(cadena) - 1, -1, -1):
    print(cadena[i], end='')

print()

print(cadena[:])
