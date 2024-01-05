class Forme:    
    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):        
        self.largeur = largeur
        self.hauteur = hauteur
        
    def aire(self):
        return self.hauteur * self.largeur
    
forme = Forme()
print(f"L'air de mon rectangle est de: {forme.aire()}")

rect = Rectangle(5, 10)
print(f"L'air de mon rectangle est de: {rect.aire()}")

