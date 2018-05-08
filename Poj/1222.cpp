#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
using namespace std;


#define maxn 32
int a[maxn];
int g[maxn][maxn];
int mark[maxn][maxn];
int cnt;
int x[maxn];


const int dx[]={-1,0,1,0};
const int dy[]={0,1,0,-1};


void init(){ //初始化
    cnt=0;
    for(int i=0;i<5;i++)
        for(int j=1;j<=6;j++)
            mark[i][j]=++cnt;
}


void add(int n){  //一维数组导入二维数组 
    int x=(n-1)/6;
    int y=n-x*6;
    int cnt=0;
    g[n][n]=1;
    for(int i=0;i<4;i++){
        int nx=x+dx[i];
        int ny=y+dy[i];
        if(nx>=0 && nx<5 && ny>=1 && ny<=6){
            int id=mark[nx][ny];
            g[n][id]=1;
            cnt++;
        }
    }
    cnt++;
    if(cnt&1)   g[n][31]=a[n]^1;
    else g[n][31]=a[n];
}


void gauss(int n,int m){
    int i,j,row,col,k;
    for(row=1,col=1;row<n,col<m;row++,col++){
        for(k=row;;k++) if(g[k][col])   break;
        if(k!=row){
            for(j=col;j<=m;j++) swap(g[k][j],g[row][j]);
        }
        for(i=row+1;i<=n;i++){
            if(g[i][col]==0)    continue;
            for(j=col;j<=m;j++) g[i][j]^=g[row][j];
        }
    }
    for(i=n;i>=1;i--){
        x[i]=g[i][m];
        for(j=i+1;j<=n;j++) x[i]^=(x[j]&g[i][j]);
        x[i]&=g[i][i];
    }
}


int main(){
    int i,j,nn=0,cs;
    //freopen("test","r",stdin);
    init();
    scanf("%d",&cs);
    while(cs--){
        for(i=1;i<=30;i++)  scanf("%d",&a[i]);
        memset(g,0,sizeof(g));
        for(i=1;i<=30;i++)
            add(i);
        gauss(30,31);
        printf("PUZZLE #%d\n",++nn);
        for(i=1;i<=30;i++){
            printf("%d",1-x[i]);
            if(i%6==0)  printf("\n");
            else printf(" ");
        }
    }
    return 0;
}