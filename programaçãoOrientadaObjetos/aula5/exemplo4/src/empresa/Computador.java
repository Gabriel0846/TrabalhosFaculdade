package empresa;

public abstract class Computador {
    int gbMemoria;
    int numProcessadoes;

    public Computador(int gbMemoria, int numProcessadoes) {
        this.gbMemoria = gbMemoria;
        this.numProcessadoes = numProcessadoes;
    }

    abstract double calculaValor();

}
