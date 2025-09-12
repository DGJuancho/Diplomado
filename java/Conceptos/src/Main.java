public class Main {
    public static void main(String[] args) {
        CuentaBancaria cuentaDeJuan = new CuentaBancaria();
        cuentaDeJuan.titular = "Juan C. Núñez";
        cuentaDeJuan.tipoDeCuenta = "nómina";
        cuentaDeJuan.saldo = 23500;

        cuentaDeJuan.sacarDinero(500);
        System.out.println("Ahora la cuenta de Juan tiene " + cuentaDeJuan.saldo);

        cuentaDeJuan.ingresarDinero(1000);
        System.out.println("Ahora,al ingresar dinero,  la cuenta de Juan tiene " + cuentaDeJuan.saldo);

        cuentaDeJuan.cambiarTipoDeCuenta("ahorro");
        System.out.println("la cuenta de Juan ahora es: " + cuentaDeJuan.tipoDeCuenta);
    }
}
