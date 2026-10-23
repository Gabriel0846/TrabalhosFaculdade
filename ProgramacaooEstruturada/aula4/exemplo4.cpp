#include <stdio.h>
#include <stdlib.h>

//definicao da estrutura pessoa
struct pessoa{
    char nome[50];
    int idade;
    float altura;
};

int main(){
    //declaracao de uma variavel do tipo pessoa
    struct pessoa pessoa1;

    //preenchendo os dados da pessoa1
    printf("digite o nome da pessoa: ");
    scanf("%s", pessoa1.nome);
    printf("digite a idade da pessoa: ");
    scanf("%d", &pessoa1.idade);
    printf("digite a altura da pessoa: ");
    scanf("%f", &pessoa1.altura);
    
    //usando ponteiros para acessar os elementos da struct pessoa
    struct pessoa *ptrpessoa;
    ptrpessoa = &pessoa1;

    //imprimindo os dados da pessoa1 usando ponteiros
    printf("\ndados da pessoa: \n");
    printf("nome: %s\n", ptrpessoa->nome);
    printf("idade: %d anos\n", ptrpessoa->idade);
    printf("altura: %.2f metros\n", ptrpessoa->altura);
    
    return 0;
}
