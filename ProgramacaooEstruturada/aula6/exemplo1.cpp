#include <stdio.h>

int main(void) {
    FILE *file = fopen("example.txt", "r");

    if (file == NULL) {
        printf("Erro ao abrir o arquivo.\n");
        return 1;
    }

    // Leitura ou operação com o arquivo aqui
    
    fclose(file);
    return 0;
}
