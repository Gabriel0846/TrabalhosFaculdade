#include <stdio.h>

struct pessoa{
    char nome[50];
    int idade;
};

void print_pessoa(struct pessoa *pessoa){
    printf("nome: %s\n", pessoa->nome);
    printf("idade: %d\n", pessoa->idade);
}

void altera_idade(struct pessoa *pessoa, int nova_idade){
    pessoa->idade = nova_idade;    
}

int main(){
    struct pessoa pessoa = {"joao silva", 25};

    print_pessoa(&pessoa);

    //modifica a idade da pessoa dentro da funcao
    altera_idade(&pessoa, 30);

    print_pessoa(&pessoa);

    return 0;
}
