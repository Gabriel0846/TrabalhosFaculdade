import java.util.Scanner;

public class Principal {

    public static void main(String[] args) {
        // criação de um scanner para ler entradas do usuario
        Scanner scanner = new Scanner(System.in);
        
        // criação do cofrinho onde as moedas serão armazenadas
        Cofrinho cofrinho = new Cofrinho();
        
        // variavel para controlar o loop do menu
        boolean continuar = true;

        // laço para exibir o menu e permitir que o usuário escolha opções
        while (continuar) {
            // exibição do menu com opções disponíveis
            System.out.println("\nMenu:");
            System.out.println("1. Adicionar moeda");
            System.out.println("2. Remover moeda");
            System.out.println("3. Listar moedas");
            System.out.println("4. Calcular total convertido para Real");
            System.out.println("5. Encerrar");
            System.out.print("Escolha uma opção: ");
            
            // leitura da opção escolhida pelo usuário
            int opcao = scanner.nextInt();

            // estrutura de controle switch para tratar as opções do menu
            switch (opcao) {
                case 1:
                    // caso o usuário queira adicionar uma moeda
                    System.out.println("\nEscolha a moeda:");
                    System.out.println("1. Real");
                    System.out.println("2. Dolar");
                    System.out.println("3. Euro");
                    int tipoMoeda = scanner.nextInt();  // leitura do tipo de moeda
                    System.out.print("Digite o valor da moeda: ");
                    double valor = scanner.nextDouble();  // leitura do valor da moeda

                    // condicional para adicionar a moeda no cofrinho
                    if (tipoMoeda == 1) {
                        cofrinho.adicionarMoeda(new Real(valor));  // adiciona Real
                    } else if (tipoMoeda == 2) {
                        cofrinho.adicionarMoeda(new Dolar(valor));  // adiciona Dolar
                    } else if (tipoMoeda == 3) {
                        cofrinho.adicionarMoeda(new Euro(valor));  // adiciona Euro
                    } else {
                        System.out.println("Opção invalida.");
                    }
                    break;

                case 2:
                    // caso o usuario queira remover uma moeda
                    System.out.println("\nEscolha a moeda para remover:");
                    System.out.println("1. Real");
                    System.out.println("2. Dolar");
                    System.out.println("3. Euro");
                    tipoMoeda = scanner.nextInt();  // leitura do tipo de moeda
                    System.out.print("Digite o valor da moeda a ser removida: ");
                    valor = scanner.nextDouble();  // leitura do valor da moeda a ser removida

                    // condicional para remover a moeda do cofrinho
                    if (tipoMoeda == 1) {
                        cofrinho.removerMoeda(new Real(valor));  // remove real
                    } else if (tipoMoeda == 2) {
                        cofrinho.removerMoeda(new Dolar(valor));  // remove dolar
                    } else if (tipoMoeda == 3) {
                        cofrinho.removerMoeda(new Euro(valor));  // remove euro
                    } else {
                        System.out.println("Opção invalida.");
                    }
                    break;

                case 3:
                    // caso o usuario queira listar as moedas no cofrinho
                    cofrinho.listarMoedas();
                    break;

                case 4:
                    // caso o usuario queira calcular o total das moedas convertido para Real
                    System.out.println("Total convertido para Real: " + cofrinho.calcularTotalConvertido());
                    break;

                case 5:
                    // caso o usuario queira encerrar o programa
                    continuar = false;  // encerra o loop
                    System.out.println("Programa encerrado.");
                    break;

                default:
                    // caso o usuário escolha uma opção invalida
                    System.out.println("Opção invalida.");
            }
        }

        // fecha o scanner após a execução do programa para liberar o recurso
        scanner.close();
    }
}
