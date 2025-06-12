import java.util.Scanner;

public class BucleFor {
    public static void main(String[] args) {
        Scanner scanner = new Scanner (System.in);
        System.out.println ("Por favor, introduzca el primer número");
        int firstOper = scanner.nextInt();
        System.out.println ("Por favor, introduzca el segundo número");
        int secondOper = scanner.nextInt();
        int resultado = 0;
        for (int i = 0; i<secondOper; i++) {
            System.out.println("Iteración: " + i);
            resultado += firstOper;
        }
        System.out.println("El resultados de multiplicar " + firstOper + " por " + secondOper + " es: " + resultado);
    }
}
