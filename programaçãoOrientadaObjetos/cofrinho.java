package programaçãoOrientadaObjetos;

import java.util.ArrayList;
import java.util.List;

class Cofrinho {
    private List<Moeda> moedas;

    public Cofrinho() {
        moedas = new ArrayList<>();
    }

    // Método para adicionar moeda
    public void adicionarMoeda(Moeda moeda) {
        // Verifica se já existe uma moeda do mesmo tipo
        boolean moedaExistente = false;
        
        for (Moeda m : moedas) {
            if (m.getClass().equals(moeda.getClass())) {
                // Se já houver, soma o valor da moeda existente
                m.setValor(m.getValor() + moeda.getValor());
                moedaExistente = true;
                break; // Já encontrou a moeda, então sai do loop
            }
        }
        
        // Se a moeda não existir, adiciona uma nova moeda
        if (!moedaExistente) {
            moedas.add(moeda);
        }
    }

    // Método para remover moeda
    public void removerMoeda(Moeda moeda) {
        moedas.remove(moeda);
    }

    // Método para listar as moedas
    public void listarMoedas() {
        if (moedas.isEmpty()) {
            System.out.println("Nenhuma moeda no cofrinho.");
        } else {
            System.out.println("Moedas no cofrinho:");
            for (Moeda moeda : moedas) {
                System.out.println(moeda.info() + " | Convertido para Real: " + moeda.converterParaReal());
            }
        }
    }

    // Método para calcular o total em Reais
    public double calcularTotalEmReais() {
        double total = 0;
        System.out.println("Detalhamento da conversão para Reais:");
        for (Moeda moeda : moedas) {
            double valorConvertido = moeda.converterParaReal();
            System.out.println(moeda.info() + " | Convertido para Real: " + valorConvertido);
            total += valorConvertido;
        }
        return total;
    }

    // Método para acessar a lista de moedas
    public List<Moeda> getMoedas() {
        return moedas;
    }
}
