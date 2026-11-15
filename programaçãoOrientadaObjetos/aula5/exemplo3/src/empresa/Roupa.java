package empresa;

enum Estacao{
    VERAO,
    OUTONO,
    INVERNO,
    PRIMAVERA
}
public class Roupa {
    String modelo;
    int tamanho;
    Estacao colecao;

    public Roupa(String modelo, int tamanho, Estacao colecao) {
        this.modelo = modelo;
        this.tamanho = tamanho;
        this.colecao = colecao;
    }
    
    public void msg(){
        switch (colecao) {
            case VERAO:
                System.out.println("Arrase na praia!");
                break;
            case OUTONO:
                System.out.println("Passe o outono com elegancia!");
                break;
            case INVERNO:
                System.out.println("se agasalhe bem e com estilo!");
                break;
            case PRIMAVERA:
                System.out.println("se vista na estacao das flores");
                break;
            default:
                System.out.println("Erro!");
                break;
        }
    }
}
