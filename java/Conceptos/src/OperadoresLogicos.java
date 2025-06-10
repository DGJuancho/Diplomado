public class OperadoresLogicos {
    public static void main(String[] args) {

//Operador and (&) es true si los dos operandos es true
        System.out.println("False & False es: " + (false & false));
        System.out.println("True & False es: " + (true & false));
        System.out.println("False & True es: " + (false & true));
        System.out.println("True & True es: " + (true & true));
// El operador and (&&) de circuito corto evalúa el primer operando, si este es false, la operación es false, no continua evaluando, de esta manera es más eficiente

//Operador or (|) es true, si alguno de los 2 operandos es true
        System.out.println("False | False es: " + (false | false));
        System.out.println("True | False es: " + (true | false));
        System.out.println("False | True es: " + (false | true));
        System.out.println("True | True es: " + (true | true));
// El operador or (||) de circuito corto evalúa el primer operando, si este es true, la operación es true, no continua evaluando, de esta manera es más eficiente

//Operador xor (^) es true, sólo si uno de los operandos es true
        System.out.println("False ^ False es: " + (false ^ false));
        System.out.println("True ^ False es: " + (true ^false));
        System.out.println("False ^ True es: " + (false ^ true));
        System.out.println("True ^ True es: " + (true ^ true));

//Operador not (!) usa un solo operando y niega lo que siga
        System.out.println("!False es: " + !false);
        System.out.println("!True es: " + !true);
    }
}
