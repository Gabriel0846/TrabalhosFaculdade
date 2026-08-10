#include <stdio.h>

int main(){
    FILE *arquivo;
    int idade = 25;
    float peso = 75.5;
    char nome[100] = "João Silva";

    //abre o arquivo para escrita
    arquivo = fopen("arquivo_fprint.txt", "w");

    //verifica se o arquivo foi aberto com sucesso
    if (arquivo != NULL) {
        //escreve os dados formatados no arquivo
        fprintf(arquivo, "idade: %d\n", idade);
        fprintf(arquivo, "peso: %.2f\n", peso);
        fprintf(arquivo, "nome: %s", nome);

        //fecha o arquivo
        fclose(arquivo);
        printf("dados formatados escritos no arquivo com sucesso.\n");
    } else {
        //exibe mensagem de erro se não for possivel abrir o arquivo
        printf("erro ao abrir o arquivo.\n");
    }
    return 0;
}
