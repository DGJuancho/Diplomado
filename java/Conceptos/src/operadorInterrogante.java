import java.util.Scanner;

public class operadorInterrogante {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Introduzca un número entero: ");
        int dividendo = scanner.nextInt();
        System.out.println("Introduzca otro número entero: ");
        int divisor = scanner.nextInt();
        int resultado;
        /* if (divisor ==0) {
            resultado = 0;
        } else {
            resultado = dividendo / divisor;
        }*/
        resultado = divisor ==0?0:dividendo / divisor;

        /* Se interpreta: si el divisor es igual a 0 entonces,
         el resultado es igual a lo indicado en el lado izquierdo de los dos puntos ":"
         sino, el resultado es igual a lo expresado a la derecha de los dos puntos*/

        System.out.println("El resultado de dividir " + dividendo + " entre " + divisor + " es: " + resultado);
    }
}
