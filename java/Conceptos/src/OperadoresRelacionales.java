public class OperadoresRelacionales {
    public static void main(String[] args) {
        boolean esMayorQue = 1 > 2;

        System.out.println("Es cierto que 1 es mayor que 2? " + esMayorQue);

        boolean esMenorQue = 1.5 < 7.2;

        System.out.println("Es cierto que 1.5 es menor que 7.2? " + esMenorQue);

        boolean esMayorOIgualQue = 8 >= 8;

        System.out.println("Es cierto que 8 es mayor o igual que 8? " + esMayorOIgualQue);

        boolean esMenorOIgualQue = 3.5 <= 1.5;

        System.out.println("Es cierto que 3.5 es menor o igual que 1.5? " + esMenorOIgualQue);

        boolean esIgualQue = 6==6;

        System.out.println("Es cierto que 6 es igual a 6? " + esIgualQue);

        boolean esDiferente =  4 != 2+2;

        System.out.println("Es cierto que 4 es diferente de 2+2? " + esDiferente);
    }
}
