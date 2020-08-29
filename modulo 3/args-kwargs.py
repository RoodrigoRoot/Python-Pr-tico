
def sumar(*args):
    resultado = 0
    for numero in args:
        resultado += numero
    print(resultado)
    
sumar(459, 120, 600, 160)

def introduce_self_me(**kwargs):
    presentation = "Hola, soy {}.\n Actualmente tengo {} años,\n mi nombre de usuario es: {} y vivo en {}".format(kwargs.get("name"),
                                kwargs.get("age"),
                                kwargs.get("username"),
                                kwargs.get("city"))
    print(presentation)

introduce_self_me(name="rodrigo", username="roodrigo", age=24, city="Guadalajara")


