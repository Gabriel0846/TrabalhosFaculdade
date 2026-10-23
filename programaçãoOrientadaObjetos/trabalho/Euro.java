// classe para euro
public class Euro extends Moeda {

    public Euro(double valor) {
        super(valor);
    }

    @Override
    public double converterParaReal() {
        return valor * 6.41; // considera 1 euro = 6.41 Reais
    }
}