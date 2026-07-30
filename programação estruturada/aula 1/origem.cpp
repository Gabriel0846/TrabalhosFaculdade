#include <stdio.h>

int main() {
	int idade;

	char nome[45];

	printf("digite seu nome: ");

	fgets(nome, 44, stdin);

	printf("digite sua idade: ");
	scanf("%d", &idade);
	printf("idade de %s eh de %d", nome, idade);
	
	return 0;
};