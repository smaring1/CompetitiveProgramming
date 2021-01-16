#include <iostream>
#include <bits/stdc++.h>
#include <string>

using namespace std;

int main(){
    // ---- Sizeof ----
    //Retorna el size del operand que este siendo visto
    //Cuando el operand es un data type (char, int, float) retorna cuanta memoria esta alocando a ese tipó de dato
    sizeof(int); //Bytes 8


    // ---- new and delete operators ----
    int *ptr;
    ptr = new int; // new datatype -> With this word c++ is going to allocate memory from the heap and returns the address from the allocated memory
    *ptr = 24; //tambien se puede asi: ptr = new int(24);
    cout << *ptr; 
    delete ptr; //After doing operations with the variables in the allocated memory we need to free that space again

    // ---- Dynamic allocation arrays ----
    int *ptr2 = NULL;
    cout << "Size of array" << endl;
    int input;
    cin >> input;

    ptr2 = new int[input]; //If input is 3 its gonna allocate enough space for 3 ints
    for(int i = 0; i<input; ++i){
        cin >> *(ptr2+i); //ptr array cin
    } 

    delete []ptr2; //BRACKETS B4 NAME
}