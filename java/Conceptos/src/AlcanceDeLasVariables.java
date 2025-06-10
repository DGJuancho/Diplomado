public class AlcanceDeLasVariables {
    public static void main(String[] args) {
        int dias = 0;

        while (dias < 30) {
            dias = dias + 1;
            int semanas = dias/7;
            System.out.println("Han pasado " + dias + " días, lo que supone " + semanas + " semanas");

        }
    }
}
