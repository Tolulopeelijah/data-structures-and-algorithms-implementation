#include <stdio.h>

void merge(int[] array){
    if (sizeof(array) <= 1){
        return array;
    }
    int mid = sizeof(array) // 2;
    int[mid/2] left = merge(array[:mid]);
    int[mid/2] right = merge(array[mid:]);
    
    return merge_sort(left, right);

}
void merge_sort(int[] left, int[] right){
    int l = 0, r = 0
    int len = sizeof(left) + sizeof(right);
    int[len] sorted_array;

    while (l <= sizeof(left) and r >= sizeof(right)){
        if (left[l] <= right[r]){
            sorted_array[k] = left[l];
            l ++;
            k ++;
        }
        else{
            sorted_array[k] = right[r];
            r ++;
            k ++;
        }
    }
    while (l <= sizeof(left)){
        sorted_array[k] = left[l];
        l ++;
        k ++;
    }
    while (r <= sizeof(right)){
        sorted_array[k] = right[r];
        r ++;
        k ++;
    }
}
void main(){
    int[8] array = {8, 2, 7, 6, 3, 5, 4, 1};
    for (int i = 0;i < 8; i++){
        printf("%d", array[i]);
    }
}