import time

class CuentaBancaria:

    def __init__(self, balance: int, name_owner: str, card_number: str):
        self.__balance = balance
        self.__name_owner = name_owner
        self.__card_number = card_number
        self.__account = self.__get_acount()

    def __get_acount(self):
        return 1

    @property
    def esta_vacia(self):
        if self.__balance == 0:
            return True
        else:
            return False

    @property
    def nombre_propietario(self):
        return self.__name_owner

    @property
    def saldo(self):
        return self.__balance

    @property
    def numero_tarjeta(self):
        return self.__card_number

    def extraer_todo(self):
        print("Retirando todo el dinero")
        time.sleep(2)
        self.__balance = 0
        print("Se ha retirado todo el dinero\n\n")

    def extraer_dinero(self, cantidad):
        if cantidad > self.__balance:
            print(
                "La cantidad es mayor que tu saldo, por favor revisa tu saldo de nuevo.\n\n")
        else:
            self.__balance -= cantidad
            print("Se ha retirado la cantidad de: {}\nTu saldo ahora es: {}\n\n".format(cantidad,
                                                                                    self.__balance))

    def depositar(self, cantidad):
        self.__balance += cantidad
        print("Tu nuevo saldo es: {}\n\n".format(self.__balance))

    def transferir(self, cantidad, cuenta):
        if cantidad > self.__balance:
            print(
                "Tu saldo es menor que la cantidad a transferir. Por favor revisa tu saldo.\n\n")
        else:
            self.__balance -= cantidad
            print("Se ha transferido la cantidad de {} a la cuenta{} satisfactoriamente.\n\n".format(
                cantidad, cuenta))

    def select_method(self, option):
        if option == 1:
            cantidad = int(input("Ingrese la cantidad a depositar: "))
            self.depositar(cantidad)
            time.sleep(.5)
        
        elif option == 2:
            print("Tu saldo es de: {}\n\n".format(self.saldo))
            time.sleep(.5)
        
        elif option == 3:
            cantidad = int(input("Ingrese la cantidad a retirar: "))
            self.extraer_dinero(cantidad)
            time.sleep(.5)
        
        elif option == 4:
            self.extraer_todo()
            time.sleep(.5)
        
        elif option == 5:
            cantidad = int(input("Ingrese la cantidad a transferir: "))
            cuenta = int(input("Ingrese la cuenta a transferir: "))
            self.transferir(cantidad)
            time.sleep(.5)
        
        elif option == 6:
            print("Tú número de tarjeta es: {}\n\n".format(self.numero_tarjeta))
            time.sleep(.5)

    def menu(self):
        while True:
            menu = """Bienvenido al Banco\n1.-Depositar a cuenta\n2.-Consultar tu saldo\n3.-Retirar\n4.-Retirar todo el dinero\n5.-Transferir a otra cuenta\n6.-Ver número de tarjeta\n7.-Salir\n> """
            option = input(menu)
            option = int(option)
            if option != 7:
                self.select_method(option)
            else:
                break


rod = CuentaBancaria(2500, "Rodrigo", "4152313645658909")
rod.menu()
