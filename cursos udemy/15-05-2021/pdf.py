#Importamos modulos de reportlab

from reportlab.pdfgen import canvas

pdf = canvas.Canvas('prueba.pdf')

pdf.save()
