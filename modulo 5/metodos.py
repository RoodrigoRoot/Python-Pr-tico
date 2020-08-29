class Galleta:  
    """Clase de Ejemplo para enterder clases y objetos"""
    #Forma
    #Color
    #chispas
    
    def __init__(self, forma, color, chispas):
        self.forma = forma
        self.color = color
        self.chispas = chispas

    def hornear(self):
        print("Las galletas se están horneando")
        
        
chokis = Galleta("Redonda", "cafe", "chocolate")
chokis.hornear()

def saludar():
    print("Saludar")

saludar()