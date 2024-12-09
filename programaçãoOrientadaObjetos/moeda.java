package programaçãoOrientadaObjetos;

abstract class Moeda {
    protected double valor;

    public Moeda(double valor) {
        this.valor = valor;
    }

    public double getValor() {
        return valor;
    }

    // Método abstrato para conversão para Real
    public abstract double converterParaReal();

    // Método para retornar informações sobre a moeda
    public abstract String info();
}
