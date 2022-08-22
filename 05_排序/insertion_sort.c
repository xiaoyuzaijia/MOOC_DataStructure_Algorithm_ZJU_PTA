#include<stdio.h>

int N;
int A[100000];


void insertion_sort(){
    int tmp, i;

    for (int p=1; p<N; p++){
        tmp = A[p];
        for (i=p; i>0 && A[i-1] > tmp; i--){
            A[i] = A[i-1];
        }
        A[i] = tmp;
    }
}

int main(){
    scanf("%d", &N);
    for (int i=0; i<N; i++){
        scanf("%d", &A[i]);
    }
    
    insertion_sort();
    
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