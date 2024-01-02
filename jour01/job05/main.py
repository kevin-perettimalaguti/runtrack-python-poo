class Point:    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def afficherLesPoints(self):
        print(f"X a pour coordonnée {self.x} et Y a pour coordonnée {self.y}")
        
    def afficherX_et_afficherY(self):
        print(f"x = {self.x}")
        print(f"y = {self.y}")
        
    def changerX_et_changerY(self):
        self.x = int(input("Nouvelle valeur pour X : "))
        self.y = int(input("Nouvelle valeur pour Y : "))

# Instance de la classe Point
point = Point(5, 10)

# Afficher les points initiaux
print("Avant modification :")
point.afficherLesPoints()
point.afficherX_et_afficherY()

# Modifier les valeurs de x et de y
point.changerX_et_changerY()

# Afficher les points après modification
print("Après modification :")
point.afficherLesPoints()
point.afficherX_et_afficherY()
