#include <stdio.h>

//funcao recursiva para calcular o mdc de dois numeros utilizando o algoritimo de euclides
unsigned int mdc(unsigned int a, unsigned int b){
    if (b == 0) //condicao de parada
    return a;
    else
    return mdc(b, a % b); //chamada recursiva    
}

int main(){
    unsigned int numero1 = 48, numero2 = 18;
    printf("o mdc de %u e %u e: %u\n", numero1, numero2, mdc(numero1, numero2));
    return 0;
}
