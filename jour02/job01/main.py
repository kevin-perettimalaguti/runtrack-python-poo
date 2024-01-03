class Rectangle:
    def __init__(self,longueur,largeur):
        self.__rect_long = longueur
        self.__rect_larg = largeur
    
    # Assesseurs   
    def get_longueur(self):
        return self.__rect_long
    
    def get_largeur(self):
        return self.__rect_larg
    
    # Mutateurs
    def set_longueur(self, longueur):
         self.__rect_long = longueur

    def set_largeur(self, largeur):
         self.__rect_larg = largeur
        
# Création avec les valeur de base        
rectangle = Rectangle(10,5)

# Affichage des valeurs initiales
print("Longueur initiale:", rectangle.get_longueur())
print("Largeur initiale:", rectangle.get_largeur())

# Modification des valeurs
rectangle.set_longueur(15)
rectangle.set_largeur(8)

# Affichage des valeurs modifiées
print("Longueur modifiée:", rectangle.get_longueur())
print("Largeur modifiée:", rectangle.get_largeur())

        