class Joueur:
    def __init__(self, nom, numero, position): 
        # Initialisation des attributs du joueur
        self.nom = nom
        self.numero = numero
        self.position = position
        self.nb_but = 0
        self.passe_decisive = 0
        self.carton_jaune = 0
        self.carton_rouge = 0
        
    def marquerUnBut(self):
        # Méthode pour incrémenter le nombre de buts
        self.nb_but += 1 
    
    def effectuerUnePasseDecisive(self):
        # Méthode pour incrémenter le nombre de passes décisives
        self.passe_decisive += 1
    
    def recevoirUnCartonJaune(self):
        # Méthode pour incrémenter le nombre de cartons jaunes
        self.carton_jaune += 1
    
    def recevoirUnCartonRouge(self):
        # Méthode pour incrémenter le nombre de cartons rouges
        self.carton_rouge += 1
    
    def afficherStatistiques(self):
        # Méthode pour afficher les statistiques du joueur
        print(f"\nStatistique de {self.nom} {self.numero} :\n Poste: {self.position} Buts marqués: {self.nb_but} Passe décisives: {self.passe_decisive} Nombre de carton jaune: {self.carton_jaune} Nombre de carton rouge: {self.carton_rouge}")

# Création d'une instance de joueur avec des informations spécifiques
info_joueur = Joueur("Kevin", 21, "Attaquant")

# Affichage des statistiques initiales
info_joueur.afficherStatistiques()

# Simulation d'un match
info_joueur.marquerUnBut()
info_joueur.afficherStatistiques()

info_joueur.effectuerUnePasseDecisive()
info_joueur.afficherStatistiques()

info_joueur.recevoirUnCartonJaune()
info_joueur.afficherStatistiques()

info_joueur.recevoirUnCartonRouge()
info_joueur.afficherStatistiques()

                
class Equipe:
    def __init__(self, nom_equipe):
        # Initialisation de l'équipe avec un nom
        self.nom_equipe = nom_equipe
        self.liste_joueurs = []
    
    def ajouterJoueur(self, nouveau_joueur):
        # Méthode pour ajouter un joueur à l'équipe
        self.liste_joueurs.append(nouveau_joueur)
    
    def afficherStatistiquesJoueurs(self):
        # Méthode pour afficher les statistiques de tous les joueurs de l'équipe
        print(f"Statistiques des joueurs de l'équipe {self.nom_equipe}:")
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom_joueur, buts=0, passes=0, cartons_jaunes=0, cartons_rouges=0):
        # Méthode pour mettre à jour les statistiques d'un joueur spécifique
        for joueur in self.liste_joueurs:
            if joueur.nom == nom_joueur:
                joueur.nb_but += buts
                joueur.passe_decisive += passes
                joueur.carton_jaune += cartons_jaunes
                joueur.carton_rouge += cartons_rouges
                
# Création des joueurs
vanny = Joueur("Vanny", 25, "Buteuse")
ines = Joueur("Ines", 6, "Milieu Gauche")
lucy = Joueur("Lucy", 14, "Defenseuse")
carlie = Joueur("Carlie", 9, "Attaquante")

# Création des équipes
liverpool = Equipe("Liverpool")
manchester = Equipe("Manchester")

# Ajout des joueurs aux équipes
liverpool.ajouterJoueur(vanny)
liverpool.ajouterJoueur(ines)
manchester.ajouterJoueur(lucy)
manchester.ajouterJoueur(carlie)

# Affichage des statistiques avant le match
print("\nStatistiques avant le match:")
print("\nEquipe de Liverpool:\n")
liverpool.afficherStatistiquesJoueurs()
print("\nEquipe de Manchester City:\n")
manchester.afficherStatistiquesJoueurs()

# Simulation d'un match
vanny.marquerUnBut()
lucy.recevoirUnCartonRouge()

# Affichage des statistiques après le match
print("\nStatistiques après le match:")
print("\nEquipe de Liverpool:\n")
liverpool.afficherStatistiquesJoueurs()
print("\nEquipe de Manchester City:\n")
manchester.afficherStatistiquesJoueurs()
