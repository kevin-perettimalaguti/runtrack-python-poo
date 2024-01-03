class Voiture:
    def __init__(self,marque,modele,annee,kilometrage):
        self.__car_marque = marque
        self.__car_modele = modele
        self.__car_annee = annee
        self.__car_kilometrage = kilometrage
        self.car_en_marche = False
        self.__reservoir = 50
        
    def get_marque(self):
        return self.__car_marque
    
    def get_modele(self):
        return self.__car_modele
    
    def get_annee(self):
        return self.__car_annee
    
    def get_kilometrage(self):
        return self.__car_kilometrage
    
    def get_reservoir(self):
        return self.__reservoir
    
    def set_marque(self,marque):
        self.__car_marque = marque
    
    def set_modele(self,modele):
        self.__car_modele = modele
    
    def set_annee(self,annee):
        self.__car_annee = annee
    
    def et_kilometrage(self,kilometrage):
        self.__car_kilometrage = kilometrage
        
    def set_reservoir(self,reservoir):
        self.__reservoir = reservoir
        
    def demarrer(self):
        if self.__verifier_plein() > 5:
            print("La voiture peut demarrer")
            self.car_en_marche = True
        else:
            print("La voiture n'a pas assez de carburants")        
        
    def arreter(self):
        self.car_en_marche = False
        print("La voiture freine est s'arrête")
        
    def __verifier_plein(self):
        return self.get_reservoir()
    
car = Voiture("Porshe","GT3 RS",2011, 93254)

print (f"\n La marque : {car.get_marque()}\n Le modèle : {car.get_modele()}\n L'année de sortie : {car.get_annee()}\n Son kilometrage : {car.get_kilometrage()}")

car.demarrer()
car.arreter()
car.set_reservoir(5)
car.demarrer()



            
    
    