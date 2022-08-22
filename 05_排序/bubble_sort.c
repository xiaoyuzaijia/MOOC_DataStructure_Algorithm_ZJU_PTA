#include<stdio.h>

int N;
int A[100000];

void swap(int *a, int *b){
    int tmp;
    
    tmp = *a;
    *a = *b;
    *b = tmp;
}

void bubble_sort(){
    int flag;
    
    for (int p=N-1; p>0; p--){
        flag = 0;
        for (int i=0; i<p; i++){
            if (A[i] > A[i+1]){
                swap(&A[i], &A[i+1]);
                flag = 1;
            }
        }
        if (flag == 0){
            break;
        }
    }
}

int main(){
    scanf("%d", &N);
    for (int i=0; i<N; i++){
        scanf("%d", &A[i]);
    }
    
    bubble_sort();
    
    for (int i=0; i<N; i++){
        if (i != N-1){
            printf("%d ", A[i]);
        }
        else{
            printf("%d\n", A[i]);
        }
    }
    
    return 0;
}