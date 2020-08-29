class Galleta:  
    """Clase de Ejemplo para enterder clases y objetos"""
    
    def __init__(self, forma, color, chispas):
        self.forma = forma
        self.color = color
        self.chispas = chispas
        
    def hornear(self):
        print("Las galletas se están horneando")
        
        
chokis = Galleta("Redonda", "cafe", "chocolate")

class Tematica(Galleta):
    
    def __init__(self, forma, color, chispas, tematica):
        super().__init__(forma, color, chispas)
        self.__tematica = tematica

    def __get_tematica(self):
        return self.__tematica
    
    def __set_tematica(self, new_value):
        self.__tematica = new_value
    
    tematica = property(__get_tematica, __set_tematica)

    def __str__(self):
        return "Galleta con tematica de {} con chispas de {}".format(self.tematica, self.chispas)

navidad = Tematica("Arbol", "cafe con verde", "Chocolate", "Navidad")

print("Valor viejo:", navidad.tematica)
value = input("Nueva tematica?")
navidad.tematica = value
print("Valor nuevo:", navidad.tematica)

