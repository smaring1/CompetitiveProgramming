#include <iostream>
using namespace std;

int main() 
{
    int size;
    cin >> size;
    for(int i = 0; i < size; i++) {
        int p, e;
        cin >> p >> e;
        if (p-e >= 10) {
            cout << "YES" << "\n";
        } else {
            cout << "NO" << "\n";
        }
    }
    return 0;
}