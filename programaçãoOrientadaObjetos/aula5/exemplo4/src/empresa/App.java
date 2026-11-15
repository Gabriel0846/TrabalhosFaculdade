package empresa;

import java.util.ArrayList;

public class App {
    public static void main(String[] args) throws Exception {
        Desktop compA = new Desktop(8, 4, 600);
        Notebook compB = new Notebook(8, 4, 15);

        Computador comp;

        ArrayList<Computador> listaComputadores = new ArrayList<>();

        listaComputadores.add(compA);
        listaComputadores.add(compB);
        listaComputadores.add(new Desktop(16, 8, 1200));
        listaComputadores.add(new Notebook(16, 8, 18));

        comp = compA;
        System.out.println("Valor: "+comp.calculaValor());
        comp = compB;
        System.out.println("---------");
        System.out.println("Valor: "+comp.calculaValor());

        double total = 0;

        for(Computador c : listaComputadores){
            total += c.calculaValor();
        }

        System.out.println("Total do valor: " + total);
    }
}
