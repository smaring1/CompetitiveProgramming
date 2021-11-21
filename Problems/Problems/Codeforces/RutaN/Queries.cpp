#include <iostream>
#include <string>
using namespace std;

int main() 
{
    int cases;
    cin >> cases;
    for(int i = 0; i < cases; i++) {
        int queries;
        cin >> queries;
        stack<int> st;
        for(int j = 0; j < queries; j++) {
            
        }
    }
    
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