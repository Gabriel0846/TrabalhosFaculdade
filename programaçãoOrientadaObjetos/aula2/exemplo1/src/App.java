public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        Aluno a = new Aluno();
        a.matricula=1001;
        a.nome="Super Mario";
        a.cpf="111222333";

        Aluno b = new Aluno();
        b.matricula=1002;
        b.nome="Yoshi";
        b.cpf="777222555";

        a.info();

        a.nome="Super Luigi";

        a.info();

        b.info();
    }
}
