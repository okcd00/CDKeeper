#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

char str[1005][25];

struct trienode
{
    int num;
    struct trienode *next[26];
}Root;

trienode *newnode()
{
    trienode *temp = new trienode;
    temp->num = 1;
    for(int i = 0; i<26; i++)
        temp->next[i] = NULL;
    return temp;
}

void insert(char *tar)
{
    int id;
    trienode *p = &Root;
    while(*tar)
    {
        id = *tar - 'a';
        if(p->next[id] == NULL)
        {
            p->next[id] = newnode();
        }
        else 
            p->next[id]->num++;
        p = p->next[id];
        tar++;
    }
}

void search(char *tar)
{
    int id;
    trienode *p = &Root;
    while(*tar)
    {
        id = *tar - 'a';
        if(p->next[id] ->num == 1)
        {
            printf("%c",*tar);
            return;
        }
        else 
            printf("%c",*tar);
        p = p->next[id];
        tar++;
    }
}
int main()
{
    //freopen("in.txt","r",stdin);
    int n = 0;
    while(scanf("%s",str[n])!=EOF)
    {
        insert(str[n]);
        n++;
    }
    for(int i = 0; i<n; i++)
    {
        printf("%s ",str[i]);
        search(str[i]);
        printf("\n");
    }
    return 0;
}