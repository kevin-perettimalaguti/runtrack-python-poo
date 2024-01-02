class Operation:        
    def __init__(self, nombre1, nombre2):
        self.nb1 = nombre1
        self.nb2 = nombre2
        
    def afficher_nombre(self):
        print(f"Le nombre1 est {self.nb1}")
        print(f"Le nombre2 est {self.nb2}")
        
ope = Operation(12,3)  
ope.afficher_nombre()     

