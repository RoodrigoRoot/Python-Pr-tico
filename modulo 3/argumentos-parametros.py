#Parametro->Son los valores que se reciben, cuando se está definiendo una función.

def suma_dos_numeros(valor1=10, valor2=20):#Parámetros por defecto, son aquellos que ya tienen un valor asignado, en dado caso que no se le pasen argumentos al momento de llamar la función.
    """Función con dos paráetros"""
    resultado = valor1 + valor2
    print(resultado)

#Argumento->Son los valores que se envían a la función cuando esta se mande a llamar.

#suma_dos_numeros()#Llamada de la función con dos argumentos que son 10 y 20.

def restar_dos_numeros(valor1, valor2):
    """Función que resta dos número utilizando dos parámetros"""
    resultado = valor1 - valor2
    print(resultado)

restar_dos_numeros(valor2=40, valor1=10)#Llamada de la función, utilizando argumentos por nombre. Al usar argumentos por nombre no importa el orden en que están los parametros, ya que estoy asignando directamente sus valores.