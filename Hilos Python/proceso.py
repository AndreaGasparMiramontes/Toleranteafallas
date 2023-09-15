class Proceso:
    def __init__(self, id, programador, num1,op,num2,tiempo):
        self.__id = id
        self.__programador = programador
        self.__num1 = num1
        self.__op = op
        self.__num2 = num2
        self.__tiempo = tiempo
        self.__restante = tiempo
        if(op == "+"):
            self.__resultado = num1 + num2
        elif(op == "-"):
            self.__resultado = num1 - num2
        elif(op == "*"):
            self.__resultado = num1 * num2
        elif(op == "/"):
            if(num2!=0):
                self.__resultado = num1 / num2
            else:
                self.__resultado = "math error"
        elif(op == "%"):
            if(num2!=0):
                self.__resultado = num1 % num2
            else:
                self.__resultado = "math error"
        elif(op == "^"):
            self.__resultado = num1 ** num2

    def __str__(self):
        return (
            "ID: " + str(self.__id) + "\n"
            "Operacion: " + str(self.__num1) + str(self.__op) + str(self.__num2) + "\n"
            "Tiempo max: " + str(self.__tiempo) + " segundo(s)\n"
        )
    
    def set_time(self,time):
        self.__restante = time
    
    def set_error(self):
        self.__resultado = "ERROR"

    def to_dict(self):
        return{
            "id": self.__id,
            "programador": self.__programador,
            "operacion": self.__operacion,
            "tiempo": self.__tiempo,
        }

    @property
    def id(self):
        return self.__id

    @property
    def programador(self):
        return self.__programador

    @property
    def operacion(self):
        return (str(self.__num1) + self.__op + str(self.__num2))

    @property
    def tiempo(self):
        return self.__tiempo
    
    @property
    def restante(self):
        return self.__restante
    
    @property
    def resultado(self):
        return self.__resultado