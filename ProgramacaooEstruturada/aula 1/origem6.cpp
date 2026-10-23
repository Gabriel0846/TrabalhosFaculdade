#include <stdio.h>

int main() {
    int cont = 1, entrada;

    printf("digite o valor final da contagem: ");
    scanf("%d", &entrada);

    while (cont <= entrada) {
        printf("%d \t", cont);
        cont++;
        if (cont == entrada) {
            printf("%d \n", cont);
            cont ++;
            break;
        }
        printf("%d \t", cont);
        cont ++;
    }
    return 0;
}