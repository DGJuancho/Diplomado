import java.util.Scanner;

public class SentenciaIf {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numeroPensado = 3;
        System.out.println("Adivina que número estoy pensando (Del 1 al 10)");
        int numeroIntroducido = scanner.nextInt();
        String color;
        if (numeroPensado ==numeroIntroducido) {
            color = "\033[0;32m";
            System.out.println(color + "¡Excelente, lo adivinaste!");
        }
        else {
            color = "\033[0;31m";
            System.out.println(color + "¡Sorry, el " + numeroIntroducido + " no es el número que estaba pensando");
        }
    }
}
