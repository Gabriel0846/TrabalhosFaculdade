package empresa;

import java.util.Scanner;

public class Principal {
    public static void main(String[] args)  {

        int idade = 10;

        idade = idade +2;
        String nome = "Mario";
        double peso = 72.5;
        float peso2 = 80.6f;
        
        Scanner teclado = new Scanner(System.in);

        System.out.println("Digite idade, peso e nome: ");
        idade = teclado.nextInt();
        peso = teclado.nextDouble();
        nome = teclado.next();

        System.out.println("Nome: "+ nome);
        System.out.printf("Idade: %d\n", idade);
        System.out.printf("Peso: %.2f\n", peso);

        if(idade <18){
            System.out,println("Acesso bloqueado");
        }
        else if (idade <65) {
            System.out.println("Adulto");
        }
        else {
            System.out.println("adulto idoso");
        }
        
    }
}
