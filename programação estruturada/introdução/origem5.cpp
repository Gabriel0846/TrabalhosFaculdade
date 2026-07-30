#include <stdio.h>

main() {
    int cont = 1;

    while (cont <=100)
    {
        if (!(cont % 2))
        {
            printf("%d ", cont);
        }
        cont++;
    }
    return 0;
}