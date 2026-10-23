import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class App {
    public static void main(String[] args) throws Exception {
        
        LocalDate dataHoje = LocalDate.now();

        System.out.println(dataHoje);
        DateTimeFormatter formatador = DateTimeFormatter.ofPattern("dd/MM/yyyy - EEEE");
        System.out.println(dataHoje.format(formatador));
    }
}
