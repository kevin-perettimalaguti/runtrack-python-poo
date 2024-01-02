class Personne:    
    def __init__(self,nom,prenom):
        self.nom = nom
        self.prenom = prenom
        
    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}" 
        
        
personne1 = Personne("Doe","John")
print(personne1.SePresenter())

personne2 = Personne("Dupond","Jean")
print(personne2.SePresenter())
      