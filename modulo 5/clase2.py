class Galleta:  
    """Clase de Ejemplo para enterder clases y objetos"""
    #Forma
    #Color
    #chispas
    forma = "Estrella"
    
    def __init__(self, forma, color, chispas):
        self.forma = forma
        self.color = color
        self.chispas = chispas

    def hornear(self):
        print("Las galletas se están horneando")
    
    def crear_galletas(self):
        self.forma
        self.color
        self.chispas

chokis = Galleta("Estrella", "Amarilla", "Chocolate")
print("chokis ->",chokis.forma)
print("chokis ->",chokis.color)
print("chokis ->",chokis.chispas)
chokis.hornear()

maria = Galleta("Redonda", "Beige", "Ninguna")
print("maria ->",maria.forma)
print("maria ->",maria.color)
print("maria ->",maria.chispas)
maria.hornear()

