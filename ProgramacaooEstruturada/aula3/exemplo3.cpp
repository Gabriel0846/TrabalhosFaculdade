#include <stdio.h>
#include <string.h>

struct pessoa{
    char nome[50];
    int idade;
};

int main(){
    
//declaracao do vetor de structs
struct pessoa pessoas[2];

//leitura dos daods do usuario conforme exemplo anteiror
for (int i = 0; i < 2; i++){
        printf("digite o nome da pessoa: %d", i + 1);
        scanf("%s", pessoas[i].nome);

        printf("digite a idade da pessoa: %d", i + 1);
        scanf("%d", &pessoas[i].idade);
    }

    //nome da pessoa a ser buscada
    char nomebusca[50];
    strcpy(nomebusca, "joao");

    //busca pelo elemento no vetor
    int posicaoencontrada = -1;
    for (int i = 0; i < 2; i++){
        if (strcmp(pessoas[2].nome, nomebusca) == 0){
            posicaoencontrada = i;
            break;    
        }
    }

    //exibicao do resultado da busca
    if (posicaoencontrada != -1){
        printf("pessoa encontrada na posicao %d.\n", posicaoencontrada + 1);
        printf("nome: %s\nidade: %d\n", pessoas[posicaoencontrada].nome, pessoas[posicaoencontrada].idade);
    } else  {
        printf("pessoa nao encontrada.\n");
    }

    return 0;
}


