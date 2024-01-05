from math import pi

class Forme:    
    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):        
        self.largeur = largeur
        self.hauteur = hauteur
        
    def aire(self):
        return self.hauteur * self.largeur
    
class Cercle(Forme):
    def __init__(self, radius):    
        self.radius = radius
        
    def aire(self):
        return pi * (self.radius * self.radius)
    
rect = Rectangle(6,12)
print(f"L'air du rectangle est de: {rect.aire()}")

cercle = Cercle(15)
print(f"L'air du cercle est de: {cercle.aire():.2f}")



    

        