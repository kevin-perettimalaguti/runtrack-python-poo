class Joueur:
    def __init__(self, nom, numero, position, nb_but, passe_decisive, carton_jaune, carton_rouge): 
        self.nom = nom
        self.numero = numero
        self.position = position
        self.nb_but = nb_but
        self.passe_decisive = passe_decisive
        self.carton_jaune = carton_jaune
        self.carton_rouge = carton_rouge
        
    def marquerUnBut(self):
        pass
    
    def effectuerUnePasseDecisive(self):
        pass
    
    def recevoirUnCartonJaune(self):
        pass
    
    def recevoirUnCartonJaune(self):
        pass
    
    def afficherStatistiques(self):
        pass
    
class Equipe:
    def __init__(self, nom, liste_joueur=[]):
        self.nom = nom
        self.liste_joueur = liste_joueur
    
    def ajouterJoueur(self, nouveau_joueur):
        

        
    