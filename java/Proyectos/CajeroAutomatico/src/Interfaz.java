import java.util.Scanner;

/*
Programa que emula la interfaz de una cajero automático. el programa presentará las siguientes opciones al usuario:

Elija una de las siguientes opciones:
    escriba 1 para consultar su saldo
    Escriba 2 para ingresar dinero
    Escriba 3 para retirar dinero
    Escriba 4 para consultar sus últimos movimientos
Para salir, escriba cualquier otro número

Una vez escrita la opción, pulsa la tecla enter

Una vez que el usuario a elegido la opción, el programa le mostrará por pantalla el número correspondiente a la opción elegida.

 */

public class Interfaz {
    public static void main(String[] args) {

        int opcionSeleccionada;

        Scanner scanner = new Scanner(System.in);

        do {
            System.out.println();
            System.out.println("Elija una de las siguientes opciones:");
            System.out.println();
            System.out.println("1)  Saldo");
            System.out.println("2)  Depósito");
            System.out.println("3)  Retiro");
            System.out.println("4)  Últimos movimientos");
            System.out.println("    \"Para salir, escriba cualquier otro número\"");
            System.out.println();

            opcionSeleccionada = scanner.nextInt();
            System.out.println();

            switch (opcionSeleccionada) {
                case 1:
                    System.out.println("La opción que usted ha elegido es: \"Consultar Saldo\"");
                    break;
                case 2:
                    System.out.println("La opción que usted ha elegido es: \"Realizar un Depósito\"");
                    break;
                case 3:
                    System.out.println("La opción que usted ha elegido es: \"Realizar un Retiro\"");
                    break;
                case 4:
                    System.out.println("La opción que usted ha elegido es: \"Consultar los últimos movimientos\"");
                    break;
                default:
                    System.out.println("\"GRACIAS POR UTILIZAR NUESTROS SERVICIOS\"");
            }

        } while  (opcionSeleccionada == 1 || opcionSeleccionada == 2 || opcionSeleccionada == 3 || opcionSeleccionada ==4 );

    }
}
