import java.util.Scanner;

/*
El programa pedirá por pantalla una cantidad de dinero en euros y devuelve la conversión en USD
El mensaje con el resultado será: *** Euros equivalen a *** USD
 */

public class Conversor {

    public static void main(String[] args) {
        System.out.println("¡Bienvenido al Conversor de Monedas");
        System.out.println("Por favor introduzca una cantidad en euros y el sistema le indicará su equivalente en USD");

        Scanner scanner = new Scanner(System.in);

        double euros = scanner.nextDouble();

        double dolares = 1.09 * euros;

        System.out.println(euros + " Euros equivalen a: " + dolares + " $");
    }
}
