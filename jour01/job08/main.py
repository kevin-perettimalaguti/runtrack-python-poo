# Importation du module math pour recuperer PI
import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
        
    def changerRayon(self):        
        self.rayon = int(input("Saisissez une nouvelle valeur pour le rayon : "))
    
    def diametre(self):
        return self.rayon * 2
        
    def aire(self):
        return math.pi * (self.rayon * self.rayon)
        
    def circonference(self):
        return self.diametre() * math.pi
    
    def afficherInfos(self):
        return f"\nLes infos de mon Cercle:\nRayon: {self.rayon}\nDiamètre: {self.diametre()}\nCirconférence: {self.circonference()}\nAire: {self.aire()}\n"


# Création du premier cercle    
cercle1 = Cercle(4)
print(cercle1.afficherInfos())

cercle2 = Cercle(7)
print(cercle2.afficherInfos())



