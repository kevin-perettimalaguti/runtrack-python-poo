class Personne:
    def __init__(self, age=14):
        self.pers_age = age
        
    def afficherAge(self):
        print(f"L'âge de la personne est {self.pers_age} ans.")
    
    def bonjour(self):
        return "Hello"
    
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
        return "Je vais en cours"
    
    def afficherAge(self):
        print(f"J'ai {self.pers_age} ans")
        
class Professeur:
    def __init__(self, matiereEnseignee):
        self.prof_matiereEnseignee = matiereEnseignee
        
    def enseigner(self):
        return "Le cours va commencer"
    
kevin = Personne()
kevin.afficherAge()

g3 = Eleve()
g3.afficherAge()
