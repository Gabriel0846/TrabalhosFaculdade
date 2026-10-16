package empresa;

public class App {
    public static void main(String[] args) throws Exception {
        Aluno a1 = new Aluno("Mario", 111,0.1,new Curso("Engenharia", 1000));

        a1.info();
        System.out.println("Valor da mensalidade: " + a1.pagamento());
    }
}
