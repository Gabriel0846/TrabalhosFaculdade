#include <stdio.h>

//funcao recursiva para gerar o n-esimo numero de fibonacci
unsigned int fibonacci(unsigned int n){
    if (n <= 1) //condicao de parada
    return n;
    else
    return fibonacci(n - 1) + fibonacci(n - 2); //chamadas recusivas
}

int main(){
    unsigned int termo = 10;
    printf("os primeiros %u termos da sequencia de fibonacci sao:\n", termo);
    for (unsigned i = 0; i < termo; i++){
        printf("%u ", fibonacci(i));
    }
    printf("\n");
    
    return 0;
}
