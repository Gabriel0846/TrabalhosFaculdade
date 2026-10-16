package empresa;

public class App {
    public static void main(String[] args) throws Exception {
        Cofrinho c = new Cofrinho();

        c.add(new Moeda("Euro", 0.5));
        c.add(new Moeda("Euro", 1));
        c.add(new Moeda("Euro", 0.1));
        c.add(new Moeda("Euro", 0.05));

        System.out.printf("O total no cofrinho eh: %.2f \n", c.calculaTotal());
    }
}
