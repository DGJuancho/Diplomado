import java.util.Scanner;

public class BucleWhile {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Por favor, introduce el número del que quieras saber la raíz cuadrada: ");
        double  numero = scanner.nextDouble();
        double candidatoRaiz = 0.0;
        while (candidatoRaiz * candidatoRaiz <= numero) {
            candidatoRaiz += 0.01;
            System.out.println("¿Será el numero " + candidatoRaiz + " su cuadrado?" + " Su cuadrado es: " + candidatoRaiz * candidatoRaiz);
        }
        candidatoRaiz -= 0.01;
        System.out.println("La raiz cuadrada calculada de manera manual es: " + candidatoRaiz);
        System.out.println("La raíz cuadrada real es: " + Math.sqrt(numero));
    }
}
