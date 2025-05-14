public class OperadoresAritmeticos {
    public static void main(String[] args) {
        int numero2 = 2;
        int numero3 = 3;

        int resultadoSuma = numero2 + numero3;
        //El operador + se utiliza para sumar
        System.out.println("El resultado de sumar " +  numero2 + " y " + numero3 + " es igual a = " + resultadoSuma);
        //También se utiliza para concatenar string
        System.out.println("Esto es un string " + "y lo concatenamos con este otro");
        //El operador - funciona para restar
        int resultadoResta = numero3 - numero2;
        //También sirve para realizar el cambio de signo
        int numeroConCambioDeSigno = - numero2;

        System.out.println("El resultado de restar " + numero3 + " y " + numero2 + " es igual a = " + resultadoResta);
        System.out.println("Si utilizamos el operador de resta a la variables, vamos a obtener " + numeroConCambioDeSigno);

        //El operador * funciona para multiplicar
        double resultadoMultiplicacion = numero3 * 3.5;
        System.out.println("El resultado de multiplicar 3 por 3.5 es igual a: " + resultadoMultiplicacion);
        //El operador / funcionara para dividir
        double resultadoDivision = (double)numero2 / numero3;
        System.out.println("El resultado de dividir 2 entre 3 es igual a: " + resultadoDivision);
        //El operador % funciona para calcular el resto en una división
        double resultadoModulo = (double)numero3 % numero2;
        System.out.println("El resto de dividir 3 entre 2 es: " + resultadoModulo);
    }
}
