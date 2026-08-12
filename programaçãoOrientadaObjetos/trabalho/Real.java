// classe real
public class Real extends Moeda {

    public Real(double valor) {
        super(valor);
    }

    @Override
    public double converterParaReal() {
        return valor; // Valor já esta em real
    }
}