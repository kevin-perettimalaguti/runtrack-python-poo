class CompteBancaire:
    def __init__(self, prenom, nom, numero_compte, solde):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_compte = numero_compte
        self.__solde_compte = solde
        self.decouvert = True

    def get_nom_compte(self):
        return self.__nom

    def get_prenom_compte(self):
        return self.__prenom

    def get_numero_compte(self):
        return self.__numero_compte

    def get_solde_compte(self):
        return self.__solde_compte

    def set_nom_compte(self, nouveau_nom):
        self.__nom = nouveau_nom

    def set_prenom_compte(self, nouveau_prenom):
        self.__prenom = nouveau_prenom

    def set_numero_compte(self, nouveau_numero_compte):
        self.__numero_compte = nouveau_numero_compte

    def set_solde_compte(self, nouveau_solde):
        self.__solde_compte = nouveau_solde

    def afficher(self):
        print(f"\nTitulaire de compte : {self.get_prenom_compte()} {self.get_nom_compte()}\nNuméro de compte : {self.get_numero_compte()}\n")

    def afficherSolde(self):
        print(f"Solde du compte : {self.get_solde_compte()}€\n")

    def versement(self, montant_versement):
        self.__solde_compte += montant_versement

    def retrait(self, montant_retrait):
        if self.__solde_compte >= montant_retrait:
            self.set_solde_compte(self.__solde_compte - montant_retrait)
            return True
        else:
            print("Vous n'avez pas les fonds pour faire ce retrait")
            self.agios()
            return False

    def agios(self):
        if self.__solde_compte < 0:
            self.__solde_compte -= 5

    def virement(self, montant_virement, destinataire_virement):
        if self.retrait(montant_virement):
            destinataire_virement.versement(montant_virement)
            print("Votre virement à bien été effectué")
        else:
            print("Votre virement n'a pas fonctionné")


compte_vanny = CompteBancaire("Vanny", "LaMorte", 696877, 35000)
compte_vanny.afficher()

compte_vanny.versement(10000)
compte_vanny.afficherSolde()

compte_vanny.retrait(20000)
compte_vanny.afficherSolde()

compte_vanny.retrait(50000)
compte_vanny.afficherSolde()

compte_kevin = CompteBancaire("Kevin", "Peretti-Malaguti", 564875, -500)
compte_kevin.afficher()
compte_kevin.afficherSolde()

compte_vanny.virement(500, compte_kevin)

compte_kevin.afficherSolde()
