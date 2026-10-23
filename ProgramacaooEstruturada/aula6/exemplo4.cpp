#include <stdio.h>

int main(void){
    FILE *arquivo;
    char url[] = "arquivo.txt", nome[20];
    float nota1, nota2, nota3;

    //abre o arquivo para a leitura
    arquivo = fopen(url, "r");

    //verifica se o arquivo foi aberto com sucesso
    if (arquivo == NULL) {
        printf("erro ao abrir o arquivo.\n");
    } else {
        //le os dados do arquivo enquanto nao atingir o fim do arquivo (EOF)
        while (fscanf(arquivo, "%s %f %f %f\n", nome, &nota1, &nota2, &nota3) != EOF){
            //calcula e imprime a media das tres notas.
            printf("%s teve media %.2f\n", nome, (nota1 + nota2 + nota3) / 3);
        }
        //fecha o arquivo
        fclose(arquivo);
    }
    return 0;
}