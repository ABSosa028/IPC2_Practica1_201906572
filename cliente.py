class Cliente():
    
    def __init__(self,nombre, telefono, domicilio):
        self.nombre = nombre
        self.telefono = telefono
        self.domicilio = domicilio


    def Mostrar(self):
        print('cliente: '+str(self.nombre))
        print('telefono: '+str(self.telefono))
        print('domic: '+str(self.domicilio))
