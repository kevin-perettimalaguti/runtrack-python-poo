class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description_tache = description
        self.statut = statut
        
class ListeDeTaches:
    def __init__(self):
        self.liste_taches = []
                
    def ajouterTache(self, nouvelle_tache):
        self.liste_taches.append(nouvelle_tache)        
        
    def supprimerTache(self, suppression_tache):
        self.liste_taches.remove(suppression_tache)
        
    def marquerCommeFinie(self, tache_finie):
        for tache in self.liste_taches:
            if tache.titre == tache_finie:
                tache.statut = "Terminée"
                return tache.statut
                
    def afficherListe(self):
        for tache in self.liste_taches:
            print(f"{tache.titre}({tache.statut})")
        
    def filtrer_liste(self, statut_filtrage):
        liste_filtree = []
        for tache in self.liste_taches:
            if tache.statut == statut_filtrage:
                liste_filtree.append(tache)
            self.liste_taches = liste_filtree

        

liste = ListeDeTaches()
tache1 = Tache("Manger", "Prendre un bon repas")
tache2 = Tache("Python avec Vanny ce soir", "Learn together")
tache3 = Tache("Appeler Vanny", "Se parler")
tache4 = Tache("Jouer", "Profiter d'un moment de détente")

liste.ajouterTache(tache1)
liste.ajouterTache(tache2)
liste.ajouterTache(tache3)
liste.ajouterTache(tache4)

print("\nListe de taches initial : \n")
liste.afficherListe()

liste.supprimerTache(tache4)

print("\nSuppression de la tache 'Jouer': \n")
liste.afficherListe()

print("\nListe mis a jour : \n")
liste.marquerCommeFinie("Appeler Vanny")
liste.marquerCommeFinie("Manger")
liste.afficherListe()

print("\nMa liste de tache(s) terminée(s) : \n")
liste.filtrer_liste("Terminée")
liste.afficherListe()
