package empresa;

public class Conta {
    String nome;
    double saldo;

    public Conta(String nome, double saldo) {
        this.nome = nome;
        this.saldo = saldo;
    }

    void depositar(double valor){
        if (valor<0) {
            throw new RuntimeException("valor invalido");
        }
        saldo += valor;
    }

    void sacar(double valor)throws Exception{
        if (valor>saldo) {
            throw new Exception("saldo insulficiente");
        } if (valor<0) {
            throw new Exception("valor invalido");
        }
        saldo -= valor;
    }

    void transferir(double valor, Conta destino)throws Exception{
        this.sacar(valor);
        destino.depositar(valor);
    }

    void info(){
        System.out.println("----");
        System.out.println("Nome: "+nome);
        System.out.println("Saldo: "+saldo);
    }
}
