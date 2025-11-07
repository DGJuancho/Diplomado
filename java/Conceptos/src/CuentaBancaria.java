public class CuentaBancaria {
    String titular;
    TipoDeCuenta tipoDeCuenta;
    double saldo;

    final double COMISION = 1.2;

    CuentaBancaria(String t, TipoDeCuenta tipo, double s){
    titular = t;
    tipoDeCuenta = TipoDeCuenta;
    saldo = s;
    }

    CuentaBancaria(String t, double s){
        titular = t;
        tipoDeCuenta = TipoDeCuenta.AHORRO;
        saldo = s;
    }

    CuentaBancaria(){
        tipoDeCuenta = TipoDeCuenta.AHORRO;
    }

    void ingresarDinero(double cantidad) {
        if (cantidad < 0) {
            return;
        }
        saldo += cantidad;
    }

    void sacarDinero(double cantidad) {
        if (cantidad < 0) {
            return;
        }
        double comision = calcularComision();
        saldo -= cantidad;
        saldo -= comision;
    }

    double calcularComision(){
        switch (tipoDeCuenta){
            case AHORRO:
                return COMISION;
            case NOMINA:
                return 0;
        }
    }

    void cambiarTipoDeCuenta(TipoDeCuenta nuevoTipo) {
        tipoDeCuenta = nuevoTipo;
    }

    double obtenerSaldo () {
        return saldo;
    }
}


