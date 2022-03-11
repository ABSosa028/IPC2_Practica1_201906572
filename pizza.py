class Pizza():

    def __init__(self,pepperoni,salchicha,carne, queso,piña):
        self.pepperoni = pepperoni
        self.salchicha = salchicha
        self.carne = carne
        self.queso = queso
        self.piña = piña
        self.siguiente = None

    def Mostrar(self, NoPizza):
        print("---------------------")
        print("Pizza #"+str(NoPizza)+" Ingredientes:        ")
        if(self.pepperoni=='y'):
            print('+  Pepperoni')
        if(self.salchicha=='y'):
            print('+  Salchicha')
        if(self.carne=='y'):
            print('+  Carne')
        if(self.queso=='y'):
            print('+  Queso')
        if(self.piña=='y'):
            print('+  Piña')

            
        
        



