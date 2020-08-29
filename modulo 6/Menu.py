from User import UserMethod
from BDUser import *

ADD = 1
SEARCH = 2
DELETE = 3
SHOW = 4

user_list = bd_user()

def selected_option(option):
    
    if option == ADD:
        user = UserMethod.add_user()
        add_user_db(user, user_list)
    
    elif option == SEARCH:
        id_user = UserMethod.search_user()
        search_user_db(id_user, user_list)
    
    elif option == DELETE:
        id_user = UserMethod.delete_user()
        delete_user_db(id_user, user_list)
    
    elif option == SHOW:
        UserMethod.show_users(user_list)
    
        


def menu():
    message = """Control de usuarios
**Escoge una opción**
1.-Agregar Usuario
2.-Buscar Usuario
3.-Eliminar Usuario
4.-Mostrar Usuarios
5.-Salir
Opción: """
    while True:
        option = input(message)
        option = int(option)
        selected_option(option)

menu()