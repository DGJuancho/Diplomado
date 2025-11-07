public class Main {
    public static void main(String[] args) {
/*        CuentaBancaria cuentaDeJuan = new CuentaBancaria("Juan Núñez", TipoDeCuenta.AHORRO, 23500);

        CuentaBancaria cuentaDeMaria = new CuentaBancaria("María Pérez", 25000);

        CuentaBancaria cuentaDeAna = new CuentaBancaria("Ana García", TipoDeCuenta.INFANTIL, 15000);

        double saldo = cuentaDeJuan.obtenerSaldo();
        System.out.println("El saldo de la cuenta de Juan es: " + saldo);

        cuentaDeJuan.sacarDinero(1000);

        double saldoFinal = cuentaDeJuan.obtenerSaldo();
        System.out.println("El saldo de la cuenta de Juan es: " + saldoFinal);*/

        Informador informador = new Informador();

        informador.mostrarPorPantalla(3);

        byte unByte = 2;

        informador.mostrarPorPantalla(unByte);

        informador.mostrarPorPantalla(3.5);

        informador.mostrarPorPantalla("Hola Mundo");

        informador.mostrarPorPantalla("Hola", informador.COLOR_AMARILLO);

    }
}
