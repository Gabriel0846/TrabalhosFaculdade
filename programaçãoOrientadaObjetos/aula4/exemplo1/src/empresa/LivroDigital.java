package empresa;

public class LivroDigital extends Livro{
    public String linkDownload;
    public int tamanhoMB;

    public LivroDigital(String titulo, String autor, String linkDownload) {
        super(titulo, autor);
        this.linkDownload = linkDownload;
    }

    //MUDOU
    public float imposto(){
        return super.imposto() + 2;
    }
    //NOVO
    public float tamanhoPorPagina(){
        return tamanhoMB/(float)paginas;
    }

    public void imprimirImposto() {
        System.out.println("O imposto do livro fisico: " + super.imposto());
        System.out.println("O imposto do livro digital: " + imposto());
    }
}
