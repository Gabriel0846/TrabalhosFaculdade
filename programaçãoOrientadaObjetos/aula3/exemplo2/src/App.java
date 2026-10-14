import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;

public class App {
    public static void main(String[] args) throws Exception {
        //ArrayList<String> pessoas = new ArrayList();
        LinkedList<String> pessoas = new LinkedList();

        pessoas.add("Mario");
        pessoas.add("Luigi");
        pessoas.add("Peach");
        pessoas.add("Yoshi");

        System.out.println(pessoas.get(0));
        //pessoas.remove(1);

        System.out.println("Ordem original");
        System.out.println(pessoas);

        Collections.sort(pessoas);
        System.out.println("Ordem alfabetica");
        System.out.println(pessoas);

        
        Collections.reverse(pessoas);
        System.out.println("Ordem inversa");
        System.out.println(pessoas);

        Collections.shuffle(pessoas);
        System.out.println("apos shuffle");
        System.out.println(pessoas);

        System.out.println(Collections.min(pessoas));
        System.out.println(Collections.max(pessoas));

        HashMap<String,String> capitais = new HashMap<>();
        capitais.put("Brasil", "Brasilia");
        capitais.put("Argentina", "Buenos Aires");
        capitais.put("Paraguai", "Assunção");
        capitais.put("Uruguai", "Montevideu");

        System.out.println(capitais);
        System.out.println(capitais.get("Uruguai"));
    }
}
