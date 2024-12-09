package programaçãoOrientadaObjetos;

import java.util.Scanner;

public class principal {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Cofrinho cofrinho = new Cofrinho();
        int opcao;
        
        // menu principal
        do {
            System.out.println("----------- MENU -----------");
            System.out.println("1 - Adicionar moeda");
            System.out.println("2 - Remover moeda");
            System.out.println("3 - Listar moedas");
            System.out.println("4 - Calcular total em Reais");
            System.out.println("5 - Sair");
            System.out.print("Escolha uma opção: ");
            opcao = scanner.nextInt();
            scanner.nextLine();// limpa o buffer do scanner

            switch (opcao) {
                case 1:
                    menuAdicionarMoeda(scanner, cofrinho);
                    break;
                case 2:
                    menuRemoverMoeda(scanner, cofrinho);
                    break;
                case 3:
                    cofrinho.listarMoedas();
                    pause(); // pausa para o usuario visualizar
                    break;
                case 4:
                    System.out.println("Total em Reais: " + cofrinho.calcularTotalEmReais());
                    pause(); // pausa para o usuario visualizar
                    break;
                case 5:
                    System.out.println("Saindo...");
                    break;
                default:
                    System.out.println("Opção invalida!");
                    pause(); // pausa para o usuario visualizar
            }
        } while (opcao != 5);

        scanner.close();
    }

    // função para adicionar moeda
    private static void menuAdicionarMoeda(Scanner scanner, Cofrinho cofrinho) {
        System.out.println("Escolha o tipo da moeda: ");
        System.out.println("1 - Dólar");
        System.out.println("2 - Euro");
        System.out.println("3 - Real");
        System.out.println("4 - Voltar");
        System.out.print("Escolha uma opção: ");
        int tipoMoeda = scanner.nextInt();
        scanner.nextLine(); // limpa o buffer do scanner

        if (tipoMoeda == 4) {
            return; // volta para o menu principal
        }

        System.out.print("Digite o valor da moeda: ");
        double valor = scanner.nextDouble();
        scanner.nextLine(); // limpa o buffer do scanner

        switch (tipoMoeda) {
            case 1:
                cofrinho.adicionarMoeda(new Dolar(valor));
                break;
            case 2:
                cofrinho.adicionarMoeda(new Euro(valor));
                break;
            case 3:
                cofrinho.adicionarMoeda(new Real(valor));
                break;
            default:
                System.out.println("Opção inválida!");
        }

        pause(); // pausa para o usuario visualizar
    }

    // função para remover moeda
    private static void menuRemoverMoeda(Scanner scanner, Cofrinho cofrinho) {
        cofrinho.listarMoedas();
        System.out.println("Escolha a moeda a ser removida (informe o valor exato): ");
        double valorRemover = scanner.nextDouble();
        scanner.nextLine(); // limpa o buffer do scanner

        boolean moedaRemovida = false;
        for (Moeda moeda : cofrinho.getMoedas()) {
            if (moeda.getValor() == valorRemover) {
                cofrinho.removerMoeda(moeda);
                moedaRemovida = true;
                break;
            }
        }

        if (moedaRemovida) {
            System.out.println("Moeda removida com sucesso!");
        } else {
            System.out.println("Moeda não encontrada!");
        }

        pause(); // pausa para o usuário visualizar
    }

    // função de pausa
    private static void pause() {
        System.out.println("Pressione Enter para continuar...");
        Scanner scanner = new Scanner(System.in);
        scanner.nextLine();
    }

}
