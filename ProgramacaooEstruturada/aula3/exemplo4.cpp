#include <stdio.h>
#include <string.h>

struct pessoa{
    char nome[50];
    int idade;
};

int main(){
    //declara da matriz de structs
    struct pessoa matrizpessoas[3][2];

    //inicialização de matriz
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 2; j++){
            strcpy(matrizpessoas[i][j].nome, "nome padrao");
            matrizpessoas[i][j].idade = 0;
        }
        
    }

    //impressao da matriz original
    printf("matriz  original:\n");
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 2; j++){
            printf("nome: %s\nidade: %d\n\n", matrizpessoas[i][j].nome, matrizpessoas[i][j].idade);
        }
    }

    //acesso a um elemento especifico da matriz
    strcpy(matrizpessoas[1][0].nome, "joao silva");
    matrizpessoas[1][0].idade = 25;

    //impressao da matriz
    printf("\nmatriz pos alteracao de elemento: \n");
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 2; j++){
            printf("nome: %s\nidade: %d\n\n", matrizpessoas[i][j].nome, matrizpessoas[i][j].idade);
        }
    }
    

    return 0;
}
