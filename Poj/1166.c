#include<stdio.h>
#include<stdlib.h>
int a[10],b[10],c[10],ans,num=1000000,i,j,t,k;
int main()
{
    for(i=1;i<10;i++)
        scanf("%d",&a[i]);
    for(i=0;i<256;i++)
    {
        b[1]=i&3,b[2]=(i&(3<<2))>>2,b[7]=(i&(3<<4))>>4,b[8]=(i&(3<<6))>>6;
        c[1]=(b[1]+b[2]+a[1])%4,c[7]=(b[7]+b[8]+a[7])%4;
        if(c[1]-c[7])
            continue;
        b[4]=(4-c[1])%4;
        c[4]=(b[4]+a[4]+b[1]+b[7])%4;
        b[5]=(4-c[4])%4;
        c[2]=(a[2]+b[1]+b[2]+b[5])%4;
        c[8]=(a[8]+b[7]+b[8]+b[5])%4;
        b[3]=(4-c[2])%4;
        b[9]=(4-c[8])%4;
        c[5]=(a[5]+b[1]+b[7]+b[5]+b[9]+b[3])%4;
        if(c[5])
            continue;
        c[3]=(a[3]+b[2]+b[3])%4;
        c[9]=(a[9]+b[8]+b[9])%4;
        c[6]=(a[6]+b[3]+b[5]+b[9])%4;
        if(c[3]-c[9]||c[3]-c[6])
            continue;
        b[6]=(4-c[3])%4;
        for(k=1,j=0;k<=9;k++)
            j+=b[k];
        if(num<=j)
            continue;
        for(k=1,t=0;k<=9;k++)
            t|=b[k]<<(k<<1);
        num=j;ans=t;
    }
    for(i=1;i<=9;i++)
    {
        t=(ans&(3<<(i<<1)))>>(i<<1);
        for(j=0;j<t;j++)
            printf("%d ",i);
    }
    printf("\n");

}