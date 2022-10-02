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


print("BIENVENIDO SELECCIONE LAS PRIMERAS OPCIONES PARA INICIAR:")
print(" -limpiar\n -cargarConfig \n -crearEmpresa \n -cargarInicial")
enterpriseList=EnterpriseList()
attentionList=AttentionPointList()
listadodesk=DesksList()
listTransacciones= TransactionsList()

while True:
    firstOpcion= input()
    if firstOpcion == "limpiar":
        enterpriseList=EnterpriseList()
        attentionList=AttentionPointList()
        listadodesk=DesksList()
        listTransacciones= TransactionsList()
        print("LA LISTA SE HA LIMPIADO CORRECTAMENTE")
        enterpriseList.recorrer_fin_inicio()
        
        
        
    elif firstOpcion =="cargarConfig":
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
        print("hola mundo")
        


    elif firstOpcion=="cargarInicial":
        
        inicialConfig=ET.parse(askopenfile())
        inicialConfigXml=inicialConfig.getroot()
        for configInicial in inicialConfigXml:
            print(configInicial.tag)
            activarEscritorios=configInicial.findall("escritoriosActivos")
            for element in  activarEscritorios:
                for desk in element:
                    activar=desk.attrib["idEscritorio"]
                    print(activar)
                    listadodesk.activarEscritorio(activar)
                    listadodesk.recorrer_fin_inicio()
    #esto es una prueba
    
    
    
    
        