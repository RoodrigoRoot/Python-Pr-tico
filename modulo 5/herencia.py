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
        self.tematica = tematica

    def __str__(self):
        return "Galleta con tematica de {} con chispas de {}".format(self.tematica, self.chispas)

navidad = Tematica("Arbol", "cafe con verde", "Chocolate", "Navidad")
navidad.hornear()
print(navidad)
print(navidad.forma)
print(navidad.color)
print(navidad.tematica)

