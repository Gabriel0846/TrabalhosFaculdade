#include <stdio.h>

int main(){
    FILE *arquivo;
    char string1[] = "esta e a primeira string.";
    char string2[] = "esta é a segunda string.";

    arquivo = fopen("arquivo_fputs.txt", "w");

    //abre o arquivo foi aberto com sucesso
    if (arquivo != NULL){
        //escreve as strings no arquivo
        fputs(string1, arquivo);
        fputs("\n", arquivo); //adiciona nova linha entre as strings
        fputs(string2, arquivo);

        //fecha o arquivo
        fclose(arquivo);
        printf("strings escrtas no arquivo com sucesso.\n");
    } else {
        //exibe mensagem de erro se não for possivel abrir o arquivo
        printf("erro ao abrir o aquivo.\n");
    }
    return 0;
}
