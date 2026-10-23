public class Ingresso {
    String nomeEvento;
    double valor;

    public Ingresso(String nomeEvento, double valor) {
        this.nomeEvento = nomeEvento;
        this.valor = valor;
    }

    void info(){
        System.out.println("Nome evento: " + nomeEvento);
        System.out.println("Valor ingresso: " + valor);
    }
}
