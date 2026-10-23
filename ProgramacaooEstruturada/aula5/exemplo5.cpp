#include <stdio.h>

//definicao de um enum para os dias da semana
enum dias_da_semana {
    DOMINGO,
    SEGUNDA,
    TERCA,
    QUARTA,
    QUINTA,
    SEXTA,
    SABADO
};
int main(){
    //declaracao de uma variavel de tipo enum dias_da_semana
    enum dias_da_semana dia = SEGUNDA;
    //impressao do dia da semana
    switch (dia){
        case DOMINGO:
            printf("domingo.\n");
            break;
        case SEGUNDA:
            printf("segunda-feira.\n");
            break;
        case TERCA:
            printf("terca-feira.\n");
            break;
        case QUARTA:
            printf("quarta-feira.\n");
            break;
        case QUINTA:
            printf("quinta-feira.\n");
            break;
        case SEXTA:
            printf("sexta-feira.\n");
            break;
        case SABADO:
            printf("sabado.\n");
            break;
        default:
            printf("dia invalido\n");
            break;
    }
    return 0;
}
