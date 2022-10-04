from email.errors import InvalidMultipartContentTransferEncodingDefect
import sys
sys.path.append(r"C:\Users\andyr\Desktop\PROGRA PARA USAC\PROYECTO2-LAB-IPC2\src")
from importlib.metadata import FileHash
from tkinter.filedialog import askopenfile
from xml.dom.minidom import Element
import xml.etree.ElementTree as ET
from EnterpriseList import EnterpriseList
from AttentionPointList import AttentionPointList
from ClientList import ClientList
from DesksList import DesksList
from TransactionsList import TransactionsList
from transaccionesClientesLista import TransaccionesClientesLista



enterpriseList=EnterpriseList()
attentionList=AttentionPointList()
listadodesk=DesksList()
listTransacciones= TransactionsList()
listaClientes=ClientList()
listaTransaccionesClientes= TransaccionesClientesLista()

while True:
    print(" -limpiar\n -config \n -crearEmpresa \n -inicial \n -seleccion")
    firstOpcion= input(". . .")
    if firstOpcion == "limpiar":
        enterpriseList=EnterpriseList()
        attentionList=AttentionPointList()
        listadodesk=DesksList()
        listTransacciones= TransactionsList()
        listaClientes=ClientList()
        listaTransaccionesClientes=TransaccionesClientesLista()
        
        print("LA LISTA SE HA LIMPIADO CORRECTAMENTE")
        enterpriseList.recorrer_fin_inicio()
        
        
        
    elif firstOpcion =="config":
        systemConfig=ET.parse(askopenfile())
        systemConfigXml=systemConfig.getroot()
        
        #Aca cargamos toda la informacion para las listas enlazadas de la app
        enterprise=systemConfigXml.findall("empresa")
        print("LISTA DE EMPRESAS---------")
        for element in enterprise:
            id=element.attrib["id"]
            name=element.find("nombre").text
            abb=element.find("abreviatura").text
            enterpriseList.agregar_inicio(id,name,abb)
            
                
        enterpriseList.recorrer_fin_inicio()
        print("----------------")
        for empresa in systemConfigXml:
            
            for punto in empresa:
                
                puntoAtencion= punto.findall("puntoAtencion")
                transacciones= punto.findall("transaccion")
                for element in puntoAtencion:
                    id=element.attrib["id"]
                    name=element.find("nombre").text
                    direccion=element.find("direccion").text
                    idEmpresa=empresa.attrib["id"]
                    
                    attentionList.agregar_inicio(id,name,direccion,idEmpresa)
                    
                    for listaEscritorio in element:
                        listDesk=listaEscritorio.findall("escritorio")
                        
                        for ele in listDesk:
                            code=ele.attrib["id"]
                            id=ele.find("identificacion").text
                            attendant=ele.find("encargado").text
                            state=False
                            idPuntoAtencion=element.attrib["id"]
                            listadodesk.agregar_inicio(code,id,attendant,state,idPuntoAtencion)
                
                for transac in transacciones:
                    id=transac.attrib["id"]
                    nombre=transac.find("nombre").text
                    tiempoAtencion=transac.find("tiempoAtencion").text
                    idempresa=empresa.attrib["id"]
                    listTransacciones.agregar_inicio(id,nombre,tiempoAtencion,idempresa)
                    
         
        print("LISTA DE PUNTOS DE ATENCION -----------------------")
        attentionList.recorrer_fin_inicio()
        print("LISTA DE ESCRITORIOS -----------------------")
        listadodesk.recorrer_fin_inicio()
        print("LISTA DE TRANSACCIONES -----------------------")
        listTransacciones.recorrer_fin_inicio()
        


    elif firstOpcion=="crearEmpresa":
        code=input("INGRESE EL ID DE LA EMPRESA ")
        name=input("INGRESE EL NOMBRE DE LA EMPRESA ")
        abbreviation=input("INGRESE LA ABREVIACION DE LA EMPRESA ")
        enterpriseList.agregar_inicio(code,name,abbreviation)
        print("-----------")
        cantidadPuntos=input("¿CUANTOS ESCRITORIOS QUIERE INGRESAR? ")
        for i in range(int(cantidadPuntos)):
            print("-------------")
            codigo=input("INGRESE EL ID DEL PUNTO DE ATENCION ")
            nombre=input("INGRESE EL NOMBRE DEL PUNTO DE ATENCION ")
            address=input("INGRESE LA DIRECCION DEL PUNTO DE ATENCION ")
            idEmpresa=code
            attentionList.agregar_inicio(codigo,nombre,address,idEmpresa)
        
        cantidadEscritorios=input("¿CUANTOS ESCRITORIOS DESEA INGRESAR? ")
        for i in range(int(cantidadEscritorios)):
            print("-----------")
            Codigo=input("INGRESE EL ID DEL ESCRITORIO ")
            ide=input("INGRESE LA IDENTIFICACION DEL ESCRITORIO ")
            attend=input("INGRESE EL NOMBRE DEL ENCARGADO ")
            state=False
            idAtencion=codigo
            listadodesk.agregar_inicio(Codigo,ide,attend,state,idAtencion)
            
        print("SE HAN GUARDADO LOS DATOS DE LA EMPRESA SATISFACTORIAMENTE: ")
        print("Empresas")
        enterpriseList.recorrer_fin_inicio()
        print("Puntos de Atencion")
        attentionList.recorrer_fin_inicio()
        print("Escritorios de atencion")
        listadodesk.recorrer_fin_inicio()
        


    elif firstOpcion=="inicial":
        
        inicialConfig=ET.parse(askopenfile())
        inicialConfigXml=inicialConfig.getroot()
        for configInicial in inicialConfigXml:
            
            idEmpresa=configInicial.attrib["idEmpresa"]
            idpoint=configInicial.attrib["idPunto"]
            idConfig=configInicial.attrib["id"]
            
            activarEscritorios=configInicial.findall("escritoriosActivos")
            
           
            for element in  activarEscritorios:
                for desk in element:
                    activar=desk.attrib["idEscritorio"]
                    
                    listadodesk.activarEscritorio(activar)
                    #listadodesk.recorrer_fin_inicio()
            
            for el in configInicial:
                clientes=el.findall("cliente")
                
                for cliente in clientes:
                    dpi= cliente.attrib["dpi"]
                    nombre=cliente.find("nombre").text
                    listaClientes.agregar_inicio(dpi,nombre,idEmpresa,idpoint)
                    print("todo bien")
                    
                    for transaccion in cliente:
                        clienteTransaccion=transaccion.findall("transaccion")
                        
                        for element in clienteTransaccion:
                            idTransaccion=element.attrib["idTransaccion"]
                            cantidad=element.attrib["cantidad"]
                            listaTransaccionesClientes.agregar_inicio(idTransaccion,cantidad,dpi)
                            print(idTransaccion,cantidad)
                            
                    
        listaTransaccionesClientes.recorrer_fin_inicio()            
        listaClientes.recorrer_fin_inicio()
        
    elif firstOpcion=="seleccion":
        #LISTADO DE TODAS LAS EMPRESAS DISPONIBLES
        enterpriseList.recorrer_fin_inicio()
        seleccionEmpresa=input("SELECCIONE UNA EMPRESA INGRESANDO EL ID: ")
        enterpriseList.seleccionEmpresa(seleccionEmpresa)
        print("---------------------")
        attentionList.repartoPuntos(seleccionEmpresa)
        
        seleccionPunto=input("SELECCIONE EL PUNTO DE ANTECION INGRESANDO EL ID: ")
        attentionList.seleccionPuntoAtencion(seleccionPunto,seleccionEmpresa)
        
        
        
        
        
        
        
        
        
            
                
    
    
    
    
        