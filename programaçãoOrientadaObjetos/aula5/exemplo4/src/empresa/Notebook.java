package empresa;

public class Notebook extends  Computador{
    int polegadasTela;

    public Notebook(int gbMemoria, int numProcessadoes, int polegadasTela) {
        super(gbMemoria, numProcessadoes);
        this.polegadasTela = polegadasTela;
    }

    @Override
    double calculaValor() {
        double total = 250*gbMemoria + 500*numProcessadoes + 100*polegadasTela;
        return total;
    }


}
