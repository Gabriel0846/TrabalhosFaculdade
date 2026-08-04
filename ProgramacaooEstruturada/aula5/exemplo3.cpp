#include <stdio.h>

void sort(int *array, int size){
    //algoritimo de ordenação (ex: bubble sort)
    for (int i = 0; i < size - 1; i++){
        for (int j = 0; j < size - i - 1; j++){
            if (array[j] > array[j +1]){
                //troca os elementos do array
                int temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
        }
    }
}

int main(){
    int array[] = {5, 2, 4, 6, 1, 3};
    int size = sizeof(array) / sizeof(array[0]);

    sort(&array[0], size);

    //imprime o array ordenado
    for (int i = 0; i < size; i++){
        printf("%d ", array[i]);
    }

    printf("\n");

    return 0;
}
