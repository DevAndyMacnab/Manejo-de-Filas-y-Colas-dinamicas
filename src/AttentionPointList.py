
from AttentionPoint import AttentionPoint

class AttentionPointList:
    def __init__(self) :
        self.primero=None
        self.ultimo=None
        
    def estaVacia(self):
        if self.primero==None:
            return True
        else:
            return False
        
    def agregar_inicio(self, code, name, address,idEmpresa):
        nuevo=AttentionPoint(code, name, address,idEmpresa)

        if self.estaVacia():
            self.primero=self.ultimo=nuevo
        else:
            tmp=nuevo
            tmp.siguiente=self.primero
            self.primero.anterior=tmp
            self.primero=tmp
        self .__unir_nodos()
        
    def __unir_nodos(self):
        if self.primero!=None:
            self.primero.anterior=self.ultimo
            self.ultimo.siguiente=self.primero
            
    def eliminar_final(self):
        if self.estaVacia():
            print("ERROR: La lista esta vacia")
        elif self.primero==self.ultimo:
            self.primero=self.ultimo=None
        else:
            self.ultimo=self.ultimo.anterior
        self .__unir_nodos()
        
    def recorrer_fin_inicio(self):
        tmp=self.ultimo
        
        while tmp:
            print(tmp.code, tmp.name, tmp.address,tmp.idEmpresa)
            tmp=tmp.anterior
            if tmp==self.ultimo:
                break
            
        
    def repartoPuntos(self,seleccionEmpresa):
        self.seleccion=seleccionEmpresa
        tmp=self.ultimo
        while tmp:
            tmp=tmp.anterior
            if tmp.idEmpresa==self.seleccion:
                print(tmp.code,tmp.name,tmp.address,tmp.idEmpresa)
                
            if tmp==self.ultimo:
                break
    def seleccionPuntoAtencion(self,seleccionPunto,idempresa):
        self.idempresa=idempresa
        self.seleccion=seleccionPunto
        tmp=self.ultimo
        while tmp:
            tmp=tmp.anterior
            if tmp.code==self.seleccion and tmp.idEmpresa==self.idempresa:
                print("HA SELECCIONADO EL PUNTO: ",tmp.code,tmp.name,tmp.address,tmp.idEmpresa)
                
            if tmp==self.ultimo:
                break
        
        