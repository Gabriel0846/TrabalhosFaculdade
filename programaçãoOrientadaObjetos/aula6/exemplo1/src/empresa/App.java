package empresa;

import java.util.Scanner;

public class App {
    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);
        Conta c1 = new Conta("Mario", 5000);
        Conta c2 = new Conta("Luigi",2000);

        c1.info();
        c2.info();

        System.out.println("Digite um valor para transferir: ");
        double valorTransferir = teclado.nextDouble();

        boolean sucessoLeitura = false;
        while (!sucessoLeitura) {
            try {
                c1.transferir(valorTransferir, c2);
                c1.info();
                c2.info();
                sucessoLeitura = true;
            } catch (Exception e) {
                System.out.println("Ocorreu um problema, digite outro valor");
                System.out.println(e.getMessage());
                System.out.println("Digite um valor para transferir: ");
                valorTransferir = teclado.nextDouble();
            }
        }

        
        
    }
}
