class TransaccionesClientes:
    def __init__(self,idTransaccion,cantidad,dpiCliente):
        self.idTransaccion=idTransaccion
        self.cantidad=cantidad
        self.dpiCliente=dpiCliente
        self.siguiente=None
        self.anterior=None