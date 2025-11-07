public class Main {
    public static void main(String[] args) {
        CuentaBancaria cuentaDeJuan = new CuentaBancaria("Juan C. Nunez", "ahorros", 23500 );

        CuentaBancaria cuentaDeMaria = new CuentaBancaria("María Pérez", CuentaBancaria.TIPO_NOMINA,25000);

        CuentaBancaria cuentaDeAna = new CuentaBancaria("Ana García", TipoDeCuenta.INFANTIL, 15000);

        double saldo = cuentaDeJuan.obtenerSaldo();
        System.out.println("El saldo de la cuenta de Juan es: " + saldo);

        cuentaDeJuan.sacarDinero( -1000);
       System.out.println("El saldo de la cuenta de Juan es: " + saldo);
    }
}
