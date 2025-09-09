public class PasoPorReferencia {
    public static void main(String[] args) {
        int variable1 = 23;
        int variable2 = variable1;
        System.out.println("El valor de variable 1 es: " + variable1);
        System.out.println("El valor de variable 2 es: " + variable2);

        variable2 = 78;

        System.out.println("El valor de variable 1 es: " + variable1);
        System.out.println("El valor de variable 2 es: " + variable2);

        CuentaBancaria cuentaDeJuan = new CuentaBancaria();
        cuentaDeJuan.saldo = 23500;

        CuentaBancaria cuentaDeAna = cuentaDeJuan;
        cuentaDeAna.saldo = 10000;

        System.out.println("El Saldo de la cuenta de Juan es: $ " + cuentaDeJuan.saldo);
        System.out.println("El Saldo de la cuenta de Ana es: $ " + cuentaDeAna.saldo);

    }
}
