package empresa;

public class Desktop extends Computador{
    double acessorios;

    
    public Desktop(int gbMemoria, int numProcessadoes, double acessorios) {
        super(gbMemoria, numProcessadoes);
        this.acessorios = acessorios;
    }

    @Override
    double calculaValor() {
        double total = 200*gbMemoria + 400*numProcessadoes + acessorios;
        return total;
    }
    
}
