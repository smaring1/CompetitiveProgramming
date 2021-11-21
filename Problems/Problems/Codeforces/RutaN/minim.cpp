#include <iostream>
#include <string>
using namespace std;

int main() 
{
    int size;
    cin >> size;
    string line;
    cin.ignore();
    getline(cin, line);
    int total = 0;
    for (char c : line) {
        if (c == '0') {
            total += 2;
        }
        if 
    }
    cout << "EASY" << "\n";
    return 0;
}