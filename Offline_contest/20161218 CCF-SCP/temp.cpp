#include <queue>
#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

#define MAXN 100

struct In
{
	int data;
	char str[100];
}s[MAXN];

int cmp (const void *a, const void *b)
{
	return strcmp( (*(In *)a).str, (*(In *)b).str );
}

int main()
{
	qsort(s, MAXN,sizeof(s[0],cmp))
	return 0;
}

