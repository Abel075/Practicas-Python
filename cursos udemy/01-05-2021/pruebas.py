class sumaDos:
    def __init__(seft,datos):
        self.datos = datos
        self.indice = 0
        
    def __iter__(seft):
        return self
    
    def __next__(self):
        if self.indice ==len(self.datos):
            raise StopIteration()
        elemento = self.datos[self.indice] +2
        self.indice +=1
        return elemento
    
list(sumaDos([1,2,3,4,5]))