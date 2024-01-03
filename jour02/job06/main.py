class Commande:
    def __init__(self, numero_commande): 
        self.__num_commande = numero_commande
        self.__list_plat = []
        self.__statut_commande = "en cours"
    
    def get_num_commande(self):
        return self.__num_commande
    
    def get_list_plat(self):
        return self.__list_plat
    
    def get_statut_commande(self): 
        return self.__statut_commande
    
    def set_num_commande(self, num_commande):
        self.__num_commande = num_commande

    def set_plat_commande(self, plat_commande):
        self.__list_plat = plat_commande

    def set_statut_commande(self, statut_commande): 
        self.__statut_commande = statut_commande

    def ajouter_plat_a_la_commande(self, nom_plat, prix, statut="en cours"):
        self.__list_plat.append({"nom": nom_plat, "prix": prix, "statut": statut})
        self.__statut_commande = "en cours"

    def annuler_la_commande(self):
        self.__statut_commande = "annulée"        
        print(f"\nLa commande a été annulée, Statut: {self.get_statut_commande()}\n")
        

    def __calculer_total_commande(self):
        total = 0
        for plat in self.__list_plat:
            total += plat["prix"]
        return total
    
    def calculer_tva(self, taux_tva=0.2):
        total = self.__calculer_total_commande()
        tva = total * taux_tva
        return tva
    
    def afficher_commande(self):
        print(f"Numéro de commande : {self.__num_commande}")
        print("Plats commandés:")
        for plat in self.__list_plat:
            print(f"- {plat['nom']}: {plat['prix']} € ({plat['statut']})")
        print(f"Total à payer : {self.__calculer_total_commande()} €")
        print(f"TVA à payer : {commande1.calculer_tva():.2f} €")

    
# Ma première commande    
commande1 = Commande(52)
commande1.ajouter_plat_a_la_commande("Gyoza", 6)
commande1.ajouter_plat_a_la_commande("Hamburger", 13)
commande1.ajouter_plat_a_la_commande("Pâte carbonara", 9)

commande1.afficher_commande()

commande1.annuler_la_commande()

commande1.afficher_commande()

