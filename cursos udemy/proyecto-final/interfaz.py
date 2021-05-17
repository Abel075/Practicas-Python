



'''
Proyecto final
'''

from tkinter import * 
from tkinter.ttk import *
from controlador import *
from tkinter.messagebox import *

#Agregar productos al carrito

def añadir():
    cantidad = int(sbNumero.get())
    
    #Control de errores
    if twProductos.focus() == "":
        showerror("Error", "Selecciona algun producto")
    elif cantidad == 0:
        showerror("Error", "La cantidad seleccionada no puede ser 0")
    else:
        # Focus devuelve un Indice Ejemple #I001, #I005
        index = int(twProductos.focus().split("I")[1],16) -1
        producto = productos[index]
        importe = round(cantidad * producto[2])
        añadir_linea(twCarrito,txtTotal,producto,cantidad,importe)
        sbNumero.delete(0,"end")
        sbNumero.insert(0,0)
        carrito.append([producto[0],producto[1],producto[2],cantidad])
        
        
        
    
def finalizar():
    cliente = cmbCliente.get()
    
    #Control de errores
    if cliente =="":
        showerror("Error", "Debes seleccionar un cliente")
    elif len(carrito) == 0:
        showerror("Error", "Imposible realizar pedido sin articulos")
    else:
        try:
            dniCliente = cliente.split("-")[0]
            nombreCliente = cliente.split("-")[1]
            finalizar_pedido(carrito,dniCliente,nombreCliente)
            twCarrito.delete(*twCarrito.get_children())
            carrito.clear()
            showinfo("Aviso","El pedido ha sido realizado con exito")
        except:
            showerror("Error","Error al realizar el pedido")
            
        
    
    



clientes = []
productos = []
carrito = []



ventana = Tk(className='Proyecto Final')
ventana.title('Proyecto Final')
ventana.geometry('800x500')
ventana.resizable(False,False)


lblCliente = Label(ventana,text='Cliente')
lblCliente.place(x=100,y=20,in_=ventana)

cmbCliente = Combobox(ventana,width=80,state='readonly')
cmbCliente.place(x=160,y=20,in_=ventana)

#Carga de clientes
clientes = cargar_clientes(cmbCliente)

lblProduct = Label(ventana,text='Productos')
lblProduct.place(x=100,y=90,in_=ventana)

twProductos = Treeview(ventana,height=15)
twProductos['columns'] = ('#1')
twProductos.column('#0',width=180)
twProductos.column('#1',width=60)
twProductos.heading('#0',text='Nombre')
twProductos.heading('#1',text='Precio')
twProductos.place(x=60,y=120,in_=ventana)

#Funcion de carga de productos
productos = cargar_productos(twProductos)

#Caja para alementos a añadir al carrito

sbNumero = Spinbox(ventana,from_=0, to=10, width=5)
sbNumero.place(x=330,y=200,in_=ventana)
sbNumero.insert(0,0)

btnComprar = Button(ventana, text='>>', width=5, command=añadir)
btnComprar.place(x=300,y=250,in_=ventana)

lblCarrito = Label(ventana,text='Carrito de la compra')
lblCarrito.place(x=520,y=90,in_=ventana)

twCarrito = Treeview(ventana,height=15)
twCarrito['columns'] = ('#1', '#2')
twCarrito.column('#0', width=200)
twCarrito.column('#1', width=60)
twCarrito.column('#2', width=80)
twCarrito.heading('#0', text='Nombre')
twCarrito.heading('#1', text='Cant.')
twCarrito.heading('#2', text='importe')
twCarrito.place(x=400,y=120,in_=ventana)

btnFinalizar = Button(ventana, text='Finalizar Compra', width=20,command=finalizar)
btnFinalizar.place(x=400,y=450, in_=ventana)

lblTotal = Label(ventana, text='Total')
lblTotal.place(x=600, y=450, in_=ventana)

txtTotal = Entry(ventana, width=10, justify='right')
txtTotal.place(x=650, y=450, in_=ventana)
txtTotal.insert(END,'0.0 $')
txtTotal.config(state='readonly')








ventana.mainloop()