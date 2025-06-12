import java.util.Scanner;

public class EstructuraSwitch {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Por favor introduzca el día de la semana en que desea su cita: ");
        String dia = scanner.nextLine();
        String color;
        switch (dia) {
            case "lunes":
            case "miercoles":
                System.out.println("El " + dia + " puede venir de 11:00 a 12:00");
                break;
            case "martes":
            case "jueves":
                System.out.println("El " + dia + " puede venir de 03:00 a 04:00");
                break;
            case "viernes":
                System.out.println("El " + dia + " puede venir de 04:00 a 05:00");
                break;
            case "sabado":
            case "domingo": {
                color = "\033[0;31m";
                System.out.println(color + "El " + dia + " No trabajamos");
                break;}
            default:
                System.out.println("No es un día válido");
        }
    }
}
