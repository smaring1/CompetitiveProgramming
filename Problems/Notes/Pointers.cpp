#include <iostream>
#include <bits/stdc++.h>
#include <string>
typedef long long ll;
#define for (n) for (int i = 0; i < n; i++)

using namespace std;

void Pointers(){
    // ------ & Address operator! ------
    // Returns the address of the memory location
    int variable = 10;
    cout << variable << " " << &variable <<endl; // se impirme: 10 0x23f5

    //------ Pointer ------
    // They print the values stored at a memory location
    // A pointer is a variable which contains the address of a variable
    int *variableptr = &variable;


    cout << variable << " " << variableptr <<endl; // se impirme: 10 0x23f5
    cout << *variableptr << endl; // se impirme: 0x23f5

    //------ Pass by address ------
    /*
    int variable = 8;
    display(&variable); //Sale 8
    cout << variable; //Sale 100

    void display(int *ptrargument){
        cout << *ptr << endl;
        *ptr = 100; //Al modificar el valor en memoria se cambia la variable sin improtar donde se este
    }
    */

    // ----- Arrays y pointers ------
    //Un array es una estructura lineal pues sus datos estan guardados en espacios contiguos y continuos de memoria
    int numeros[5] = {1,2,3,4,5};
    cout << numeros; //Sale la direccion en memoria
    cout << *numeros; //Sale el primer numero del array, al declarar el array este guarda la memoria del primer elemento
    cout << *(numeros+2); //Sale el tercer elemento, al ser continuo el avanzar los elementos dara las siguientes direcciones

    //----- CONST con pointers, funciones y arrays -----
    /*
    void display(const int num[]){
        for(int i = 0; i<num.size(); ++i){
            cout << num[i] << endl;
        }
    }
    */

   //----- Rangos de un array con pointers -----
    /*
    int nums[5] = {1,2,3,4,5};
    display(numbers, numbers+4); //Saldrian todos los numeros 

    void display(const int *start, const int *end){
        int *ptr;
        for(ptr = start; ptr != end; ++ptr){
            cout << *ptr << endl;
        }
        En cada vuelta aumenta en 1 el memory address, luego hace explicit deconversion
        E imprime el valor
    }
   */
}

