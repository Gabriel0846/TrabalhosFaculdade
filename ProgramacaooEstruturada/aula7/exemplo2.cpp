#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
    if (argc != 3){
        printf("uso: %s <num1> <num2>\n", argv[0]);
        return 1;
    }

    int num1 = atoi(argv[1]);
    int num2 = atoi(argv[2]);
    int soma = num1 + num2;

    printf("a soma de %d e %d é %d\n", num1, num2, soma);
    
    return 0;
}
