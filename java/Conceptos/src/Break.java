public class Break {
    public static void main(String[] args) {
        int numeroEncontrado;
        for (numeroEncontrado = 2567; numeroEncontrado <= 3642; numeroEncontrado++) {
            System.out.println("Será el número? " + numeroEncontrado);
            if ((numeroEncontrado % 2 == 0) && (numeroEncontrado % 3 == 0) && (numeroEncontrado % 5 ==0)) {
                break;
            }
        }
        if (numeroEncontrado > 3642) {
            System.out.print("No hay ningún número entre 2567 y 3642 que sea múltiplo de 2, de 3 y de 5 de manera simultánea");
        } else {
            System.out.println("El primer múltiplo de 2, 3, y 5 entre 2567 y 3642 es: " + numeroEncontrado);
        }
    }
}
