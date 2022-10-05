class Client:
    def __init__(self,dpi,name,idEmpresa,idPunto,idDesk,tiempoEspera,tiempoAtencion) :
        self.dpi=dpi
        self.name=name
        self.idEmpresa=idEmpresa
        self.idPunto=idPunto
        self.idDesk=idDesk
        self.tiempoEspera=tiempoEspera
        self.tiempoAtencion=tiempoAtencion
        self.siguienteCliente=None
        self.anteriorCliente=None
        
        