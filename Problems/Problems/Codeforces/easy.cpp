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
    for (char c : line) {
        if (c == '1') {
            cout << "HARD" << "\n";
            return 0;
        }
    }
    cout << "EASY" << "\n";
    return 0;
}