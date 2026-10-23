package empresa;


public class Nota {
    private double nota1;
    private double nota2;
    private int faltas;

    public Nota(){

    }

    public Nota(double nota1, double nota2, int faltas) {
        setNota1(nota1);
        setNota2(nota2);
        setFaltas(faltas);
    }

    public void setNota1(double nota1){
        if(nota1<0 || nota1>10){
            System.out.println("Nota invalida");
            return;
        }
        this.nota1 = nota1;
    }

    public void setNota2(double nota2){
        if(nota2<0 || nota2>10){
            System.out.println("Nota invalida");
            return;
        }
        this.nota2 = nota2;
    }

    public double getNota1(){
        return nota1;
    }

    public double getNota2(){
        return nota2;
    }

    public int getFaltas() {
        return faltas;
    }

    public void setFaltas(int faltas) {
        if (faltas>40 || faltas<0) {
            System.out.println("Numero de faltas invalido.");
            return;
        }
        this.faltas = faltas;
    }

    void resultado(){

        double media = (nota1 + nota2)/2;

        System.out.println("Media: " + media);
        if (faltas>7) {
            System.out.println("Reprovado por faltas.");
            return;
        }
        if(media <4) {
            System.out.println("Reprovado por notas.");
        }
        else if(media <7){
            System.out.println("Exame Final");;
        }
        else {
            System.out.println("Aprovado");
        }
    }
}
