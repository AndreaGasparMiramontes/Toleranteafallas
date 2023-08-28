# Manejo de excepciones en C#

Al igual que la mayoria de lenguajes C# tambien hace uso de la instruccion try catch solo que en su caso se tiene un par de instrucciones extra a las que ya se conocen

Try: indica el segmento de codigo que se va a intentar ejecutar
Catch: atrapa cualquier error que pueda suceder en tiempo de ejecución
Throw: relanza la excepcion (imprime en pantalla lo que sucedió)
Finally: codigo que independientemente de si se ejecuto el codigo o si dio error va a pasar

En C# hay diversas excepciones que pueden suceder y ya estan definidas en el lenguaje como lo son:

AccessViolationException: se genera cuando se intenta leer o escribir en la memoria protegida.
AppDomainUnloadedException: se genera cuando se intenta acceder a un dominio de aplicación que aún no se ha cargado.
ApplicationException: se genera cuando ocurre un error de la aplicación que no es fatal.
ArgumentException: se genera cuando se pasa un argumento inválido a un método.
ArgumentNullException: se genera cuando se pasa un argumento nulo a un método que no lo admite.
ArgumentOutOfRangeException: se genera cuando se pasa un argumento que está fuera del rango esperado por un método.
ArithmeticException: se genera cuando ocurre un error aritmético, como una división por cero o un desbordamiento.
DivideByZeroException: se genera cuando se intenta dividir un número por cero.
FormatException: se genera cuando se intenta convertir una cadena a un tipo que no tiene el formato adecuado.
IndexOutOfRangeException: se genera cuando se intenta acceder a un elemento de una matriz o una colección con un índice que está fuera de los límites.
InvalidCastException: se genera cuando se intenta realizar una conversión inválida entre tipos.
InvalidOperationException: se genera cuando se intenta realizar una operación que no es válida en el estado actual del objeto.
NullReferenceException: se genera cuando se intenta acceder a un miembro de un objeto nulo.
OutOfMemoryException: se genera cuando no hay suficiente memoria para continuar la ejecución del programa.
OverflowException: se genera cuando ocurre un desbordamiento aritmético o de conversión.
StackOverflowException: se genera cuando hay demasiadas llamadas recursivas o anidadas en la pila.

Y otras más...

De igual forma en caso de querer hacer uso de una excepción que no existe previamente esta se puede definir como una hija de la clase padre "exception"
