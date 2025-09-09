public class Main {
    public static void main(String[] args) {
        CuentaBancaria cuentaDeJuan = new CuentaBancaria();
        cuentaDeJuan.titular = "Juan C. Núñez";
        cuentaDeJuan.tipoDeCuenta = "nómina";
        cuentaDeJuan.saldo = 23500;

        System.out.println("Cuále es el saldo disponible de la Cuenta de Juan?\n$ " + cuentaDeJuan.saldo);
    }
}
