#include <stdio.h>

int main() {
    float p1, p2, p3;

    printf("digite o preço do primeiro produto: ");
    scanf("%f", &p1);

    printf("digite o preço do segundo produto: ");
    scanf("%f", &p2);

    printf("digite o preço do terceiro produto: ");
    scanf("%f", &p3);

    if ((p1 < p2) && (p1 < p3)) {
        printf("\n\n o produto 1 eh mais barato!\n\n");
    } else if ((p2 < p1) && (p2 < p3)) {
        printf("\n\n o produto 2 eh mais barato!\n\n");
    } else {
        printf("\n\n o produto 3 eh mais barato!\n\n");
    }   
}