from ast import Break
import os
from Transactions import Transactions
from transaccionesClientes import TransaccionesClientes
from Desks import Desks
from Client import Client


class TransactionsList:
    def __init__(self) :
        self.primero=None
        self.ultimo=None
        
        self.primero2=None
        self.ultimo2=None
        
        self.primerodesk=None
        self.ultimodesk=None
        
        self.primeroCliente=None
        self.ultimoCliente=None
        
        
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
        
    def estaVaciaDesk(self):
        if self.primerodesk==None:
            return True
        else:
            return False
        
    def estaVaciaCliente(self):
        if self.primeroCliente==None:
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
        
    def agregar_inicioClientes(self,dpi,name,idEmpresa,idPunto,idDesk,tiempoEspera,tiempoAtencion):
        nuevo=Client(dpi,name,idEmpresa,idPunto,idDesk,tiempoEspera,tiempoAtencion)
        if self.estaVaciaCliente():
            self.primeroCliente=self.ultimoCliente=nuevo
        else:
            tmp=nuevo
            tmp.siguienteCliente=self.primeroCliente
            self.primeroCliente.anteriorCliente=tmp
            self.primeroCliente=tmp
        self.unirNodosClientes()
        
    def agregar_inicioDesk(self,code,id,attendant,state,idPuntoAtencion,idEmpresa):
        nuevo=Desks(code,id,attendant,state,idPuntoAtencion,idEmpresa)
        if self.estaVaciaDesk():
            self.primerodesk=self.ultimodesk=nuevo
        else:
            tmp=nuevo
            tmp.siguientedesk=self.primerodesk
            self.primerodesk.anteriordesk=tmp
            self.primerodesk=tmp
        self.unirNodosDesk()
        
            
            
        
    def __unir_nodos(self):
        if self.primero!=None:
            self.primero.anterior=self.ultimo
            self.ultimo.siguiente=self.primero
            
    def unirNodosClientes(self):
        if self.primero2!=None:
            self.primero2.anterior2=self.ultimo2
            self.ultimo2.siguiente2=self.primero2
            
    def unirNodosClient(self):
        if self.primeroCliente!=None:
            self.primeroCliente.anteriorCliente=self.ultimoCliente
            self.ultimoCliente.siguienteCliente=self.primeroCliente
            
    def unirNodosDesk(self):
        if self.primerodesk!=None:
            self.primerodesk.anteriordesk=self.ultimodesk
            self.ultimodesk.ultimodesk=self.primerodesk
        
            
            
            
            
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
    
    def recorrerClient(self):
        tmp=self.ultimoCliente
        while tmp:
            print(tmp.dpi,tmp.name,tmp.idEmpresa,tmp.idPunto,tmp.tiempoEspera,tmp.tiempoAtencion)
            tmp=tmp.anteriorCliente
            if tmp==self.ultimoCliente:
                break
            
    def recorrerDesk(self):
        tmp=self.ultimodesk
        while tmp:
            print(tmp.code,tmp.id,tmp.attendant,tmp.state,tmp.idPuntoAtencion,tmp.idEmpresa)
            tmp=tmp.anteriordesk
            if tmp==self.ultimodesk:
                break
                    
            
            
            
    def tiemposTotales(self,idempresa,idpoint):
        self.sumatoria=0
        self.idempresa=idempresa
        self.idpoint=idpoint
        tmp=self.ultimo
        tmp2=self.ultimo2
        while tmp2:
            while tmp:       
                operando=0
                tmp=tmp.anterior
                if tmp.code==tmp2.idTransaccion and self.idempresa==tmp2.idEmpresa:
                    
                    operando=int(tmp.time)*int(tmp2.cantidad)
                    tmp2.tiempoTotal=operando

                    print(operando)
                if tmp==self.ultimo:
                    break
            tmp2=tmp2.anterior2
            if tmp2==self.ultimo2:
                break
            
            
        
            

                
                
        
        
        
        