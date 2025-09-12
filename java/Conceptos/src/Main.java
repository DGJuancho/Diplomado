public class Main {
    public static void main(String[] args) {
        CuentaBancaria cuentaDeJuan = new CuentaBancaria();
        cuentaDeJuan.titular = "Juan C. Núñez";
        cuentaDeJuan.tipoDeCuenta = "nómina";
        cuentaDeJuan.saldo = 23500;

        double saldo = cuentaDeJuan.obtenerSaldo();
        System.out.println("El saldo de la cuenta de Juan es: " + saldo);

        cuentaDeJuan.sacarDinero( -1000);
        System.out.println("El saldo de la cuenta de Juan es: " + saldo);
    }
}
