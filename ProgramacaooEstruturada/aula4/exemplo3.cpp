#include <stdio.h>

int main(){
    //definindo a matriz 3 x 3
    int matriz[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    //declarando um ponteiro para percorrer a matriz
    int *ptr = NULL;

    //inicializando o ponteiro para o primeiro elemento da matriz
    ptr = &matriz[0][0];

    //percorrendo a matriz usando ponteiro
    printf("elementos da matriz:\n");
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++){
            //imprimindo o valor apontado pelo ponteiro
            printf("%d ", *ptr);
            //movendo o ponteiro para o proximo elemento da matriz
            ptr++;
        }
        printf("\n");
    }
    
    return 0;
}
