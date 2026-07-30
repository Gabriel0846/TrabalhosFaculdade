#include <stdio.h>

int main() {
    int n1, n2;

    printf("digite o primerio numero: ");
    scanf("%d", &n1);

    printf("digite o segundo numero: ");
    scanf("%d", &n2);

    if (n1 > n2) {
        printf("\n\n numero 1 eh maior que o numero 2");
    } else {
        printf("\n\n numero 2 eh maior que o numero 1");
    }

    return 0;
}