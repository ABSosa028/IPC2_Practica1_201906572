from numpy import prod


class Orden():
    def __init__(self,id,hora,cliente,productos, tiempoEspera):
        self.id = id
        self.hora = hora
        self.cliente = cliente
        self.productos = productos
        self.tiempoEspera = tiempoEspera
        self.siguiente = None

    def Mostrar(self):
        print('===================================')
        print(' Orden No. '+str(self.id)+'  hora: '+str(self.hora))
        self.cliente.Mostrar()
        print('------------------------')
        print('Productos de la orden')
        print('------------------------')
        self.productos.Mostrar()
        print('tiempo de Preparacion: '+str(self.tiempoEspera))
        print('===================================')

    def MostrarTit(self):
        print('=============================================')
        print(' Orden No. '+str(self.id)+'  hora: '+str(self.hora))
        print('=============================================')
