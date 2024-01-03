class Livre:
    def __init__(self, titre, auteur, nb_pages, disponible):
        self.__livre_titre = titre
        self.__livre_auteur = auteur
        self.__livre_nb_pages = nb_pages
        self.__livre_dispo = disponible
        
    # Assesseurs
    def get_auteur(self):
        return self.__livre_auteur
    
    def get_titre(self):
        return self.__livre_titre
    
    def get_number_pages(self):
        return self.__livre_nb_pages
    
    def get_dispo(self):
        return self.__livre_dispo
    
    # Vérification de la disponibité du livre
    def verification_dispo(self):
        if self.__livre_dispo:
            print("Ce livre est disponible")            
        else:
            print("Ce livre n'est pas disponible")
            
    
    # Fonction pour emprunter le livre
    def emprunter(self):
        if self.__livre_dispo:
            self.__livre_dispo = False
            print("Le livre a bien été emprunté !")            
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")
            
    
    # Fonction pour rendre le livre
    def rendre(self):
        if not self.__livre_dispo:
            self.__livre_dispo = True
            print("Le livre a été rendu avec succès !")            
        else:
            print("Le livre est déjà disponible.")            

# Initialisation du livre choisit
characteristic_book = Livre("L'étranger", "Albert Camus", 111, True)
characteristic_book.verification_dispo()

# On emprunt le livre
characteristic_book.emprunter()
characteristic_book.verification_dispo()

# On rend le livre 
characteristic_book.rendre()
characteristic_book.verification_dispo()




