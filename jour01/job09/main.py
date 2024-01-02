class Produit:
    def __init__(self,nom,prixHT,TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
        
    def calculerPrixTTC(self):
        return self.prixHT + (self.prixHT*self.TVA)
    
    def modifier_nom(self):
        self.nom = input("Renommer votre objet : ")
        
    def modifier_prix(self):
        self.prixHT = input("Modifier votre prix : ")
        
    def afficher_nom(self):
        return self.nom
    
    def afficher_prixHT(self):
        return self.prixHT
    
    def afficher_prixTTC(self):
        return self.calculerPrixTTC()
    
    def afficher(self):
        return f"\n{self.afficher_nom()}:\nPrix: {self.afficher_prixHT()}\nPrixTTC: {self.afficher_prixTTC()}\n"


table = Produit("Table",18,0.2)
print(table.afficher())

tv = Produit("Télévision",340,0.2)
print(tv.afficher())

chambre_hotel = Produit("1 Nuit d'Hotel",84.99,0.1)
print(chambre_hotel.afficher())

sachet_de_pate = Produit("Pâte 1kg",1.25,0.055)
print(sachet_de_pate.afficher())

doliprane = Produit("Doliprane",2.18,0.021)
print(doliprane.afficher())


