from random import randint



def lanzar():

    
 return randint(1,6) 

primer_dado = lanzar()
segundo_dado = lanzar()
suma = primer_dado + segundo_dado



    

menu = """
¿Quiere lanzar los dados?
1-Si
2-No
"""
print(menu)
op = int(input())
if op is 1:
    
    
        print('Se lanzaron los dados y el primer salio: ', primer_dado)    
        print('El segundo salio: ', segundo_dado)
        print('La suma de los dados es:' , suma)
        
elif op is 2:
    
        print("quier volver a lanzar?")
    
print(menu)    
    
    
    

