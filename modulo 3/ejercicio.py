
def sumar(valor1=1, valor2=1):
    resultado = valor1 + valor2
    print(resultado)

def restar(valor1=1, valor2=1):
    resultado = valor1 - valor2
    print(resultado)

def multiplicar(valor1=1, valor2=1):
    resultado = valor1 * valor2
    print(resultado)

def dividir(valor1=1, valor2=1):
    resultado = valor1 / valor2
    print(resultado)

def seleccion_funcion(opcion):
    funciones = {"1":sumar, "2":restar, "3":dividir, "4":multiplicar}
    funcion = funciones.get(opcion)
    funcion()
    


def menu():
    menu = """Bienvenido\nEscoge una opción:\n1.-Suma\n2.-Resta\n3.-Dividir\n4.-Multiplicar\nIngresa una opción: """
    opcion = input(menu)
    seleccion_funcion(opcion)


menu()

