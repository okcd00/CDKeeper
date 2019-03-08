#include<iostream>
#include<windows.h>

using namespace std;

int main() {
    int t = 100;
//    for(int i = 1; i <= 1; ++i) {
//        cout << "Test: " << i << endl;
//        system("gene > in.txt");
//        system("std < in.txt > 1.txt");
//        system("std_bf < in.txt > 2.txt");
//        if(system("fc /a 1.txt 2.txt")) break;
//    }

    system("gene > 1.in");
    system("std < 1.in > 1.out");
    return 0;
}
