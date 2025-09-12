public class CuentaBancaria {
    String titular;
    String tipoDeCuenta;
    double saldo;

    void ingresarDinero(double cantidad) {
        saldo += cantidad;
    }

    void sacarDinero(double cantidad) {
        saldo -= cantidad;
    }

    void cambiarTipoDeCuenta(String nuevoTipo) {
        tipoDeCuenta = nuevoTipo;
    }
}
