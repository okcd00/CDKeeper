#include <cmath> 
#include <cctype>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define Max(a,b) ((a)>(b)?(a):(b))
#define Min(a,b) ((a)<(b)?(a):(b))

struct node
{
      int left,right;//��˵㡢�Ҷ˵�
      int n;//��¼�����߶γ����˶��ٴΣ�Ĭ��Ϊ0
}a[16];

void insert(int s,int t,int step)//Ҫ������߶ε���˵���Ҷ˵㡢�Լ���ǰ�߶����е�ĳ���߶�
{
      if (s==a[step].left && t==a[step].right)
      {
            a[step].n++;//������߶�ƥ��������߶εļ�¼+1
            return;//�����������
      }
      if (a[step].left==a[step].right)   return;//��ǰ�߶������߶�û�ж��ӣ������������
      int mid=(a[step].left+a[step].right)/2;
      if (mid>=t)    insert(s,t,step*2);//����е���t���ұߣ���Ӧ�ò��뵽�����
      else if (mid<s)    insert(s,t,step*2+1);//����е���s����ߣ���Ӧ�ò��뵽�Ҷ���
      else//�����е�һ����s��t֮�䣬�Ѵ����߶ηֳ�����ֱ�嵽���Ҷ�������
      {
            insert(s,mid,step*2);
            insert(mid+1,t,step*2+1);
      }
}


int main()
{
	
	return 0;
}
