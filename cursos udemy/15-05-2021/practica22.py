'''
Desarrollar un programa con interfaz grafica destinado a la conversion de divisas.
El usuario podra insertar el numero d euros que quiere convertir y mediante un boton proceder a su conversion a dolares y libras.
'''

from tkinter import * 
from tkinter.messagebox import *


def convertir():
    try:
        euros = float(txtEuros.get())
        dolares = round(euros * 1.17,2)
        libras = round(euros * 0.9,2)
        
        
        txtDolares.config(state='normal')
        txtDolares.delete(0,END)
        txtDolares.insert(0,dolares)
        txtDolares.config(state='disabled')
        txtLibras.config(state='normal')
        txtLibras.delete(0,END)
        txtLibras.insert(0,libras)
        txtLibras.config(state='disabled')
       
    except:
        print('Error, imposible realizar la convercion')
        showerror(message='imposible realizar la conversion', title='Error')
        



ventana = Tk(className='Practica 22')
ventana.geometry('500x200')

lblTitulo = Label(ventana,text='Conversor de monedas')
lblTitulo.place(x=80,y=10,in_=ventana)
lblTitulo.config(font=('Cuorier',22))


lblEuros = Label(ventana,text='Euros')
lblEuros.place(x=70,y=80,in_=ventana)

txtEuros = Entry(ventana,width=10)
txtEuros.place(x=60,y=100,in_=ventana)

lblDolares = Label(ventana, text='Dolares')
lblDolares.place(x=350,y=80,in_=ventana)

txtDolares = Entry(ventana,width=10)
txtDolares.place(x=340,y=100,in_=ventana)
txtDolares.config(state='disabled')

lblLibras = Label(ventana, text='Libras')
lblLibras.place(x=200,y=80,in_=ventana)

txtLibras = Entry(ventana,width=10)
txtLibras.place(x=200,y=100,in_=ventana)
txtLibras.config(state='disabled')

btnConvertir = Button(ventana, text='Convertir', command=convertir, bg='red')
btnConvertir.place(x=180,y=130,in_=ventana)





ventana.mainloop()