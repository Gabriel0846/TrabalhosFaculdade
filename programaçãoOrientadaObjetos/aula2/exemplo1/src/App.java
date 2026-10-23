import java.util.ArrayList;

public class App {
    public static void main(String[] args) {
        Aluno a = new Aluno();
        a.cpf="111.222.333-44";
        a.nome="Super Mario";
        a.matricula=1001;
        a.info();

        Aluno b = new Aluno(1002, "Super Luigi", "222.333.444-55");
        b.info();
        
        Aluno c = new Aluno(1003);

        ArrayList<Aluno> alunos = new ArrayList<>();

        alunos.add(c);
        alunos.add(new Aluno(1004, "Bowser", "666.777.888-99"));
    }
}
