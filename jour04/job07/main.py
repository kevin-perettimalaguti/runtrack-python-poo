# import ramdom

class Carte:
    def __init__(self, valeur, couleur):
        self.carte_valeur = valeur
        self.carte_couleur = couleur
        
    def carte_chiffre(self, chiffre):   
        if 2 <= chiffre <= 10 and type(chiffre) == int:
            self.carte_valeur = chiffre
            print(f"J'ai eu un {self.carte_valeur} {self.carte_couleur}")           
            
    def carte_figure(self):
        self.carte_valeur = 10
        print(f"Je suis tombée sur une figure, je remporte: {self.carte_valeur} points")        
        
    def carte_as(self, jouer_unAs):
        if jouer_unAs == 1:
            self.carte_valeur = 1
            print(f"Mon As aura la valeur: {self.carte_valeur} points")
        elif jouer_unAs == 11:
            self.carte_valeur = 11
            print(f"Mon As aura la valeur: {self.carte_valeur} points")
               
            
class Jeu(Carte):
    def __init__(self, valeur, couleur):
        super().__init__(valeur, couleur)
        self.liste_paquet = []        
        
    def ajouter_carteAlaMain(self, nouvelle_pioche):
        self.liste_main = []
        self.liste_main.append(nouvelle_pioche)        
        
class Joueur():
    def __init__(self, nom, statut, nb_points): 
        self.joueur_nom = nom
        self.statut = statut
        self.nb_points = nb_points
        self.carte_en_main = {}

    def AfficherInfo(self): 
        print(f"\nNom du joeur : {self.joueur_nom}\nStatut du joueur :  {self.statut}\nNombre de point : {self.nb_points}\nCarte en main : {self.carte_en_main}\n")
        
    def recevoir_carte(self, pioche):
        self.carte_en_main.append(pioche)
        
        
    def refuser_carte(self):
        pass
    
    def objectif_pointsJoueur(self):
        pass           
            
    def objectif_pointsCroupier(self):
        pass
    
    
    


    