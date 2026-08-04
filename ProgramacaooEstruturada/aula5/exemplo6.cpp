#include <stdio.h>

//definicao de uma union para representar um numero inteiro ou um numero de ponto flutuante
union numero{
    int inteiro;
    float flutuante;
};

int main(){
    //declaracao de uma variavel do tipo union numero
    union numero num;

    //atribuicao de um valor inteiro a variavel inteiro da union
    num.inteiro = 10;

    //impressao do valor inteiro
    printf("valor inteiro: %d\n", num.inteiro);

    //atribuicao de um valor de ponto flutuante a variavel flutuante da union
    num.flutuante = 3.14;

    //impressao do valor de ponto flutuante
    printf("valor de ponto flutuante: %.2f\n", num.flutuante);
    
    //impressao dos enderecos de memoria
    printf("enderecos de ponto flutuante: %p\n", &num.flutuante);
    printf("enderecos de inteiro: %p\n", &num.inteiro);

    return 0;
}

