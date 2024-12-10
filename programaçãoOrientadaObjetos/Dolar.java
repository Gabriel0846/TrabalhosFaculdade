// classe para dolar
public class Dolar extends Moeda {

    public Dolar(double valor) {
        super(valor);
    }

    @Override
    public double converterParaReal() {
        return valor * 6.05; // considera 1 dolar = 6.05 Reais
    }
}
