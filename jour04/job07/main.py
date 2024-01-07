import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

class Jeu(Carte): 
    def __init__(self):
        super().__init__(None, None)
        self.paquet = self.creer_paquet()

    def creer_paquet(self):
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        couleurs = ['Cœur', 'Carreau', 'Trèfle', 'Pique']
        paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        random.shuffle(paquet)
        return paquet

    def distribuer_cartes(self):
        return [self.paquet.pop(), self.paquet.pop()]

    def calculer_total(self, main):
        total = 0
        as_count = 0

        for carte in main:
            if carte.valeur in ['Valet', 'Dame', 'Roi']:
                total += 10
            elif carte.valeur == 'As':
                as_count += 1
            else:
                total += int(carte.valeur)

        for _ in range(as_count):
            if total + 11 <= 21:
                total += 11
            else:
                total += 1

        return total

    def joueur_gagne(self, total_joueur, total_croupier):
        return (total_joueur <= 21 and (total_croupier > 21 or total_joueur > total_croupier))

    def jouer_partie(self):
        main_joueur = self.distribuer_cartes()
        main_croupier = self.distribuer_cartes()

        while True:
            print(f"Main du joueur: {[str(carte) for carte in main_joueur]}, Total: {self.calculer_total(main_joueur)}")
            choix = input("Voulez-vous prendre une carte ? (Oui/Non): ")

            if choix.lower() == 'oui':
                main_joueur.append(self.paquet.pop())
                if self.calculer_total(main_joueur) > 21:
                    print("Vous avez dépassé 21. Vous avez perdu.")
                    return
            else:
                break

        while self.calculer_total(main_croupier) < 17:
            main_croupier.append(self.paquet.pop())

        print(f"\nMain du joueur: {[str(carte) for carte in main_joueur]}, Total: {self.calculer_total(main_joueur)}")
        print(f"Main du croupier: {[str(carte) for carte in main_croupier]}, Total: {self.calculer_total(main_croupier)}")

        if self.joueur_gagne(self.calculer_total(main_joueur), self.calculer_total(main_croupier)):
            print("Vous avez gagné!")
        else:
            print("Le croupier a gagné.")

# Exemple d'utilisation
jeu = Jeu()
jeu.jouer_partie()
