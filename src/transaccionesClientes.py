class TransaccionesClientes:
    def __init__(self,idTransaccion,cantidad,dpiCliente,idEmpresa,idpoint,tiempoTotal):
        self.idTransaccion=idTransaccion
        self.cantidad=cantidad
        self.dpiCliente=dpiCliente
        self.idEmpresa=idEmpresa
        self.idpoint=idpoint
        self.tiempoTotal=tiempoTotal
        self.siguiente2=None
        self.anterior2=None