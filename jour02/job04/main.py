class Student:
    def __init__(self, nom, prenom, numero_etudiants, nombre_credits):
        self.__student_nom = nom
        self.__student_prenom = prenom
        self.__student_numero_etudiant = numero_etudiants
        self.__student_nombre_credit = nombre_credits
        self.__student_level = self.__studentEval()
    
    def get_nom(self):
        return self.__student_nom
    
    def get_prenom(self):
        return self.__student_prenom

    def get_numero_etudiant(self):
        return self.__student_numero_etudiant
    
    def get_nombre_credit(self):
        return self.__student_nombre_credit
    
    def get_level(self):
        return self.__student_level

    def set_nom(self, nom): 
        self.__student_nom = nom

    def set_prenom(self, prenom): 
        self.__student_prenom = prenom

    def set_numero_etudiant(self, numero_etudiant): 
        self.__student_numero_etudiant = numero_etudiant

    def set_nombre_credits(self, nombre_credits): 
        self.__student_nombre_credit = nombre_credits
        
    def add_credits(self, rajout_credits):
        if rajout_credits > 0:
            self.__student_nombre_credit += rajout_credits
            self.__student_level = self.__studentEval()
            
    def __studentEval(self):
        if self.get_nombre_credit() >= 90:
            return "Excellent"        
        elif self.get_nombre_credit() >= 80:
            return "Très bien"
        elif self.get_nombre_credit() >= 70:
            return "Bien"
        elif self.get_nombre_credit() >= 60:
            return "Passable"
        elif self.get_nombre_credit() < 60:
            return "Insuffisant"
            
    def student_infos(self):
        print(f"\n Nom = {self.get_nom()}\n Prénom = {self.get_prenom()}\n id = {self.get_numero_etudiant()}\n Niveau = {self.__studentEval()}\n")
                              

# Création d'une instance de la classe Student
info_students = Student("John", "Doe", 145, 0)

# Affichage du nombre de crédits initial
print(f"\nLe nombre de credits de {info_students.get_nom()} {info_students.get_prenom()} est de {info_students.get_nombre_credit()} points")

# Ajout de 10 crédits à 3 reprises
info_students.add_credits(10)
info_students.add_credits(10)
info_students.add_credits(10)

# Affichage du nombre de crédits après l'ajout
print(f"Le nombre de credits de {info_students.get_nom()} {info_students.get_prenom()} est de {info_students.get_nombre_credit()} points")

info_students.add_credits(42)
info_students.student_infos()