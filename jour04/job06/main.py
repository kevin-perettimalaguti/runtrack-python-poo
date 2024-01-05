class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee 
        self.prix = prix
        
    def informationsVehicule(self):
        print(f"\nMarque: {self.marque}\nModèle: {self.modele}\nAnnée: {self.annee}\nPrix: {self.prix}\n")
        
    def demarrer(self):
        print("Attention, je roule")
    
class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4
        
    def informationsVehicule(self):
        print(f"\nMarque: {self.marque}\nModèle: {self.modele}\nAnnée: {self.annee}\nPrix: {self.prix}\nNombre de porte: {self.portes}\n")
        
    def demarrer(self):
        print("Ma voiture demmare et va rouler")
    
mercedes = Voiture("Mercedes", "Classe A", 2020, 18500)
mercedes.informationsVehicule()

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roues = 2
        
    def informationsVehicule(self):
        print(f"\nMarque: {self.marque}\nModèle: {self.modele}\nAnnée: {self.annee}\nPrix: {self.prix}\nNombre de porte: {self.roues}\n")
        
    def demarrer(self):
        print("Ma moto va demarrer est cabré, ecarter vous !\n")
    
yamaha = Moto("Yamaha", "1200 Vmax", 1987, 4500)
yamaha.informationsVehicule()

mercedes.demarrer()
yamaha.demarrer()


        