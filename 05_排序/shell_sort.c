#include<stdio.h>

int N;
int A[100000];


void shell_sort1(){
    int tmp, d, p, i;

    for (d=N/2; d>0; d/=2){
        for (p=d; p<N; p+=d){
            tmp = A[p];
            for (i=p; i>0 && A[i-d]>tmp; i-=d){
                A[i] = A[i-d];
            }
            A[i] = tmp;
        }
    }
}

int main(){
    scanf("%d", &N);
    for (int i=0; i<N; i++){
        scanf("%d", &A[i]);
    }
    
    shell_sort1();
    
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