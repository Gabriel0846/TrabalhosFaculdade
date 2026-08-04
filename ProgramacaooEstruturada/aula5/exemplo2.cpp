#include <stdio.h>
#include <stdlib.h>

int *get_array(int size){
    //alocacao dinamica de um array de 'size' inteiros
    int *array = (int *) malloc(sizeof(int) * size);

    //...

    //retorno do ponteiro para o array alocado
    return array;
}

int main(){
    //poteiro 'array' recebe o ponteiro retornado pela funcao 'get_array'
    int *array = get_array(10);

    //...

    //uso da array
    printf("imprimindo array: \n");
    for (int i = 0; i < 10; i++){
        array[i] = i;
        printf("%d", array[i]);
    }

    //...

    //desalocacao da memoria alocada
    free(array);
    
    return 0;
}
