/*
����ת��һ�¾���������������������ĺ�ģM����0.
��ΪҪ������������������Զ���������ͬ��ǰi��ͣ�
��¼�õ�����������������ǰk1����������ǰk2�
k2-k1��Ϊ������������г���
*/
#include <cstdio>
#include <cstring>

#define MAXM 10000

int n,m;
int a[MAXM];

int main()
{
  int i,s,x,ans;
  while (scanf("%d%d",&n,&m)==2)
  {
    memset(a,-1,sizeof(a));
    a[0]=0;
    s^=s;
    ans^=ans;
    for (i=1;i<=n;i++)
    {
      scanf("%d",&x);
      s+=x;
      if (s>=0)
        s=s%m;
      else
        s=(s%m+m)%m;
      if (a[s]==-1)
        a[s]=i;
      else
      {
        if (i-a[s]>ans)
          ans=i-a[s];
      }
    }
    printf("%d\n",ans);
  }
  return 0;
}