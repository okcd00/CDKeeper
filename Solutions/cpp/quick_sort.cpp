#include <bits/stdc++.h>
using namespace std;


//严蔚敏《数据结构》标准分割函数
int Paritition1(int A[], int low, int high)
{
  int pivot = A[low];
  while (low < high)
  {
    while (low < high && A[high] >= pivot)
    {
      --high;
    }
    A[low] = A[high];
    while (low < high && A[low] <= pivot)
    {
      ++low;
    }
    A[high] = A[low];
  }
  A[low] = pivot;
  return low;
}

void QuickSort(int A[], int low, int high) //快排母函数
{
  if (low < high)
  {
    int pivot = Paritition1(A, low, high);
    QuickSort(A, low, pivot - 1);
    QuickSort(A, pivot + 1, high);
  }
}

int main()
{
  int A[10]{1,9,2,3,4,6,6,6,7,8}; 
  QuickSort(A, 0, 9);
  for(int i=0; i<10; i++)
  {
    cout << A[i] << endl;
  }
}
