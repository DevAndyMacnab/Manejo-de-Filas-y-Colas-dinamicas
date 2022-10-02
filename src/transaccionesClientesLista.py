from transaccionesClientes import TransaccionesClientes

class TransaccionesClientesLista:
    def __init__(self):
        self.primero=None
        self.ultimo=None
        
    def estaVacia(self):
        if self.primero==None:
            return True
        else:
            return False
    def agregar_inicio(self, idTransaccion, cantidad,dpiCliente):
        nuevo=TransaccionesClientes( idTransaccion, cantidad,dpiCliente)

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
            print(tmp.idTransaccion,tmp.cantidad,tmp.dpiCliente)
            tmp=tmp.anterior
            if tmp==self.ultimo:
                break