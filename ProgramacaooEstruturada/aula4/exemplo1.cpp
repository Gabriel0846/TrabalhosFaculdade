#include<stdio.h>

int main(){
    
    int x = 10;
    char z = 'M';
    int *ponteiro_para_x = &x;
    char *ponteiro_para_z = &z;

    printf("valor de x = %d \n", x);
    printf("valor de x acessado pelo ponteiro = %d \n", *ponteiro_para_x);
    printf("valor de ponteiro_para_x = %p \n", ponteiro_para_x);

    printf("valor de z = %c \n", z);
    printf("valor de z acessado pelo ponteiro = %c \n", *ponteiro_para_z);
    printf("valor de ponteiro_para_z = %p \n", ponteiro_para_z);

    return 0;
}
