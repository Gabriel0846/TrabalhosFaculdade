#include <stdio.h>

struct pessoa {
    char nome[50];
    int idade;
};

int main(){
    // declaração do vetor de structs
    struct pessoa pessoas[5];

    for (int i = 0; i < 5; i++){
        printf("digite o nome da pessoa %d", i + 1);
        scanf("%s", pessoas[i].nome);

        printf("digite a idade da pessoa %d", i + 1);
        scanf("%d", &pessoas[i].idade);
    }

    //impressao dos dados armazenados
    for (int i = 0; i < 5; i++){
        printf("nome: %s\n", pessoas[i].nome);
        printf("idade: %d\n", pessoas[i].idade);
    }
    return 0;
}
