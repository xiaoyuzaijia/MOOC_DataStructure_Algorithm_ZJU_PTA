#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

struct Stu{
    int id, all, pef, r;
    int p[6] = {-2, -2, -2, -2, -2, -2};
} a[10001];

int n, m, k;
int pf[6];

int sum(Stu a){
    int i, s=0;
    
    for (i=1; i<=k; i++){
        if (a.p[i] > 0) s += a.p[i];
    }
    
    return s;
}

int count_pef(Stu a){
    int i, s = 0;
    for (i=1; i<=k; i++){
        if (a.p[i] == pf[i]) s++;
    }
    return s;
}

bool cmp(Stu a, Stu b){
    if (a.all != b.all) return a.all > b.all;
    else if (a.pef != b.pef) return a.pef > b.pef;
    else return a.id < b.id;
}

int main(){
    int i, j;
    scanf("%d %d %d", &n, &k, &m);
    for (i=1; i<=k; i++) scanf("%d ", &pf[i]);
    
    for (i=0; i<m; i++){
        int id, pr, sc;
        scanf("%d %d %d", &id, &pr, &sc);
        a[id].id = id;
        if (a[id].p[pr] < sc){
            a[id].p[pr] = sc;
        }
    }
    
    vector<Stu> rank;
    for (i=1; i<=n; i++){
        int join = 0;
        for (j=1; j<=k; j++){
            if (a[i].p[j] >= 0) {join = 1; break;}
        }
        
        if (join){
            a[i].all = sum(a[i]);
            a[i].pef = count_pef(a[i]);
            rank.push_back(a[i]);
        }
    }
    
    sort(rank.begin(), rank.end(), cmp);
    
    Stu h;
    h.all = -1;
    rank.insert(rank.begin(), h);
    for (i=1; i<(int)rank.size(); i++){
        if (rank[i].all != rank[i-1].all) rank[i].r = i;
        else rank[i].r = rank[i-1].r;
        
        printf("%d %05d %d", rank[i].r, rank[i].id, rank[i].all);
        for (j=1; j<=k; j++){
            if (rank[i].p[j] >= 0) printf(" %d", rank[i].p[j]);
            else if (rank[i].p[j] == -1) printf(" 0");
            else printf(" -");
        }
        printf("\n");
    }
    
    return 0;
}