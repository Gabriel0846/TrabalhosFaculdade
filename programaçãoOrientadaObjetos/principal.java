package programaçãoOrientadaObjetos;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

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
            scanner.nextLine(); // limpa o buffer do scanner

            switch (opcao) {
                case 1:
                    menuAdicionarMoeda(scanner, cofrinho);
                    break;
                case 2:
                    menuRemoverMoeda(scanner, cofrinho);
                    break;
                case 3:
                    cofrinho.listarMoedas();
                    pause(); // pausa para o usuário visualizar
                    break;
                case 4:
                    System.out.println("Total em Reais: " + cofrinho.calcularTotalEmReais());
                    pause(); // pausa para o usuário visualizar
                    break;
                case 5:
                    System.out.println("Saindo...");
                    break;
                default:
                    System.out.println("Opção inválida!");
                    pause(); // pausa para o usuário visualizar
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

        pause(); // pausa para o usuário visualizar
    }

    // Função para menu de remoção de moeda
    private static void menuRemoverMoeda(Scanner scanner, Cofrinho cofrinho) {
        System.out.println("Escolha o tipo da moeda a ser removida: ");
        System.out.println("1 - Dólar");
        System.out.println("2 - Euro");
        System.out.println("3 - Real");
        System.out.print("Escolha uma opção: ");
        int tipoMoeda = scanner.nextInt();
        scanner.nextLine(); // limpa o buffer do scanner

        switch (tipoMoeda) {
            case 1:
                removerMoedaTipo(scanner, cofrinho, Dolar.class);
                break;
            case 2:
                removerMoedaTipo(scanner, cofrinho, Euro.class);
                break;
            case 3:
                removerMoedaTipo(scanner, cofrinho, Real.class);
                break;
            default:
                System.out.println("Opção inválida!");
        }

        pause(); // pausa para o usuário visualizar
    }

    // Método para remover moeda de um tipo específico (Dólar, Euro, Real)
    private static void removerMoedaTipo(Scanner scanner, Cofrinho cofrinho, Class<? extends Moeda> tipoMoeda) {
        // Lista as moedas do tipo selecionado
        System.out.println("Lista de moedas do tipo " + tipoMoeda.getSimpleName() + ":");
        boolean encontrouMoeda = false;
        for (Moeda moeda : cofrinho.getMoedas()) {
            if (tipoMoeda.isInstance(moeda)) {
                System.out.println(moeda.info());
                encontrouMoeda = true;
            }
        }

        if (!encontrouMoeda) {
            System.out.println("Não há moedas desse tipo no cofrinho.");
            pause();
            return;
        }

        // Solicita o valor exato da moeda para remoção
        boolean entradaValida = false;
        double valorRemover = 0;
        
        while (!entradaValida) {
            System.out.print("Digite o valor exato da moeda que deseja remover: ");
            String input = scanner.nextLine();  // Lê a linha inteira
            
            try {
                valorRemover = Double.parseDouble(input);  // Tenta converter a entrada para double
                entradaValida = true;  // Se conseguir, marca como entrada válida
            } catch (NumberFormatException e) {
                System.out.println("Valor inválido! Por favor, insira um número válido.");
            }
        }

        // Processo de remoção
        boolean moedaRemovida = false;
        for (Moeda moeda : cofrinho.getMoedas()) {
            if (tipoMoeda.isInstance(moeda) && moeda.getValor() == valorRemover) {
                cofrinho.removerMoeda(moeda);
                moedaRemovida = true;
                break;
            }
        }

        if (moedaRemovida) {
            System.out.println("Moeda removida com sucesso!");
        } else {
            System.out.println("Moeda não encontrada com o valor informado.");
        }

        pause(); // Pausa para o usuário visualizar
    }

    // função de pausa
    private static void pause() {
        System.out.println("Pressione Enter para continuar...");
        Scanner scanner = new Scanner(System.in);
        scanner.nextLine();
    }
}

class Cofrinho {
    private List<Moeda> moedas = new ArrayList<>();

    // Método para adicionar moeda ao cofrinho
    public void adicionarMoeda(Moeda moeda) {
        for (Moeda m : moedas) {
            if (m.getClass().equals(moeda.getClass())) {
                // Se a moeda já existir no cofrinho, somar o valor
                m.setValor(m.getValor() + moeda.getValor());
                return;
            }
        }
        // Se não existir, adicionar nova moeda
        moedas.add(moeda);
    }

    // Método para listar moedas
    public void listarMoedas() {
        if (moedas.isEmpty()) {
            System.out.println("O cofrinho está vazio.");
        } else {
            System.out.println("Moedas no cofrinho:");
            for (Moeda moeda : moedas) {
                System.out.println(moeda.info());
            }
        }
    }

    // Método para calcular o total em Reais
    public double calcularTotalEmReais() {
        double total = 0;
        for (Moeda moeda : moedas) {
            total += moeda.converterParaReal();
        }
        return total;
    }

    public List<Moeda> getMoedas() {
        return moedas;
    }

    public void removerMoeda(Moeda moeda) {
        moedas.remove(moeda);
    }
}

