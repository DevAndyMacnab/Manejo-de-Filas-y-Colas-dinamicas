from cgi import print_directory
import os
from Desks import Desks

class DesksList:
    def __init__(self) :
        self.primero=None
        self.ultimo=None
        
    def estaVacia(self):
        if self.primero==None:
            return True
        else:
            return False
        
    def agregar_inicio(self, code, id,attendant, state,idPuntoAtencion,idEmpresa):
        nuevo=Desks( code, id, attendant,state,idPuntoAtencion,idEmpresa)

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
            print(tmp.code, tmp.id, tmp.attendant,tmp.state,tmp.idPuntoAtencion,tmp.idEmpresa)
            tmp=tmp.anterior
            if tmp==self.ultimo:
                break
            
    def activarEscritorio(self,id):
        self.id=id
        tmp=self.ultimo
        while tmp:
            tmp=tmp.anterior
            if tmp.code==self.id:
                tmp.state=True
                return True
            if tmp==self.ultimo:
                print("TODO MAL NO SE ENCONTRO NADA")
                
    def enlistarEscritorios(self,idPunto,idEmpresa):
        self.idpunto=idPunto
        self.idempresa=idEmpresa
        tmp=self.ultimo
        while tmp:
            tmp=tmp.anterior
            if tmp.idPuntoAtencion==self.idpunto and tmp.idEmpresa==self.idempresa:
                print(tmp.code, tmp.id, tmp.attendant, tmp.state,tmp.idPuntoAtencion)
            if tmp==self.ultimo:
                break
            
    def cantidadActivos(self,idPunto,idEmpresa):
        self.idempresa=idEmpresa
        self.idpunto=idPunto
        cantidad=0
        tmp=self.ultimo
        while tmp:
            tmp=tmp.anterior
            if tmp.idPuntoAtencion==self.idpunto and tmp.idEmpresa==self.idempresa:
                if tmp.state==True:
                    cantidad+=1
                    
                
            if tmp==self.ultimo:
                print("La cantidad de escritorios activos es:", cantidad)
                break
                    
        
    def cantidadNoActivos(self,idPunto,idEmpresa):
        self.idempresa=idEmpresa
        self.idpunto=idPunto
        cantidad=0
        tmp=self.ultimo
        while tmp:
            tmp=tmp.anterior
            if tmp.idPuntoAtencion==self.idpunto and tmp.idEmpresa==self.idempresa:
                if tmp.state==False:
                    cantidad+=1
                    
                
            if tmp==self.ultimo:
                print("La cantidad de escritorios NO activos es:", cantidad)
                break
        
        