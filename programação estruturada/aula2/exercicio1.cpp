#include <stdio.h>
#include <string.h>

int main() {
    char titulos[3][101];
    char autores[3][101];
    int anos[3];
    int i;
    char c;

    for (i = 0; i <3; i++) {
        printf("--- cadastro do livro %d --- \n", i + 1);

        //titulo
        printf("digite o titulo do livro: ");
        fgets(titulos[i], sizeof(titulos[i]), stdin);
        titulos[i][strcspn(titulos[i], "\n")] = '\0';

        //autor
        printf("digite o autor do livro: ");
        fgets(autores[i], sizeof(autores[i]), stdin);
        autores[i][strcspn(autores[i], "\n")] = '\0';

        //ano
        printf("digite o ano do livro: ");
        scanf("%d", &anos[i]);
        c = getchar();

        printf("\n");
    }

    printf("===========================");
    printf("\n    Livros cadastrados\n");
    printf("===========================\n");

    for(i = 0; i < 3; i++) {
        printf("Livro %d:\n", i + 1);
        printf(" titulo: %s\n", titulos[i]);
        printf(" autor: %s\n", autores[i]);
        printf(" ano: %d\n", anos[i]);
        printf("--------------------------------------\n");
    }

    return 0;
}