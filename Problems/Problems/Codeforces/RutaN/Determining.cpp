#include <iostream>
#include <string>
using namespace std;


void aux(int n) {

    int i = 2;
    int aux = 0;
    int goal = n % 2147483647;
    int fib[n+2];

    fib[0] = 0;
    fib[1] = 1;
    while(aux < goal || i < n){
        cout << "öli";
        fib[i] = fib[i-1] + fib[i-2];
        aux = fib[i];
        if (aux == goal) {
            cout << "YES" << "\n";
            return;   
        }
        i++;
    }
    cout << "NO" << "\n";
    return;

}

int main() 
{
    int size;
    cin >> size;
    for (int i = 0; i < size; i++) {
        int n;
        cin >> n;
        aux(n);
        //cout << fibo(n) << "\n";
    }
    return 0;
}