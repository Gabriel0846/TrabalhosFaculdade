package empresa;

import javax.swing.plaf.basic.BasicInternalFrameTitlePane.SystemMenuBar;

public class App {
    public static void main(String[] args) throws Exception {
        Livro l1 = new Livro("Sherlock Holmes", "Sir Arthur Conan Doyle");

        LivroDigital l2 = new LivroDigital("Sherlock Holmes", "Sir Arthur Conan Doyle", "http://meusite.com/sherlock");
        System.out.println(l1 instanceof Livro);
        System.out.println(l2 instanceof Livro);
        System.out.println(l1 instanceof LivroDigital);
        System.out.println(l2 instanceof LivroDigital);
    }
}
