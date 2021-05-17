#Importamos modulos de reportlab

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

w,h = A4

pdf = canvas.Canvas('prueba.pdf', pagesize=A4)

#Estilos al pdf
pdf.setFont('Times-Roman',40)
pdf.setFillColorRGB(255,0,0)
#Escribir en el pdf
pdf.drawString(50,h-50,'Hola mundo')

#dibujar figuras geometricas
#linea
pdf.line(50,500,100,500)
#Regtangulo
pdf.rect(300,700,50,100)
#circulo
pdf.circle(100,400,80)



pdf.save()
