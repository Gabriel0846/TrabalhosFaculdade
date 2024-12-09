package programaçãoOrientadaObjetos.moedas;

public class dolar {
    // Atributos da classe
    private String nome;          // Nome da moeda
    private String pais;          // País de origem da moeda
    private double valor;         // Valor da moeda (quanto vale em dólares)
    private double taxaConversao; // Taxa de conversão para Real

    // Construtor para inicializar todos os atributos
    public dolar(String nome, String pais, double valor, double taxaConversao) {
        this.nome = nome;
        this.pais = pais;
        this.valor = valor;
        this.taxaConversao = taxaConversao;
    }

    // Método para obter o nome da moeda
    public String getNome() {
        return nome;
    }

    // Método para definir o nome da moeda
    public void setNome(String nome) {
        this.nome = nome;
    }

    // Método para obter o país da moeda
    public String getPais() {
        return pais;
    }

    // Método para definir o país da moeda
    public void setPais(String pais) {
        this.pais = pais;
    }

    // Método para obter o valor da moeda
    public double getValor() {
        return valor;
    }

    // Método para definir o valor da moeda
    public void setValor(double valor) {
        this.valor = valor;
    }

    // Método para obter a taxa de conversão para Real
    public double getTaxaConversao() {
        return taxaConversao;
    }

    // Método para definir a taxa de conversão para Real
    public void setTaxaConversao(double taxaConversao) {
        this.taxaConversao = taxaConversao;
    }

    // Método para converter o valor da moeda para Real
    public double converterParaReal() {
        return this.valor * this.taxaConversao;
    }

    // Representação em String da moeda
    @Override
    public String toString() {
        return nome + " (" + pais + "): " + valor + " - Conversão para Real: R$ " + converterParaReal();
    }

    public static void main(String[] args) {
        // Criando um objeto de Dólar com o nome, país, valor e taxa de conversão para Real
        Dolar dolar = new Dolar("Dólar", "Estados Unidos", 100.0, 5.2); // 100 dólares, taxa de 1 Dólar = 5.2 Reais

        // Exibindo as informações do Dólar
        System.out.println(dolar);

        // Mostrando o valor em Real
        double valorEmReais = dolar.converterParaReal();
        System.out.println("Valor em Reais: R$ " + val
