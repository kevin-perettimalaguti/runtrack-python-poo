class Animal:
    def __init__(self,age,prenom):
        self.age = age
        self.prenom = prenom
        
    def appel_age(self):
        print(f"L'age de l'animal {self.age} ans")
        
    def veillir(self):
        self.age =+ 1
    
    def nommer(self,prenom):
        self.prenom = prenom
        print(f"L'animal se nomme {self.prenom}")


# Création de l'instance d'Animal
pet = Animal(0, None)

#L'age de depart
pet.appel_age()
# Age de l'animal apres l'appel de la methode viellir
pet.veillir()
#Son nouvelle age
pet.appel_age()
pet.nommer("Corvet")