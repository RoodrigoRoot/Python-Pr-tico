

def write_file(user):
    file = open("users.txt", "a+")
    file.write(user)
    file.seek(0)
    print("Estos son los usuarios registrados hasta el momento:\n")
    print(file.read())
    file.close()

def registrar_usuario():
    name = input("Ingresa tu nombre: ")
    last_name = input("Ingresa tu apellido: ")
    user =  "Nombre: {}, Apellido: {}\n".format(name, last_name)
    write_file(user)

registrar_usuario()