from ast import Break
import os
from Transactions import Transactions
from transaccionesClientes import TransaccionesClientes

class TransactionsList:
    def __init__(self) :
        self.primero=None
        self.ultimo=None
        self.primero2=None
        self.ultimo2=None
        
        
    def estaVacia(self):
        if self.primero==None:
            return True
        else:
            return False
        
    def estaVacia2(self):
        if self.primero2==None:
            return True
        else:
            return False
        
    def agregar_inicio(self, code, name, time,idEmpresa):
        nuevo=Transactions( code, name, time,idEmpresa)

        if self.estaVacia():
            self.primero=self.ultimo=nuevo
        else:
            tmp=nuevo
            tmp.siguiente=self.primero
            self.primero.anterior=tmp
            self.primero=tmp
        self .__unir_nodos()
        
    def agregar_inicio_Clientes(self,idTransaccion,cantidad,dpiCliente,idEmpresa,idpoint,tiempoTotal):
        new=TransaccionesClientes( idTransaccion,cantidad,dpiCliente,idEmpresa,idpoint,tiempoTotal)
        if self.estaVacia2():
            self.primero2=self.ultimo2=new
        else:
            tmp=new
            tmp.siguiente2=self.primero2
            self.primero2.anterior2=tmp
            self.primero2=tmp
        self.unirNodosClientes()
            
            
        
    def __unir_nodos(self):
        if self.primero!=None:
            self.primero.anterior=self.ultimo
            self.ultimo.siguiente=self.primero
            
    def unirNodosClientes(self):
        if self.primero2!=None:
            self.primero2.anterior2=self.ultimo2
            self.ultimo2.siguiente2=self.primero2
            
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
            print(tmp.code, tmp.name, tmp.time,tmp.idEmpresa)
            tmp=tmp.anterior

            if tmp==self.ultimo:
                break
            
    def recorrerClientes(self):
        tmp=self.ultimo2
        while tmp:
            print(tmp.idTransaccion,tmp.cantidad,tmp.dpiCliente,tmp.idEmpresa,tmp.idpoint,tmp.tiempoTotal)
            tmp=tmp.anterior2
            if tmp==self.ultimo2:
                break
            
    def tiemposTotales(self,idempresa,idpoint):
        
        self.idempresa=idempresa
        self.idpoint=idpoint
        tmp=self.ultimo
        tmp2=self.ultimo2
        while tmp2:
            tmp2=tmp2.anterior2
            
            while tmp:
                operando=0
                tmp=tmp.anterior
                if tmp.code==tmp2.idTransaccion:
                    print(tmp.time, tmp2.cantidad)
                    operando=int(tmp.time)*int(tmp2.cantidad)
                    print(operando)
                if tmp==self.ultimo:
                    break
            if tmp2==self.ultimo2:
                break
            
            
        
            

                
                
        
        
        
        