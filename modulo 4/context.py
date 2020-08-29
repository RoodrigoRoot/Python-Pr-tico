#with open("users.txt", "a+") as file:
#    file.seek(0)
#    print(file.read())
#    print(file.readable())
#print(file.readable())
#print("Cierre del archivo")

def write_file(user):
    with open("users.txt", "a") as file:
        file.write(user)
        file.write(user)
        file.write(user)
        file.write(user)
        file.write(user)
        file.write(user)
        if file.readable():
            file.write(user)
    

def registrar_usuario():
    name = input("Ingresa tu nombre: ")
    last_name = input("Ingresa tu apellido: ")
    user =  "Nombre: {}, Apellido: {}\n".format(name, last_name)
    write_file(user)

registrar_usuario()


