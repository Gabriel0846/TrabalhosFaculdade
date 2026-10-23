package empresa;

public class LivroDigitelEx {
    public String autor;
    public float custoProducao;
    public float precoVenda;
    public String titulo;
    public int paginas;
    //novo
    public String linkDownload;
    public int tamanhoMB;

    public float lucro(){
        return precoVenda - custoProducao;
    }

    public void imprimirTitulo() {
        System.out.println("O titulo: " + titulo);
    }
    //mudou
    public float imposto(){
        return 0.2f * lucro() + 2;
    }
    //NOVO
    public float tamanhoPorPagina(){
        return tamanhoMB/(float)paginas;
    }
}
