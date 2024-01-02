class Personne:    
    def __init__(self,prenom,nom):
        self.nom = nom
        self.prenom = prenom
        
    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}" 
        
        
personne1 = Personne("John","Doe")
print(personne1.SePresenter())

personne2 = Personne("Jean","Dupond")
print(personne2.SePresenter())
      