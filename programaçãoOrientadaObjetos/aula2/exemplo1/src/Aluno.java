public class Aluno {
    
    int matricula;
    String nome;
    String cpf;

    public Aluno(int matricula){
        this.matricula = matricula;
        this.nome= "Vazio";
        this.cpf = "000.000.000-00";
    }

    Aluno(){
        System.out.println("Aluno criado sem parametros");
    };

    Aluno(int pMatricula, String pNome, String pCpf){
        matricula = pMatricula;
        nome = pNome;
        cpf = pCpf;
    }


    public void info() {
        System.out.println("Matricula: " + matricula);
        System.out.println("Nome: " + nome);
        System.out.println("CPF: " + cpf);
        System.out.println();
    }
}

