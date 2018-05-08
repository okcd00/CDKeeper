#include <stdio.h>

int main()
{
    int n,m,max=0,min;
    int i,j,k;
    char items[101][51];
    int len[101]={0};
    int flag[101]={0};
    scanf("%d%d",&n,&m);
    for (i=0;i<m;i++)
    {
        scanf("%s",&items[i]);
         for (j=0;j<n;j++)
             for (k=j+1;k<n;k++)
               if (items[i][j]>items[i][k]) len[i]++;
        if (len[i]>max) max=len[i];
    }

     for (i=0;i<m;i++)
     {
         min=max+1;
         for (j=0;j<m;j++)
             if ((len[j]<min) && (flag[j]==0))
             {
                 min=len[j];
                 k=j;
             }
        flag[k]=1;
        printf("%s\n",items[k]);
     }

    return 0;

}