class Pizzas():
    
    def __init__(self):
        self.inicio = None

    def Mostrar(self):
        x=1
        temp = self.inicio
        while temp:
            temp.Mostrar(x)

            temp = temp.siguiente
            x+=1
        print('---------------------')

    def aggPizza(self,pizza):
        temp = self.inicio
        if(self.inicio==None):
            self.inicio = pizza
        else:
            while(temp.siguiente!=None):
                temp = temp.siguiente
            temp.siguiente = pizza
        return 
    
    def timeTot(self):
        temp = self.inicio
        time= 0
        
        while(temp !=None):
            if(temp.pepperoni=='y'):
                time+=3
            if(temp.salchicha=='y'):
                time+=4
            if(temp.carne=='y'):
                time+=10
            if(temp.queso=='y'):
                time+=5
            if(temp.piña=='y'):
                time+=2
            temp= temp.siguiente
        return time
