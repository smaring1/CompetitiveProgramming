#include <iostream>
#include <string>
using namespace std;

int main() 
{
    int size;
    int total = 0;
    int n;
    int suma;
    cin >> size;
    for (int i = 0; i < size; i++) {
        cin >> n;
        for (int j = 1; j <= n; j++) {
            total += ((j * (j + 1)) / 2);
        }
        cout << total << "\n";
        total = 0;
    }
    return 0;
}