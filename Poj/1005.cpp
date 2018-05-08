#include <stdio.h>
int main()
{
    float s,x,y;
    int n;
    int i,year;
    scanf("%d",&n);
    for (i=1;i<=n;i++)
    {
        scanf("%f %f",&x,&y);
        s=(x*x+y*y)*3.14/2.0;
        year=(int)(s/50)+1  ;
        printf("Property %d: This property will begin eroding in year %d.\n",i,year);
    }
    printf("END OF OUTPUT.\n");
    return 0;
}