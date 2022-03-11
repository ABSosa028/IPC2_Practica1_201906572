import time,os
import graphviz
from PIL import Image

class Ordenes():

    def __init__(self):
        self.cabecera = None
        self.cola = None
    
    def aggOrden(self, orden):
        temp = self.cabecera
        if(temp == None):
            self.cabecera = orden
            self.cola = orden
        else:
            temp = self.cola
            temp.siguiente = orden
            self.cola = orden
            
    def Mostrar(self):
        temp = self.cabecera
        if(self.cabecera == None):
            print('No hay ordenes para mostrar')
        while temp:
            temp.Mostrar()
            temp = temp.siguiente

    def MostrarTit(self):
        temp = self.cabecera
        if(self.cabecera == None):
            print('No hay ordenes para mostrar')
            return
        while temp:
            temp.MostrarTit()
            temp = temp.siguiente
    
    def despachar(self,codigo):
        temp = self.cabecera
        if(temp!=None):
            if(temp.siguiente!=None):
                if(str(temp.id)==str(codigo)):
                    aux = temp
                    tiempoPrep = aux.tiempoEspera
                    hIn = aux.hora
                    ho = hIn.split(' ') 
                    hO = ho[-1].split(':')
                    horaIn = int(hO[0])
                    minIn = int(hO[1])

                    timer = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                    hf = timer.split(' ')
                    hF = hf[-1].split(':')
                    
                    horaFin = int(hF[0])
                    minFin = int(hF[1])
                    if(minFin<minIn):
                        minFin+=60
                        totalTime = int(minFin)-int(minIn)
                    else:
                        totalTime = int(minFin)-int(minIn)+int(tiempoPrep)
                    print('Tiempo total hasta entregar la Orden de cod: '+str(codigo)+ ' Fue de : '+str(totalTime)+' minutos')

                    self.cabecera = aux.siguiente
                    
                    
                    return
                print('/////////////////////////////////////////////////////')
                print('Esta orden aun no se puede despachar, NO ES SU TURNO')
                print('/////////////////////////////////////////////////////')

                """while temp:
                    aux = temp.siguiente
                    if(str(aux.id) == str(codigo)):
                        tiempoPrep = aux.tiempoEspera
                        hIn = aux.hora
                        ho = hIn.split(' ') 
                        hO = ho[-1].split(':')
                        print(hO)

                        timer = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                        hf = timer.split(' ')
                        hF = hf[-1].split(':')
                        print(hF)
                        

                        temp.siguiente = aux.siguiente
                        
                        
                        return
                    temp = temp.siguiente"""
            else:
                aux = temp
                if(str(aux.id) == str(codigo)):
                        tiempoPrep = aux.tiempoEspera
                        hIn = aux.hora
                        ho = hIn.split(' ') 
                        hO = ho[-1].split(':')
                        horaIn = int(hO[0])
                        minIn = int(hO[1])

                        timer = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                        hf = timer.split(' ')
                        hF = hf[-1].split(':')
                        horaFin = int(hF[0])
                        minFin = int(hF[1])
                        if(minFin<minIn):
                            minFin+=60
                            totalTime = int(minFin)-int(minIn)
                        else:
                            totalTime = int(minFin)-int(minIn)+int(tiempoPrep)
                        print('Tiempo total hasta entregar la Orden de cod: '+str(codigo)+ ' Fue de : '+str(totalTime)+' minutos')
                        

                        self.cabecera = None
                        
                        
                        return
            
    def imagen(self):
        archivo = open("cola.dot",'w')
        archivo.write('digraph grid {')
        archivo.write('layout=dot\n labelloc = "t"')
        archivo.write('edge [weight=1000 style=dashed color=dimgrey]\n')
        archivo.write('rankdir="LR"\n')

        temp = self.cabecera
        temp2 = self.cabecera

        while temp != None:
            archivo.write('pedido_'+str(temp.id)+'_cliente_'+str(temp.cliente.nombre)+'\n\n')
            temp = temp.siguiente

        while temp2 != None:
            archivo.write('pedido_'+str(temp2.id)+'_cliente_'+str(temp2.cliente.nombre)+ "->")
            temp2 = temp2.siguiente

        archivo.write("\"None\"\n")

        archivo.write('}')
        archivo.close()
        os.system("dot -Tpng cola.dot -o cola.png")
        im = Image.open("cola.png")
        im.show()
                
