/*
Programa que emula la interfaz de una cajero automático. el programa presentará las siguientes opciones al usuario:

Elija una de las siguientes opciones:
    escriba 1 para consultar su saldo
    Escriba 2 para ingresar dinero
    Escriba 3 para retirar dinero
    Escriba 4 para consultar sus últimos movimientos
Una vez escrita la opción, pulsa la tecla enter

Una vez que el usuario a elegido la opción, el programa le mostrará por pantalla el número correspondiente a la opción elegida.

 */

import java.util.Scanner;

public class Interfaz {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Elija una de las siguientes opciones:");
        System.out.println();
        System.out.println("1)  Saldo");
        System.out.println("2)  Depósito");
        System.out.println("3)  Retiro");
        System.out.println("4)  Últimos movimientos");
        System.out.println();

        int opcionSeleccionada = scanner.nextInt();

        System.out.println();
        System.out.println("Usted eligio la opción: " + opcionSeleccionada);
    }
}
