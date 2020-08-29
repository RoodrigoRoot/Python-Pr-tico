#file = open("information.txt", "a")
#file.write("Línea 3\n")
#file.close()

#file = open("information.txt", "a")
#file.write("Línea 4\n")
#file.close()

def write_file(user):
    file = open("users.txt", "a")
    file.write(user)
    file.close()

def registrar_usuario():
    name = input("Ingresa tu nombre: ")
    last_name = input("Ingresa tu apellido: ")
    user =  "Nombre: {}, Apellido: {}\n".format(name, last_name)
    write_file(user)

registrar_usuario()