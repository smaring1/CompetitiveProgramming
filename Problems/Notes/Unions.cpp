#include <iostream>
#include <bits/stdc++.h>
#include <string>
typedef long long ll;
#define for (n) for (int i = 0; i < n; i++)

using namespace std;

union worker{
    int id;
    float salary;
} Pedro; //Igual que un struct

int main(){
    //A union is like a struct except all its members share the smae memory
    // in a struct each member has a memory allocation

    worker miguel;
    miguel.id = 25;
    cout << miguel.id << endl;
    miguel.salary = 14;
    cout << miguel.id << endl; //En esta segundo cout sale un valor extraño, esto es por que el miguel.salary ocupo el espacio de id
}