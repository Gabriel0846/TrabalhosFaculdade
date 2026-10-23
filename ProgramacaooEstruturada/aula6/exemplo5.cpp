#include <stdio.h>

int main(){
    FILE *arquivo;
    char mensagem[] = "gravando uma nova mensagem no arquivo usando fputc()";

    //abre o arquivo para escrita
    arquivo = fopen("arquivo_fputc.txt", "w");

    //verifica se o arquivo foi aberto com sucesso
    if (arquivo != NULL){
        //escreve a mensagem caractere a caractere no arquivo
        for (int i = 0; mensagem[i] != '\0'; i++){
            fputc(mensagem[i], arquivo);
        }

        //fecha o arquivo
        fclose(arquivo);
        printf("mensagem escrita no arquivo com sucesso.\n");
    } else {
        //exibe mensagem de erro se não for possivel abrir o arquivo
        printf("erro ao abrir o arquivo.\n");
    }
    return 0;
}
