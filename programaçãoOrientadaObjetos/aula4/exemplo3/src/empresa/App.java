public class App {
    public static void main(String[] args) throws Exception {
        IngressoVip iv = new IngressoVip("Rock in Curitiba", 200, 100);

        iv.info();

        System.out.println("----------------------------------------------");
        Ingresso i = new Ingresso("Rock in Rio Pardo ", 50);

        i.info();
    }
}
