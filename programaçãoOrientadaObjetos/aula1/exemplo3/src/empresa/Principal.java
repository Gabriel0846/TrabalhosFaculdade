package empresa;

import java.util.Scanner;

public class Principal {

    public static void main(String[] args) {
        
        Scanner teclado = new Scanner(System.in);
        int palpite;
        int valorCorreto = 10000;
        System.out.println("Digite seu palpite: ");
        palpite = teclado.nextInt();
        
        while (palpite != valorCorreto) {

            msg = palpite>valorCorreto?"Um pouco menos...":"um pouco mais";
            System.out.println(msg);
            /*if (palpite < valorCorreto) {
                System.out.println("Um pouco mais... ");
            } else {
                System.out.println("Um pouco menos... ");
            }*/
            System.out.println("Digite outro palpite: ");
            palpite = teclado.nextInt();
        }
        System.out.println("Parabéns! Você acertou!");
    }
}
