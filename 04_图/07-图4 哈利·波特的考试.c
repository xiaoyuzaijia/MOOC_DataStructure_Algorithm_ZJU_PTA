#include<stdio.h>
#include<string.h>
#define MAXN 100
#define MAXM 100
#define MAXDIST 100000

int N, M;
typedef int MGraph[MAXN][MAXM];


void createGraph(MGraph G){
    for (int i=0; i<N; i++){
        for (int j=0; j<N; j++){
            if (i == j){
                G[i][j] = 0;
            }
            else{
                G[i][j] = MAXDIST;
            }
        }
    }
}

void createEdge(MGraph G){
    int a, b, weight;
    
    for (int i=0; i<M; i++){
        scanf("%d %d %d", &a, &b, &weight);
        G[a-1][b-1] = weight;
        G[b-1][a-1] = weight;
    }
}

void Flord(MGraph D){
    for (int k=0; k<N; k++){
        for (int i=0; i<N; i++){
            for (int j=0; j<N; j++){
                if (D[i][k] +D[k][j] < D[i][j]){
                    D[i][j] = D[i][k] +D[k][j];
                }
            }
        }
    }
}

int findMax(MGraph D, int i){
    int maxCode = 0;
    for (int j=0; j<N; j++){
        if (D[i][j] > maxCode){
            maxCode = D[i][j];
        } 
    }
    return maxCode;
}

int main(){
    MGraph G, D;
    int animal, minCode, maxCode;
    
    scanf("%d %d", &N, &M);
    
    createGraph(G);
    createEdge(G);
    memcpy(D, G, sizeof(G));
    Flord(D);

    animal = 0;
    minCode = MAXDIST;
    for (int i=0; i<N; i++){
        maxCode = findMax(D, i);
        if (maxCode < minCode){
            animal = i;
            minCode = maxCode;
        }
    }
    if (minCode == MAXDIST){
        printf("0\n");
    }
    else{
        printf("%d %d\n", animal+1, minCode);
    }
    
    return 0;
}