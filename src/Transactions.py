class Transactions:
    def __init__(self,code,name,time,idEmpresa) :
        self.code=code
        self.name=name
        self.time=time
        self.idEmpresa=idEmpresa
        self.siguiente=None
        self.anterior=None
        