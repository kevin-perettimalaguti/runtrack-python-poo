class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur
        
    def set_largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur
    
    def perimetre(self): 
        return 2 * (self.get_longueur() + self.get_largeur())  
    
    def surface(self):
        return self.get_longueur() * self.get_largeur()
    
class Parallepepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur
        
    def volume(self):
        return self.hauteur * self.get_largeur() * self.get_longueur()
            
    
rect = Rectangle(4, 5)
print(f"Le Périmètre est de: {rect.perimetre()}")
print(f"La Surface est de: {rect.surface()}") 

para = Parallepepipede(12, 8, 6)
print(f"Le Volume est de: {para.volume()}")
 
