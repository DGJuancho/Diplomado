public class TiposDeDatosPrimitivos {
    public static void main(String[] args) {
        byte elMenorByte = Byte.MIN_VALUE;
        byte elMayorByte = Byte.MAX_VALUE;

        System.out.println("El tipo \"byte\" es un número entero de 8 bits con signo. Está comprendido entre " + elMenorByte + " y " + elMayorByte);

        System.out.println("El tipo \"short\" es un número entero de 16 bits con signo. Está comprendido entre " + Short.MIN_VALUE + " y " + Short.MAX_VALUE);

        System.out.println("El tipo \"int\" es un número entero de 32 bits con signo. Está comprendido entre " + Integer.MIN_VALUE + " y " + Integer.MAX_VALUE);

        System.out.println("El tipo \"long\" es un número entero de 64 bits con signo. Está comprendido entre " + Long.MIN_VALUE + " y " + Long.MAX_VALUE);

        float variableFloat = 5.6f;

        double variableDouble = 6.6;

        char variablechar = 'a';

        boolean trueBoolean = true;

        boolean falseBoolean = false;
    }
}
