class Personnage:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1
        print(f"x va en direction de la gauche : {self.x}")

    def droite(self):
        self.x += 1
        print(f"x va en direction de la droite : {self.x}")

    def haut(self):
        self.y -= 1
        print(f"y va en direction du haut : {self.y}")

    def bas(self):
        self.y += 1
        print(f"x va en direction du bas : {self.y}")

    def position(self):        
        pos_tuple = (self.y,self.y)
        print(f" Ma position actuelle {pos_tuple}")
        

# Création de l'instance de Personnage avec la plateau en paramtre
personnage_position = Personnage(10,10)
personnage_position.position()

# Aller à gauche et afficher en format tuple
personnage_gauche = Personnage(-5,10)
personnage_gauche.gauche()

# Aller à droite et afficher en format tuple
personnage_droite = Personnage(8,20)
personnage_droite.droite()

# Aller à haut et afficher en format tuple
personnage_haut = Personnage(10,5)
personnage_haut.haut()

# Aller à bas et afficher en format tuple
personnage_bas = Personnage(10,-2)
personnage_bas.bas()
