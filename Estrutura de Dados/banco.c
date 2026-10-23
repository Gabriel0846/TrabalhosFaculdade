#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int numero;
    char prioridade;
    struct Node* prox;
} Node;

Node* head = NULL;
int contC = 1;
int contP = 301;

void inserirSemPriori(Node* novo) {
    if (head == NULL) {
        head = novo;
        return;
    }
    
    Node* atual = head;
    while (atual->prox != NULL) {
        atual = atual->prox;
    }
    atual->prox = novo;
}

void inserirComPriori(Node* novo) {
    if (head == NULL) {
        head = novo;
        return;
    }
    
    if (head->prioridade == 'C') {
        novo->prox = head;
        head = novo;
        return;
    }
    
    Node* atual = head;
    while (atual->prox != NULL && atual->prox->prioridade == 'P') {
        atual = atual->prox;
    }
    
    novo->prox = atual->prox;
    atual->prox = novo;
}

void inserirCli() {
    char prio;
    printf("prioridade (P ou C): ");
    scanf(" %c", &prio);
    
    Node* novo = (Node*)malloc(sizeof(Node));
    novo->prox = NULL;
    
    if (prio == 'C' || prio == 'c') {
        novo->prioridade = 'C';
        novo->numero = contC++;
    } else if (prio == 'P' || prio == 'p') {
        novo->prioridade = 'P';
        novo->numero = contP++;
    } else {
        printf("prio invalida!\n");
        free(novo);
        return;
    }
    
    if (head == NULL) {
        head = novo;
    } else if (novo->prioridade == 'C') {
        inserirSemPriori(novo);
    } else {
        inserirComPriori(novo);
    }
    
    printf("cliente add: %c%d\n", novo->prioridade, novo->numero);
}

void mostrarFila() {
    if (head == NULL) {
        printf("fila vazia!\n");
        return;
    }
    
    printf("fila: ");
    Node* atual = head;
    while (atual != NULL) {
        printf("%c%d ", atual->prioridade, atual->numero);
        atual = atual->prox;
    }
    printf("\n");
}

void atender() {
    if (head == NULL) {
        printf("sem clientes!\n");
        return;
    }
    
    Node* temp = head;
    printf("atendendo: %c%d\n", head->prioridade, head->numero);
    head = head->prox;
    free(temp);
}

int main() {
    int op;
    
    do {
        printf("\n--- menu ---\n");
        printf("1 - add cliente\n");
        printf("2 - mostrar fila\n");
        printf("3 - chamar cliente\n");
        printf("4 - sair\n");
        printf("opcao: ");
        scanf("%d", &op);
        
        switch(op) {
            case 1:
                inserirCli();
                break;
            case 2:
                mostrarFila();
                break;
            case 3:
                atender();
                break;
            case 4:
                printf("saindo...\n");
                break;
            default:
                printf("opcao inv!\n");
        }
    } while (op != 4);
    
    while (head != NULL) {
        Node* temp = head;
        head = head->prox;
        free(temp);
    }
    
    return 0;
}