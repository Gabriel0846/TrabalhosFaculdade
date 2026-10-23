package empresa;

public class App {
    public static void main(String[] args) throws Exception {
        LivroDigital ld = new LivroDigital("Senhor dos aneis", 
            new Autor("Tolkein", "Britanico", "tolkein@email.com"), 
            "Aventura",
            5,
            10000,
            3500);
        ld.info();
    }
}
