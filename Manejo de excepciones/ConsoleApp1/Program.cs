class Program
{
    static void Main(string[] args)
    {
        try
        {
            Console.WriteLine("Introduce un número:");
            int num = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("El doble del número es: " + num * 2);
        }
        catch (FormatException ex) //en caso de que se introduzca algo que no se pueda convertir a
                                   //int32 se procede a hacer lo siguiente:
        {
            Console.WriteLine("No has introducido un número válido.");
            throw; // Imprime en pantalla la excepcion que se acaba de efectuar
        }
        finally
        {
            Console.ReadLine(); //Este código siempre se va a ejecutar
        }
    }
}

