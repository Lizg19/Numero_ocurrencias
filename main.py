#El objetivo es contar el número de ocurrencias de las palabras en un archivo de texto.

palabraBuscar = input("Ingrese la palabra para realizar el conteo: ")
archivo = open('libro.txt','r')
i=0
contador =0
for line in archivo.readlines():
    lista_sin_puntos = line.split(".")
    texto_sin_puntos= " ".join(lista_sin_puntos)
    lista_sin_comas = line.split(".")
    texto_sin_comas= " ".join(lista_sin_comas)
    lista = texto_sin_comas.split()
    i = lista.count(palabraBuscar)
    contador = contador + i
if contador !=1:
  print("( " + palabraBuscar + " , " + str(contador) + ") ")
else:
  print("( " + palabraBuscar + " , " + str(contador) + ") ")
archivo.close ()
