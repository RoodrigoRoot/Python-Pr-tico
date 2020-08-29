import uuid

class User:
    """Clase base de usuario
    Attributes:
        name(str): Nombre del usuario,
        country(str): País del usuario,
        username(str): Usuario"""
    def __init__(self, name, country, username):
        self.__name = name
        self.__country = country
        self.__username = username
        self.__id = str(uuid.uuid4())[0:4]
    
    def __str__(self):
        return "id: {} Nombre: {} País: {} Usuario: {}".format(self.__id,
                                                               self.__name,
                                                               self.__country,
                                                               self.__username)

    def get_id(self):
        return self.__id
    
    id = property(get_id)

from BDUser import *

class UserMethod:
    """Clase para los método de usuario
    Methods:
        add_user: @ClassMethod
        show_user: @ClassMethod
        search_user: @ClassMethod
        delete_user: @ClassMethod
        """
    
    @classmethod
    def add_user(cls):
        name = input("Ingrese el nombre de la persona: ")
        country = input("Ingrese el país de la persona: ")
        username = input("Ingrese el nombre de usuario: ")
        user = User(name, country, username)
        return user

    @classmethod
    def show_users(cls, user_list):
        print("*********************Lista de Usuarios Registrados*************************")
        for user in user_list:
            print(user)
        print("***************************************************************************")

    @classmethod
    def search_user(cls):
        id_user = input("Ingrese el identificador del usuario: ")
        return id_user
    
    @classmethod
    def delete_user(cls):
        id_user = input("Ingrese el identificador del usuario: ")
        return id_user


#def wrapper_get_id(function):
#    def hijo():
#        print("*****************************************")
#        id_user = input("Ingrese el id del usuario: ")
#        function(id_user)
#        print("****************************************")
#    return hijo

#@wrapper_get_id
#def delete_user(id_user):
#    print("Usuario eliminado")
    
#@wrapper_get_id
#def search_user(id_user):
#    print("Usuario encontrado")

#delete_user()
#search_user()