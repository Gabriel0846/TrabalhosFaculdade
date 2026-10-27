package empresa;

public class App {
    public static void main(String[] args){
        Funcionario f = new Funcionario("Mario", "111.222.333-00");
        Carro c = new Carro("Palio", "cinza", 4);
        Quadrado q = new Quadrado(10);

        Imprimivel i = f;
        i.imprimir();
        i=c;
        i.imprimir();
        i=q;
        i.imprimir();
    }
}
