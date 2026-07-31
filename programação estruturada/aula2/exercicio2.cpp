#include <stdio.h>
#include <string.h>

int main(){
    char nomes[5][51];
    char cargos[5][31];
    float salarios[5];
    int i, j;
    char c;
    int encontrouduplicado = 0;

    for (i = 0; i < 5; i++){
        printf("--- cadastro do funcionario %d ---\n", i + 1);

        //nome
        printf("digite o nome: ");
        fgets(nomes[i], sizeof(nomes[i]), stdin);
        nomes[i][strcspn(nomes[i], "\n")] = '\0';

        //cargo
        printf("digite o cargo: ");
        fgets(cargos[i], sizeof(cargos[i]), stdin);
        cargos[i][strcspn(cargos[i], "\n")] = '\0';

        //salario
        printf("digite o salario: R$ ");
        scanf("%f", &salarios[i]);
        c = getchar();

        printf("\n");
    }

    printf("========================================\n");
    printf(" FUNCIONARIOS COM CARGOS EM DUPLICIDADE\n");
    printf("========================================\n");

    int jaexibido[5] = {0};

    for (i = 0; i < 5; i++){
        for (j = 0; i < 5; j++){    
            if (strcmp(cargos[i], cargos[j]) == 0) {
                encontrouduplicado = 1;

                if (!jaexibido[i]){
                    printf("nome: %s | cargo: %s | salario: RS %.2f\n", nomes[i], cargos[i], salarios[i]);
                    jaexibido[i] = 1;
                }

                if (!jaexibido[j]){
                    printf("nome: %s | cargo: %s | salario: RS %.2f\n", nomes[j], cargos[j], salarios[j]);
                    jaexibido[j] = 1;
                }
                
            }
        }
    }
    
    if (!encontrouduplicado){
        printf("nenhum funcionario possui cargo repetido.\n");
    }
    printf("==========================================\n");

    return 0;
}
