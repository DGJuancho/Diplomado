public class OperadorAsignacion {
    public static void main(String[] args) {
        int variable;
        variable = 3;
        int variable2;
        variable2 = 8*9+95;
        int a, b, c;
        a = b = c = 8;

        System.out. println("¿Qué valor tiene c = 8? " + (c = 8));
        System.out. println("¿Qué valor tiene b = c = 8? " + (b = c = 8));
        System.out. println("¿Qué valor tiene varible2? " + (variable2));

        int x = 10;
        x = x + 3;

        System.out.println("El valor de la variable x es: " + x);

        // Operador de asginación abreviado "+="
        int i = 10;
        i+=3;
        System.out.println("El valor de la variable i es: " + i);
    }
}
