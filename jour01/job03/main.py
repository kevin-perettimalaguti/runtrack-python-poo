class Operation:    
    def __init__(self, nombre1, nombre2):
        self.nb1 = nombre1
        self.nb2 = nombre2
        
    def afficher_nombre(self):
        print(f"Le nombre1 est {self.nb1}")
        print(f"Le nombre2 est {self.nb2}")
        
    def addition(self):
        self.resulat = self.nb1 + self.nb2
        print(self.resulat)
        
ope = Operation(12,3)  
ope.addition()  