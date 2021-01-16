#include <bits/stdc++.h>

using namespace std;

struct simon{
    string name;
    int age;
};

void display(int *ptr){
    cout << *ptr << endl;
    *ptr = 100; //Al modificar el valor en memoria se cambia la variable sin improtar donde se este
}

int main(){
    // ----- Arrays y pointers ------
    //Un array es una estructura lineal pues sus datos estan guardados en espacios contiguos y continuos de memoria
    int numeros[5] = {1,2,3,4,5};
    
    //x--; 1 ---> 5 4 3 2 1 (0)
    //--x; 2 ---> 4 3 2 1   (0)
    
}

