import java.util.ArrayList;

public class Cofrinho {
    // lista que vai armazenar as moedas no cofrinho
    private ArrayList<Moeda> moedas;

    // construtor da classe Cofrinho.
    public Cofrinho() {
        moedas = new ArrayList<>(); // inicializa a lista de moedas.
    }

    // metodo para adicionar uma moeda no cofrinho
    public void adicionarMoeda(Moeda moeda) {
        moedas.add(moeda);  // adiciona a moeda passada como argumento na lista de moedas.
    }

    // metodo para remover uma moeda do cofrinho
    public void removerMoeda(Moeda moeda) {
        // percorre a lista de moedas para verificar se existe uma com o mesmo valor
        for (Moeda m : moedas) {
            // verifica se o valor da moeda que queremos remover é igual a uma das moedas no cofrinho
            if (m.getValor() == moeda.getValor()) {
                moedas.remove(m);  // remove a moeda da lista
                System.out.println("Moeda removida: " + m.getClass().getSimpleName() + " " + m.getValor());
                return;  // sai do método após remover a moeda
            }
        }
        // se a moeda não foi encontrada, informa ao usuário
        System.out.println("Moeda não encontrada no cofrinho.");
    }        

    // metodo para listar todas as moedas no cofrinho
    public void listarMoedas() {
        if (moedas.isEmpty()) {  // verifica se a lista de moedas está vazia
            System.out.println("O cofrinho está vazio.");
        } else {
            System.out.println("Moedas no cofrinho:");
            // percorre a lista de moedas e imprime o tipo e o valor de cada moeda
            for (Moeda moeda : moedas) {
                System.out.println(moeda.getClass().getSimpleName() + ": " + moeda.getValor());
            }
        }
    }

    // metodo para calcular o total convertido para Real
    public double calcularTotalConvertido() {
        double total = 0;  // inicializa o total como 0
        // percorre a lista de moedas, somando o valor de cada moeda convertido para Real
        for (Moeda moeda : moedas) {
            total += moeda.converterParaReal();  // soma o valor convertido de cada moeda ao total
        }
        return total;  // retorna o total convertido
    }
}
