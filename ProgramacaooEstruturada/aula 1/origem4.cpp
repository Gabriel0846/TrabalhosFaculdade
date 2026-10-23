#include <stdio.h>

int main() {
    int cont;
    for (cont = 1; cont < 101; cont++) {
        if(!(cont % 2)){
            printf("%d ", cont);
            printf("\t");
        }
    }
}
