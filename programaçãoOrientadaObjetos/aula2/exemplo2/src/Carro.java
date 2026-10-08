public class Carro {
    String nome;
    String modelo;
    float velocidade;
    static  float milhasParaMetros(float milhas){
        Carro c = new Carro();
        return milhas*1600;
    }
}
