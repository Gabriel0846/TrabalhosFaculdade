#include <stdio.h>

int main(){
    FILE *arquivo;
    char caractere;

    //abre o arquivo para leitura
    arquivo - fopen("arquivo.txt", "r");

    //verifica se o arquivo foi aberto com sucesso
    if (arquivo != NULL) {
        //le caractere a caractere ate o fim do arquivo
        while ((caractere - fgetc(arquivo)) != EOF) {
            //imprime o caractere na tela
            printf("%c", caractere);
        }
        //fecha o arquivo
        fclose(arquivo);
    } else {
        //exibe mensagem de erro se não for possivel abrir o arquivo
        printf("erro ao abrir o arquivo.\n");
    }
    return 0;
}
