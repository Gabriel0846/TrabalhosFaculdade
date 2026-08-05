#include <stdio.h>
#include <string.h>

//funcao auxiliar para trocar dois caracteres em uma string
void trocar(char *a, char *b){
    char temp = *a;
    *a = *b;
    *b = temp;
}

//funcao recursiva para gerar todas as permutacoes de uma string
void permutar(char *string, int inicio, int fim){
    if (inicio == fim) //condicao de parada
    printf("%s\n", string);
    else {
        for (int i = inicio; i <= fim; i++){
            trocar((string + inicio), (string + i));
            permutar(string, inicio + 1, fim);
            trocar((string + inicio), (string + i)); //reverter a troca
        }
    }
}

int main(){
    char str[] = "ABC";
    int tamanho = strlen(str);
    printf("todas as permutações de %s são: \n", str);
    permutar(str, 0, tamanho - 1);
    return 0;
}
