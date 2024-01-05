class Personne:
    def __init__(self, age=14):
        self.pers_age = age
        
    def afficherAge(self):
        print(f"L'âge de la personne est {self.pers_age} ans.")
    
    def bonjour(self):
        print("Hello")
    
    def modifierAge(self, nouvelle_age):
        if type(nouvelle_age) == int:
            self.pers_age = nouvelle_age
            print(f"Nouvel âge de la personne : {self.pers_age} ans.")
        else:
            print("Je ne comprends pas votre âge")        

class Eleve(Personne):
    def __init__(self):
        super().__init__(age=14)
        
    def allerEnCours(self):
        print("Je vais en cours")
    
    def afficherAge(self):
        print(f"J'ai {self.pers_age} ans")
        
class Professeur(Personne):
    def __init__(self, matiereEnseignee, age=40):
        super().__init__(age)
        self.prof_matiereEnseignee = matiereEnseignee
        
    def enseigner(self):
        print("Le cours va commencer")
        
    def bonjour(self):
        return super().bonjour()
    
kevin = Personne()
g3 = Eleve()

kevin.bonjour()
g3.allerEnCours()
kevin.modifierAge(15)
kevin.afficherAge()

duBois = Professeur("Histoire-Géo")
duBois.bonjour()
duBois.enseigner()




