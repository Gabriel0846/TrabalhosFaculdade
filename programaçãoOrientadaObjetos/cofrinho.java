package programaçãoOrientadaObjetos;

import java.util.ArrayList;
import java.util.List;

class Cofrinho {
    private List<Moeda> moedas;

    public Cofrinho() {
        moedas = new ArrayList<>();
    }

    public void adicionarMoeda(Moeda moeda) {
        moedas.add(moeda);
    }

    public void removerMoeda(Moeda moeda) {
        moedas.remove(moeda);
    }

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

    // metodo para mostrar valor em reais demonstrando tambem os valores da conversão
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

    // metodo para acessar a lista de moedas
    public List<Moeda> getMoedas() {
        return moedas;
    }
}
