import java.util.Scanner;

public class BucleDoWhile {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double numero;
        do{
            System. out.println("Introduzca un número y le mostraremos la raíz cuadrada. Para salir introduzca 0");
            numero = scanner.nextDouble();
            if (numero == 0) {
                System.out.println("Hasta pronto!");
            } else {
                System.out.println("La raíz cuadrada de: " + numero + " es: " + Math.sqrt(numero));
            }
        }while(numero !=0);
    }
}
