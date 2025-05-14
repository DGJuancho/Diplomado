public class Casteo {
    public static void main(String[] args) {
        int variableInt = 10;
        float variableFloat = variableInt;

        double variableDouble = variableFloat;

        double otherDouble = 7.76;

//Para castear el valor de la derecha colocamos el tipo (int) al que queremos castear el valor de la izquierda
        int otherInt = (int) otherDouble;

        System.out.println("El resultado del casteo de la variable es: " + otherInt);

        byte variable1 = 50;
        byte variable2 = 100;

        byte suma = (byte) (variable1 + variable2);

        System.out.println ("El resultado del casteo a byte es: " + suma);
    }
}
