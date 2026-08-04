#include <stdio.h>

int main(){
    int array[5] = {1, 2, 3, 4, 5};
    int *ponteiro_para_primeiro_elemento = &array[0];
    int *ponteiro_para_ultimo_elemento = &array[4];

    //adicao
    printf("valor do elemento acessado pelo ponteiro_para_primeiro_elemento = %d \n", *ponteiro_para_primeiro_elemento);
    ponteiro_para_primeiro_elemento++;//aponta para o segundo elemento.
    printf("valor do elemento acessado pelo ponteiro_para_primeiro_elemento pos incrementado = %d \n", *ponteiro_para_primeiro_elemento);

    //subtracao
    printf("valor do elemento acessado pelo ponteiro_para_ultimo_elemento = %d \n", *ponteiro_para_ultimo_elemento);
    ponteiro_para_ultimo_elemento--;//aponta para o quarto elemento.
    printf("valor do elemento acessado pelo ponteiro_para_ultimo_elemento pos incremento = %d \n", *ponteiro_para_ultimo_elemento);

    //comparacao

    if(ponteiro_para_primeiro_elemento == ponteiro_para_ultimo_elemento){
        printf("apontam para o mesmo local");
    }

    return 0;
}