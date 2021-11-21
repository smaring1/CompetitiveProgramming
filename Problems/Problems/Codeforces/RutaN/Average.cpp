#include <iostream>
#include <string>
using namespace std;

int main() 
{
    int size;
    int test;
    int students;
    int tempGrade;
    int grade = 0;
    cin >> size;
    for(int i =0; i < size; i++){
        cin << test << students;
        for(int i = 0; i < students; i++){\
            grade = 0;
            for(int i =0; i < test; i++){
                cin >> tempGrade;
                grade += tempGrade;
            }
            
        }
    return 0;
}