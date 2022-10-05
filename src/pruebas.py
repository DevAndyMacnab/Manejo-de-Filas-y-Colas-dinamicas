from transaccionesClientesLista import TransaccionesClientesLista
from TransactionsList import TransactionsList
sumando=0
listaClientes=TransaccionesClientesLista()
listaTransacciones=TransactionsList()

#----------------------------idTransaccion, La cantidad, dpi del cliente, el id de la empresa
listaClientes.agregar_inicio("bnr","2","3020362960101","123")
listaClientes.agregar_inicio("bnr","5","30203629601","123")
listaClientes.agregar_inicio("vn","5","30203660101","123")
listaClientes.agregar_inicio("za","9","0362960101","123")
listaClientes.agregar_inicio("pablomotos","3","30101","123")
listaClientes.recorrer_fin_inicio()

print("---------------------SEPARACION------------------")
#----------------------------el id de la transaccion, nombre, el tiempo que dura, el id de la empresa al que pertenece
listaTransacciones.agregar_inicio("bnr","PedorSanchez","7","123")
listaTransacciones.agregar_inicio("vn","Abascal","2","123")
listaTransacciones.agregar_inicio("za","ermanolitox","5","123")
listaTransacciones.agregar_inicio("pablomotos","cameracafe100","20","123")
listaTransacciones.recorrer_fin_inicio()
print("-----------------------------------------")
for x in range(4):
    listaTransacciones.recorrer_fin_inicio()
    #probando=listaTransacciones.categorizacionTransacciones("bnr","2")
    #sumando=sumando + probando
    #print(sumando)

    
