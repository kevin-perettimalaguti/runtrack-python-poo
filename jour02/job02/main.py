class Livre:
    def __init__(self,titre,auteur,nb_pages):
        self.__livre_titre = titre
        self.__livre_auteur = auteur
        self.__livre_nb_pages = nb_pages
        
    # Assesseurs
    def get_auteur(self):
        return self.__livre_auteur
    
    def get_titre(self):
        return self.__livre_titre
    
    def get_number_pages(self):
        return self.__livre_nb_pages
    
    # Mutateurs
    def set_auteur(self,auteur):
        self.__livre_auteur = auteur
        
    def set_titre(self,titre):
        self.__livre_titre = titre
        
    def set_number_pages(self, nb_pages):       
        if type(nb_pages) == int and nb_pages > 0:
            self.__livre_nb_pages = nb_pages
        else:
            print("Veuillez corriger votre nombre de page: entrez un nombre entier positif")            
            
                
characteristic_book = Livre("L'étranger","Albert Camus",111)
print (f"\n Le titre du livre: {characteristic_book.get_titre()}\n L'auteur du livre: {characteristic_book.get_auteur()}\n Le nombre de page: {characteristic_book.get_number_pages()}\n\n")

characteristic_book.set_titre("Le Parfum")
characteristic_book.set_auteur("Patrick Suskin")
characteristic_book.set_number_pages(279.26)
print (f"\n Le titre du livre:{characteristic_book.get_titre()}\n L'auteur du livre: {characteristic_book.get_auteur()}\n Le nombre de page: {characteristic_book.get_number_pages()}\n\n")

characteristic_book.set_titre("L'Art de Comptempler")
characteristic_book.set_auteur("Kevin Peretti")
characteristic_book.set_number_pages(-582)
print (f"\n Le titre du livre:{characteristic_book.get_titre()}\n L'auteur du livre: {characteristic_book.get_auteur()}\n Le nombre de page: {characteristic_book.get_number_pages()}\n\n")

