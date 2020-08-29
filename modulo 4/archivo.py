#open("nombredelarchivo.extension", "escritura, lectura y sobreescritura" )
archivo = open("information.txt", "w")
print(archivo.writable())
animales = ["Gato", "Perro"]
if archivo.writable():
    archivo.write("Nuevo2 Texto2\n")
    for animal in animales:
        archivo.write("{}\n".format(animal))
archivo.close()

archivo_lectura = open("information.txt", "r")
print(archivo_lectura.read())
archivo_lectura.seek(0)
if archivo_lectura.readable():
    print("esta línea solo se verá si el archivo se puede leer")
    print(archivo_lectura.readlines())
