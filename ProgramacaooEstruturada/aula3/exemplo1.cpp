#include <stdio.h>
#include <string.h>

struct pessoa{
    char nome[50];
    int idade;
};

int main(){
    struct pessoa pessoa1;

    strcpy(pessoa1.nome, "maria oliveira");
    pessoa1.idade = 30;

    printf("nome: %s\nidade: %d\n", pessoa1.nome, pessoa1.idade);
    
    return 0;
}

