public class Literales {
    public static void main(String[] args) {
        int enteroDecimal= 100;

        int enteroOctal = 0100;

        int enteroHexadecimal = 0x100;

        System.out.println("Entero decimal es: " + enteroDecimal);
        System.out.println("Entero octal es: " + enteroOctal);
        System.out.println("Entero hexadecimal es: " + enteroHexadecimal);

        long numeroLong = 100L;

        double numeroDouble = 2.5;

        float numeroFloat = 2.5f;

        int numeroConGuionesBajos = 25_258_236;

        System.out.println("El número con guiones es: " + numeroConGuionesBajos);

        char miChar = 'b';

        char miUnicode = '\u0062';

        System.out.println("El caracter miUnicode es: " + miUnicode);

        char comillaSimple = '\'';

        String stringLiteral = "Esto es un literal";

        boolean booleanVerdadero = true;

        String stringNulo = null;
    }
}
