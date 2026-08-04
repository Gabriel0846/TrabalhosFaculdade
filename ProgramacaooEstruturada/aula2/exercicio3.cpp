#include <stdio.h>
#include <string.h>

int main() {
    char nomes[4][51];
    int idades[4];
    int i;
    char c;
    int encontroumaior = 0;

    for (i = 0; i < 4; i++) {
        printf("--- cadastro do aluno %d ---\n", i +1);

        //nome
        printf("digiteo nome: ");
        fgets(nomes[i], sizeof(nomes[i]), stdin);
        nomes[i][strcspn(nomes[i], "\n")] = '\0';

        //idades
        printf("digite a idade: ");
        scanf("%d", &idades[i]);
        c = getchar();

        printf("\n");
    }

    printf("=================================\n");
    printf("     ALUNOS MAIORES DE IDADE     \n");
    printf("=================================\n");

    for (i = 0; i < 4; i++) {
        if (idades[i] >= 18) {
            printf("nome: %-25s | idade: %d anos\n", nomes[i], idades[i]);
            encontroumaior = 1;
        }
    }
    
    if (!encontroumaior) {
        printf("nenhum aluno cadastrado eh maior de idade.\n");
    }

    printf("=================================\n");

    return 0;
    
}