package programaçãoOrientadaObjetos;

abstract class Moeda {
    private double valor;

    public Moeda(double valor) {
        this.valor = valor;
    }

    public double getValor() {
        return valor;
    }

    // metodo para conversão da moeda
    public abstract double converterParaReal();

    // metodo para fornecer informações sobre a moeda
    public String info() {
        return "Valor: " + getValor();
    }
}

class Dolar extends Moeda {
    public Dolar(double valor) {
        super(valor);
    }

    @Override
    public double converterParaReal() {
        return getValor() * 6.05; // taxa de conversão para real
    }

    @Override
    public String info() {
        return "Dólar - " + super.info(); // metodo que retorna informações da moeda
    }
}
class Euro extends Moeda {
    public Euro(double valor) {
        super(valor);
    }

    @Override
    public double converterParaReal() {
        return getValor() * 6.39; // taxa de conversão para real
    }

    @Override
    public String info() {
        return "Euro - " + super.info();// metodo que retorna informações da moeda
    }
}

class Real extends Moeda {
    public Real(double valor) {
        super(valor);
    }

    @Override
    public double converterParaReal() {
        return getValor(); // valor em real já é considerado como real
    }

    @Override
    public String info() {
        return "Real - " + super.info(); // metodo que retorna informações da moeda
    }
}