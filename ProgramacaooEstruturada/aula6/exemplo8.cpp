#include <stdio.h>

//definição de uma estrutura de exemplo
typedef struct {
    int id;
    float value;
} Data;

int main(){
    //dados para escrever no arquivo
    Data data_out = {1,123.45};
    Data data_in;
    
    //abrir arquivo para escrita em modo binario
    FILE *file = fopen("data.bin", "wb");
    if (file == NULL){
        printf("erro ao abrir o arquivo para escrita\n");
        return 1;
    }

    //escrever dados no arquivo
    size_t written = fwrite(&data_out, sizeof(Data), 1, file);
    if (written != 1){
        printf("erro ao excrever no arquivo\n");
        fclose(file);
        return 1;
    }

    //fechar o arquivo
    fclose(file);

    //abrir arquivo para leitura em modo binario
    file = fopen("data.bin", "rb");
    if (file == NULL){
        printf("erro ao abrir o arquivo para leitura\n");
        return 1;
    }

    //ler dados do arquivo
    size_t read = fread(&data_in, sizeof(Data), 1, file);
    if (read != 1){
        printf("erro ao ler do arquivo\n");
        fclose(file);
        return 1;
    }

    //fechar o arquivo
    fclose(file);

    //exibir os dados lidos
    printf("id: %d, value: %.2f\n", data_in.id, data_in.value);    
    
    return 0;
}
