"""
Autor: Miguel_Murua
Fecha: 28/11/2023
"""
# Métodos de lisas (append - pop - extend - remove - insert)
# Al igual que los string, también con las listas tenemos una serie.
# de términos que podemos utilizar.
# los cuales nos ayudan en casos concretos.
# Veamos algunos de los más conocidos.
# Recorrer listas
peliculas = ['pelicula1', "pelicula2", "pelicula3"]
print(peliculas)
print(peliculas[0])
print(len(peliculas))
# Con append agregamos datos al final de una lista
peliculas.append("pelicula4")
print(peliculas)
# Con pop removemos el último dato de una lista
peliculas.pop()
print(peliculas)
# Con extend agregamos un grupo de datos al final de la lista
peliculas.extend(["pelicula4", "pelicula5"])
print(peliculas)
# Con remove removemos un dato especifico de la lista
peliculas.remove("pelicula4")
print(peliculas)
# Con insert insertamos un dato en un lugar especifico de la lista
peliculas.insert(0, "pelicula0")
print(peliculas)
