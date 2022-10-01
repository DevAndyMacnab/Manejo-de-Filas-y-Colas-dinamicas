class Desks():
    def __init__(self,code,id,attendant,state,idPuntoAtencion) :
        self.code=code
        self.id=id
        self.attendant=attendant
        self.state=state
        self.idPuntoAtencion=idPuntoAtencion
        self.siguiente=None
        self.anterior=None
        
        