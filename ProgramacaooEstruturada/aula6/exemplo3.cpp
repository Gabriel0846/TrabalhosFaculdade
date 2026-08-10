#include <stdio.h>

int main(){
    FILE *arquivo;
    char linha[100];

    //abre o arquivo para leitura
    arquivo = fopen("arquivo.txt", "r");
    int nlinha = 1;

    //verifica se o arquivo foi aberto com sucesso
    if (arquivo != NULL) {
        //le linha a linha até o fim do arquivo
        while (fgets(linha, sizeof(linha), arquivo) != NULL){
            //imprime a linha lida na tela
            printf("linha %d: %s", nlinha, linha);
            nlinha += 1;
        }

        //fecha o arquivo
        fclose(arquivo);
    } else {
        //exibe mensagem de erro se não for possivel abrir o arquivo
        printf("erro ao abrir o arquivo.\n");
    }
    return 0;
}
