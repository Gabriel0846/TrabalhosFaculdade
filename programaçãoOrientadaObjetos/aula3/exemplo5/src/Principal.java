public class Principal {
    public static void Main(String[] args) {
    
        Nota mario = new Nota();
        mario.setNota1(9);
        mario.setNota2(10);

        mario.resultado();

        mario.setNota1(2);

        mario.resultado();
    }
}

