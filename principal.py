from ordenes import Ordenes as SP
import time
from pizzas import Pizzas as Ps
from pizza import Pizza as P
from ordenes import Ordenes as Or
from orden import Orden as O
from cliente import Cliente as C

class Principal():

        
    rec_or = 1
    Ordenes =  Or()
    

    def sigOr():
        this = Principal.rec_or+1
        Principal.rec_or = this 

    def hW():
        print('Hello World')

    def menu():
        dentro = True
        while dentro:
            print('===============================')
            print("             MENU")
            print('===============================')
            print('  1.   Tomar Orden')
            print('  2.   Ver Ordenes')
            print('  3.   Despachar Orden')
            print('  4.   Info')
            print('  5.   Salir')
            print('')
            print('Seleccione una opcion')
            op = input('')
            if(op == '1'):
                Principal.news_Orders()
            if(op == '2'):
                Principal.verOrdenes()
            if(op == '3'):
                Principal.despachar()
            if(op == '4'):
                Principal.Info()
            if(op == '5'):
                print('Chayito')
                dentro = False

    def verOrdenes():
        Principal.Ordenes.Mostrar()

    def news_Orders():
        notexit = True
        while notexit:
            notexit = Principal.nuevaOrden()
    
    def nuevaOrden():
        print('obtencion de datos del cliente para la orden, llene todos los campos')
        name=input('Nombre Cliente: ')
        phone=input('Telefono Cliente: ')
        location=input('Direccion Cliente: ')
        cl = C(name,phone,location)
        timer = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        Pizzas = Ps()
        print('Pedido del cliente, llene todos los campos') 
        morePizza =True

        while morePizza:
            print('seleccion de ingredientes para las pizza   y/n: ')
            pepp=input('Pepperoni?: ')
            salc=input('Salchicha?: ')
            carn=input('Carne?: ')
            ches=input('Queso?: ')
            piña=input('Piña: ')
            masIguales = input('mas pizzas iguales?       y/n: ')
            Pizza = P(pepp, salc,carn,ches,piña)
            if masIguales=='y':
                cantidad = input('cuantas pizzas iguales?: ')
                x=0
                while x < int(cantidad):
                    Pizzas.aggPizza(Pizza)
                    Pizza = P(pepp, salc,carn,ches,piña)

                    #Pizzas.Mostrar()
                    x+=1
            else:
                Pizzas.aggPizza(Pizza)
            op = input('otra pizza ?   y/n: ')
            if(op == 'y'):
                print('new pizza')
            else:
                morePizza = False
                taim = Pizzas.timeTot()
                Orden = O(Principal.rec_or,timer,cl,Pizzas,taim)
                Principal.Ordenes.aggOrden(Orden)
                Principal.sigOr()
                print('Orden tomada correctamente')
                print('')
                print('')
                print('')
                print('')
                other=input('desea tomar una nueva orden?  y/n:  ')
                if(other != 'y'):
                    Principal.Ordenes.imagen()
                    return False
                    
                else: 
                    Principal.Ordenes.imagen()
                    return True
        return
    
    def despachar():
        print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
        print('°              Ordenes Activas              °')
        print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
        Principal.Ordenes.MostrarTit()
        Principal.Ordenes.imagen()

        desp= input('Ingrese el codigo de la Orden que será Despachada:    ')
        Principal.Ordenes.despachar(str(desp))
    
    def Info():
        #print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
        print('')
        print('')

        print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
        print('°    Estudiante:  Allan Ricardo Barillas Sosa   °')
        print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
        print('°        Carnet:  201906572                     °')
        print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
        print('°        Correo:  allanbarillass@gmail.com      °')
        print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
        print('')
        print('')

       # print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')