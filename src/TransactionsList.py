from ast import Break, If
from cgi import print_directory
import os
from xml.etree.ElementTree import register_namespace
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
        self.unirNodosClient()
        
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
            print(tmp.dpi,tmp.name,tmp.idEmpresa,tmp.idPunto,tmp.idDesk,tmp.tiempoEspera,tmp.tiempoAtencion)
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
                if tmp==self.ultimo:
                    break
            tmp2=tmp2.anterior2
            if tmp2==self.ultimo2:
                break
            
            
    def activarEscritorio(self,id):
        self.id=id
        tmp=self.ultimodesk
        while tmp:
            tmp=tmp.anteriordesk
            if tmp.code==self.id:
                tmp.state=True
                return True
            if tmp==self.ultimodesk:
                print("TODO MAL NO SE ENCONTRO NADA")
                
                
    def cantidadActivos(self,idPunto,idEmpresa):
        self.idempresa=idEmpresa
        self.idpunto=idPunto
        cantidad=0
        tmp=self.ultimodesk
        while tmp:
            tmp=tmp.anteriordesk
            if tmp.idPuntoAtencion==self.idpunto and tmp.idEmpresa==self.idempresa:
                if tmp.state==True:
                    cantidad+=1
                    
                
            if tmp==self.ultimodesk:
                print("La cantidad de escritorios activos es:", cantidad)
                break
                    
        
    def cantidadNoActivos(self,idPunto,idEmpresa):
        self.idempresa=idEmpresa
        self.idpunto=idPunto
        cantidad=0
        tmp=self.ultimodesk
        while tmp:
            tmp=tmp.anteriordesk
            if tmp.idPuntoAtencion==self.idpunto and tmp.idEmpresa==self.idempresa:
                if tmp.state==False:
                    cantidad+=1
                    
                
            if tmp==self.ultimodesk:
                print("La cantidad de escritorios NO activos es:", cantidad)
                break
            
            
    def enlistarClientes(self,idepunto,idEmpresa):
        cantidad=0
        self.idpunto=idepunto
        self.idempresa=idEmpresa
        tmp=self.ultimoCliente
        while tmp:
            tmp=tmp.anteriorCliente
            if tmp.idPunto==self.idpunto and tmp.idEmpresa==self.idempresa:
               cantidad+=1 
            if tmp==self.ultimoCliente:
                print("La cantidad de clientes en espera es:", cantidad)
                break
        
    def asignarEscritorios(self,idpoint,idempresa):
        self.idEmpresa=idempresa
        self.idpoint=idpoint
        tmpDesk=self.ultimodesk
        tmpClient=self.ultimoCliente
        tmpTransacciones=self.ultimo2
        self.tiempoAtencion=0
        self.tiempoMaximo=0
        self.tiempoMinimo=100
        self.tiempoPromedio=0
        self.cantidad=0
        
        
        
        while tmpDesk:
            if self.idpoint==tmpDesk.idPuntoAtencion and self.idEmpresa==tmpDesk.idEmpresa and tmpDesk.state==True :
                
                print("ESCRITORIO",tmpDesk.code)
                while tmpClient:
                    self.tiempoAtencion=0
                    if self.idEmpresa==tmpClient.idEmpresa and self.idpoint==tmpClient.idPunto:
                        tmpClient.idDesk=tmpDesk.code
                        print("  CLIENTE:",tmpClient.dpi,tmpClient.name,tmpClient.idDesk)
                        
                        while tmpTransacciones:
                            if self.idEmpresa==tmpTransacciones.idEmpresa and self.idpoint==tmpTransacciones.idpoint and tmpClient.dpi==tmpTransacciones.dpiCliente:
                                print("    ",tmpTransacciones.idTransaccion,tmpTransacciones.dpiCliente)
                                self.tiempoAtencion=self.tiempoAtencion+tmpTransacciones.tiempoTotal

                            tmpTransacciones=tmpTransacciones.anterior2
                            
                            if tmpTransacciones==self.ultimo2:
                                break
                        tmpClient.tiempoAtencion=self.tiempoAtencion
                        if tmpClient.tiempoAtencion>self.tiempoMaximo:
                            self.tiempoMaximo=tmpClient.tiempoAtencion
                        if tmpClient.tiempoAtencion<self.tiempoMinimo:
                            self.tiempoMinimo=tmpClient.tiempoAtencion
                            
                        print("     El tiempo de atencion del cliente es de: ",tmpClient.tiempoAtencion)
                        self.tiempoPromedio=self.tiempoPromedio+tmpClient.tiempoAtencion
                        self.cantidad+=1
                    tmpClient=tmpClient.anteriorCliente
                    
                    if tmpClient==self.ultimoCliente:
                        break
                    
                    break
            
            tmpDesk=tmpDesk.anteriordesk
            if tmpClient==self.ultimoCliente:
                break
            
            #if tmpDesk==self.ultimodesk:
        self.tiempoPromedio=self.tiempoPromedio/self.cantidad
        print("EL TIEMPO DE ATENCION PROMEDIO DEL PUNTO ES:", self.tiempoPromedio)
        print("EL TIEMPO DE ATENCION MAXIMO DEL PUNTO ES:", self.tiempoMaximo)
        print("EL TIEMPO MINIMO DE ATENCION DEL PUNTO ES:", self.tiempoMinimo)
    
    def manejoTiempos(self,idEmpresa,idPunto):
        self.idempresa=idEmpresa
        self.idpunto=idPunto
        tmpDesk=self.ultimodesk
        tmpClient=self.ultimoCliente
        tmpTransacciones=self.ultimo2
        self.tiempoEspera=0
        self.tiempoEsperaMaximo=0
        self.tiempoEsperaMinimo=100
        self.tiempoEsperaPromedio=0
        self.cantidad=0
        
        while tmpDesk:
            self.tiempoEspera=0
            if self.idEmpresa==tmpDesk.idEmpresa and self.idpoint==tmpDesk.idPuntoAtencion and tmpDesk.state==True :
                while tmpClient:
                    if self.idEmpresa==tmpClient.idEmpresa and self.idpoint==tmpClient.idPunto and tmpDesk.code==tmpClient.idDesk:
                        print(tmpDesk.code)
                        print(tmpClient.name,tmpClient.tiempoAtencion)
                        tmpClient.tiempoEspera=self.tiempoEspera
                        self.cantidad+=1
                        self.tiempoEsperaPromedio=self.tiempoEsperaPromedio+ tmpClient.tiempoEspera
                        
                        if tmpClient.tiempoEspera>self.tiempoEsperaMaximo:
                            self.tiempoEsperaMaximo=tmpClient.tiempoEspera
                            
                        if tmpClient.tiempoEspera<self.tiempoEsperaMinimo and tmpClient.tiempoEspera>0:
                            self.tiempoEsperaMinimo=tmpClient.tiempoEspera
                        print("su tiempo de espera es:",tmpClient.tiempoEspera)
                        
                        self.tiempoEspera=self.tiempoEspera + tmpClient.tiempoAtencion
                        
                        while tmpTransacciones:
                            if self.idEmpresa==tmpTransacciones.idEmpresa and self.idpoint==tmpTransacciones.idpoint and tmpClient.dpi==tmpTransacciones.dpiCliente:
                                print("transacciones: ",tmpTransacciones.dpiCliente)
                            tmpTransacciones=tmpTransacciones.anterior2
                            if tmpTransacciones==self.ultimo2:
                                break
                    tmpClient=tmpClient.anteriorCliente
                    if tmpClient==self.ultimoCliente:
                        break
            tmpDesk=tmpDesk.anteriordesk
            if tmpDesk==self.ultimodesk:
                break
        print("--------------------------------")
        self.tiempoEsperaPromedio=self.tiempoEsperaPromedio/self.cantidad
        print("EL TIEMPO DE ESPERA MAXIMO DEL PUNTO DE ATENCION ES: ",self.tiempoEsperaMaximo)
        print("EL TIEMPO DE ESPERAR MINIMO DEL PUNTO DE ATENCION ES:", self.tiempoEsperaMinimo)
        print("EL TIEMPO DE ESPERA PROMEDIO DEL PUNTO DE ATENCION ES: ", self.tiempoEsperaPromedio)
                        
    def tiempoEscritorios(self,idEmpresa,idPunto):
        self.idempresa=idEmpresa
        self.idpunto=idPunto
        tmpDesk=self.ultimodesk
        tmpClient=self.ultimoCliente
        tmpTransacciones=self.ultimo2
        self.tiempoEspera=0
        self.tiempoEsperaMaximo=0
        self.tiempoEsperaMinimo=100
        self.tiempoEsperaPromedio=0
        self.cantidad=0
        
        self.tAntecion=0
        self.tAtencionMaximo=0
        self.tAtencionMinimo=0
        
        while tmpDesk:
            self.tiempoEspera=0
            self.tiempoEsperaMaximo=0
            self.tiempoEsperaMinimo=100
            self.tiempoEsperaPromedio=0
            if self.idEmpresa==tmpDesk.idEmpresa and self.idpoint==tmpDesk.idPuntoAtencion and tmpDesk.state==True :
                while tmpClient:
                    if self.idEmpresa==tmpClient.idEmpresa and self.idpoint==tmpClient.idPunto and tmpDesk.code==tmpClient.idDesk:
                        print(tmpDesk.code)
                        print(tmpClient.name,tmpClient.tiempoAtencion)
                        tmpClient.tiempoEspera=self.tiempoEspera
                        self.cantidad+=1
                        self.tiempoEsperaPromedio=self.tiempoEsperaPromedio+ tmpClient.tiempoEspera
                        
                        if tmpClient.tiempoEspera>self.tiempoEsperaMaximo:
                            self.tiempoEsperaMaximo=tmpClient.tiempoEspera
                            
                        if tmpClient.tiempoEspera<self.tiempoEsperaMinimo and tmpClient.tiempoEspera>0:
                            self.tiempoEsperaMinimo=tmpClient.tiempoEspera
                        print("su tiempo de espera es:",tmpClient.tiempoEspera)
                        
                        
                        self.tiempoEspera=self.tiempoEspera + tmpClient.tiempoAtencion
                        
                        while tmpTransacciones:
                            if self.idEmpresa==tmpTransacciones.idEmpresa and self.idpoint==tmpTransacciones.idpoint and tmpClient.dpi==tmpTransacciones.dpiCliente:
                                print("transacciones: ",tmpTransacciones.dpiCliente)
                            tmpTransacciones=tmpTransacciones.anterior2
                            if tmpTransacciones==self.ultimo2:
                                break
                    tmpClient=tmpClient.anteriorCliente
                    if tmpClient==self.ultimoCliente:
                
                        break
                print("--------------------------------")
                self.tiempoEsperaPromedio=self.tiempoEsperaPromedio/self.cantidad
                print("EL TIEMPO DE ESPERA MAXIMO DEL ESCRITORIO ES: ",self.tiempoEsperaMaximo)
                print("EL TIEMPO DE ESPERAR MINIMO DEL ESCRITORIO ES:", self.tiempoEsperaMinimo)
                print("EL TIEMPO DE ESPERA PROMEDIO DEL ESCRITORIO ATENCION ES: ", self.tiempoEsperaPromedio)
                
            tmpDesk=tmpDesk.anteriordesk
            if tmpDesk==self.ultimodesk:
                break
            
    def activarDesk(self,idDesk,idEmpresa,idPunto):
        self.idesk=idDesk
        self.idempresa=idEmpresa
        self.idpunto=idPunto
        
        tmp=self.ultimodesk
        while tmp:
            tmp=tmp.anteriordesk
            if tmp.code==self.idesk and tmp.idEmpresa==self.idempresa and tmp.idPuntoAtencion==self.idpunto:
                print("HA ELEGIDO EL ESCRITORIO:", tmp.code, tmp.attendant)
                tmp.state=True
            if tmp==self.ultimodesk:
                break
            
    def desactivarDesk(self,idDesk,idEmpresa,idPunto):
        self.idesk=idDesk
        self.idempresa=idEmpresa
        self.idpunto=idPunto
        
        tmp=self.ultimodesk
        while tmp:
            tmp=tmp.anteriordesk
            if tmp.code==self.idesk and tmp.idEmpresa==self.idempresa and tmp.idPuntoAtencion==self.idpunto:
                print("HA ELEGIDO EL ESCRITORIO:", tmp.code, tmp.attendant)
                tmp.state=False
            if tmp==self.ultimodesk:
                break
            
    def reporteCliente(self):
        aux=self.primeroCliente
        text=""
        text+="rankdir=LR; \n "
        text+="node[shape=egg, style=filled, color=khaki, fontname=\"Century Gothic\"];  graph [fontname = \"Century Gothic\"];"
        text+="labelloc=\"t; \"label = \"Clientes\";\n"

        while aux:
            text+="x"+str(aux.dpi)+"[dir=both label=\"DPI ="+str(aux.dpi)+"\\nNombre = "+aux.name+" \\SU ESCRITORIO = "+str(aux.idDesk)+ "\"]"
            text+="x"+str(aux.dpi)+"-> x"+str(aux.siguienteCliente.dpi) +"\n"
            text+="x"+str(aux.dpi)+"-> x"+str(aux.anteriorCliente.dpi) +"\n"
            aux=aux.siguienteCliente
            if aux!=self.primeroCliente:
                text+="x"+str(aux.dpi)+"[dir=both label=\"Codigo ="+str(aux.dpi)+"\\nNombre = "+aux.name+" \\SU ESCRITORIO = "+str(aux.idDesk)+ "\"]"
                print(text)
            if aux==self.ultimoCliente:
                text+="x"+str(aux.dpi)+ "-> x"+str(aux.siguienteCliente.dpi)+"\n"
                text+="x"+str(aux.dpi)+ "-> x"+str(aux.anteriorCliente.dpi)+"\n"
                break
        return text
    
    def crearReporteCliente(self):
        os.mkdir("Clientes")
        contenido="digraph G{\n\n"
        r=open("Clientes/reporte.txt","w")
        contenido+=str(self.reporteCliente())
        contenido+="\n}"
        r.write(contenido)
        r.close()
        print("done")
        os.system("dot -Tpng Clientes/reporte.txt -o Clientes/reporte.png")
        os.system("dot -Tpdf Clientes/reporte.txt -o Clientes/reporte.pdf")
    
    def reporteDesk(self):
        aux=self.primerodesk
        text=""
        text+="rankdir=LR; \n "
        text+="node[shape=egg, style=filled, color=khaki, fontname=\"Century Gothic\"];  graph [fontname = \"Century Gothic\"];"
        text+="labelloc=\"t; \"label = \"Escritorios\";\n"

        while aux:
            text+="x"+str(aux.id)+"[dir=both label=\"Code ="+str(aux.id)+"\\Encargado = "+aux.attendant+" \\Estado = "+str(aux.state)+ "\"]"
            text+="x"+str(aux.id)+"-> x"+str(aux.siguientedesk.id) +"\n"
            text+="x"+str(aux.id)+"-> x"+str(aux.anteriordesk.id) +"\n"
            aux=aux.siguientedesk
            if aux!=self.primerodesk:
                text+="x"+str(aux.id)+"[dir=both label=\"Code ="+str(aux.id)+"\\Encargado = "+aux.attendant+" \\Estado = "+str(aux.state)+ "\"]"
                print(text)
            
                break
        return text
    def crearReporteDesk(self):
        os.mkdir('Escritorios')
        contenido="digraph G{\n\n"
        r=open("Escritorios/reporte.txt","w")
        contenido+=str(self.reporteDesk())
        contenido+="\n}"
        r.write(contenido)
        r.close()
        print("done")
        os.system("dot -Tpng Escritorios/reporte.txt -o Escritorios/reporte.png")
        os.system("dot -Tpdf Escritorios/reporte.txt -o Escritorios/reporte.pdf")
        
                
    
        
            
        
            

                
                
        
        
        
        