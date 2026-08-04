#include <stdio.h>

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main(){
    int x = 10;
    int y = 20;

    swap(&x, &y); //passagem dos endereços de memoria de x e y

    printf("x: %d, y: %d\n", x, y); //imprime 20, 10
    
    return 0;
}
