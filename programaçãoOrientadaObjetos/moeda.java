import java.util.Objects;

// classe abstrata Moeda, que serve como base para as moedas específicas (Real, Dolar, Euro)
public abstract class Moeda {
    // valor da moeda
    protected double valor;

    // construtor que inicializa o valor da moeda
    public Moeda(double valor) {
        this.valor = valor;  // atribui o valor recebido ao atributo 'valor' da moeda
    }

    // metodo getter que retorna o valor da moeda
    public double getValor() {
        return valor;  // retorna o valor da moeda
    }

    // metodo abstrato que deve ser implementado pelas subclasses (Real, Dolar, Euro)
    // Cada tipo de moeda terá sua própria lógica para converter o valor para Real
    public abstract double converterParaReal();

    // metodo equals() para comparar duas moedas, verificando se elas tem o mesmo valor
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;  // se os dois objetos são o mesmo, retorna true
        if (obj == null || getClass() != obj.getClass()) return false;  // se o objeto for nulo ou de classe diferente, retorna false
        Moeda moeda = (Moeda) obj;  // faz o cast do objeto para Moeda
        return Double.compare(moeda.valor, valor) == 0;  // compara o valor das moedas, retornando true se forem iguais
    }

    // metodo hashCode() que gera um codigo hash único para a moeda com base no valor
    @Override
    public int hashCode() {
        return Objects.hash(valor);  // gera o codigo hash usando o valor da moeda
    }
}
