from proceso import Proceso

class Lote:
    def __init__(self):
        self.__procesos = []
        ##self.__nodos = dict()

    def agregar_final(self, proceso:Proceso):
        self.__procesos.append(proceso)

    def mostrar(self):
        for v in self.__procesos:
            print(v)

    def eliminar(self,proceso):
        self.__procesos.remove(proceso)
    
    def __str__(self):
        return "".join(
            str(v) + "\n" for v in self.__procesos
        )

    def __len__(self):
        return(
            len(self.__procesos)
        )

    def __iter__(self):
        self.cont = 0

        return self

    def __next__(self):
        if self.cont < len(self.__procesos):
            proceso = self.__procesos[self.cont]
            self.cont += 1
            return proceso

        else:
            raise StopIteration
        