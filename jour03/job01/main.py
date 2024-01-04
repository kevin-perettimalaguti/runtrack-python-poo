class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom_ville = nom
        self.__nombre_habitant_ville = nombre_habitants
        
    def get_nom_ville(self):
        return self.__nom_ville
    
    def get_nombre_habitant(self):
        return self.__nombre_habitant_ville
    
    def set_nom_ville(self, nouveau_nom):
        self.__nom_ville = nouveau_nom
        
    def set_nombre_habitants(self, nouveau_nombre_habitants):
        self.__nombre_habitant_ville = nouveau_nombre_habitants
        
class Personne:
    def __init__(self, nom, age, objet_ville):
        self.__people_nom = nom
        self.__people_age = age
        self.__people_objet = objet_ville
        
    def get_people_nom(self):
        return self.__people_nom
    
    def get_people_age(self):
        return self.__people_age
    
    def get_people_objet(self):
        return self.__people_objet
    
    def set_people_nom(self, nouveau_nom_personne):
        self.__people_objet = nouveau_nom_personne
    
    def set_people_age(self, nouvelle_age_personne):
        self.__people_objet = nouvelle_age_personne
    
    def set_people_objet(self, nouvelle_objet):
        self.__people_objet = nouvelle_objet
        
    def ajouterPopulation(self):
        population = self.__people_objet.get_nombre_habitant()
        self.__people_objet.set_nombre_habitants(population + 1)
        
        
paris = Ville("Paris", 1000000)
print(f"Population de la ville de {paris.get_nom_ville()} : {paris.get_nombre_habitant()} habitants")

marseille = Ville("Marseille", 861635)
print(f"Population de la ville de {marseille.get_nom_ville()} : {marseille.get_nombre_habitant()} habitants")

john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()

print(f"Mis à jour de la population de la ville de {paris.get_nom_ville()} : {paris.get_nombre_habitant()} habitants")
print(f"Mis à jour de la population de la ville de {marseille.get_nom_ville()} : {marseille.get_nombre_habitant()} habitants")
