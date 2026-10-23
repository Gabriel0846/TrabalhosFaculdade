#include <stdio.h>

//funcao recusiva para calcular a fatorial de um numero
unsigned int fatorial(unsigned int n){
    if (n == 0) //condicoes de parada
    return 1;
    else
    return n * fatorial(n - 1); //chamada recursiva    
}

int main(){
    unsigned int numero = 5;
    unsigned int resultado = fatorial(numero);
    printf("o fatorial de %u e: %u\n", numero, resultado);
    return 0;
}
