#include<stdio.h>
#include<memory.h>
int main()
{
    int i,j,k,v[10001],sum,t,t1;
    memset(v,0,sizeof(v));
    for(i=1;i<10000;i++)
    {
        if(v[i])continue;else printf("%d\n",i);
        sum=i;v[i]=1;   
        while(sum<10000)
        {
            t=sum;
            while(t)
            {t1=t%10;t=t/10;sum+=t1;}
            if(sum<10000)v[sum]=1;
        }    
    }    
    return 0;
}    